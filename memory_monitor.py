#!/usr/bin/env python3
"""
DNOS Device Memory Monitor
Continuously monitors memory usage from Linux shell every 5 seconds
"""

import paramiko
import time
import json
import os
import sys
import re
from datetime import datetime
import threading


class DNOSMemoryMonitor:
    """Continuously monitors memory usage on DNOS device"""
    
    def __init__(self, device_config):
        self.hostname = device_config['hostname']
        self.ip_address = device_config['ip_address']
        self.username = device_config['username']
        self.password = device_config['password']
        self.ssh_client = None
        self.shell = None
        self.is_running = False
        self.memory_data = []
        self.save_counter = 0
        
    def clean_output(self, raw_output):
        """Clean ANSI escape sequences and formatting from output"""
        # Remove ANSI escape sequences
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        cleaned = ansi_escape.sub('', raw_output)
        
        # Remove carriage returns and extra whitespace
        cleaned = cleaned.replace('\r\n', '\n').replace('\r', '\n')
        
        # Remove terminal control sequences
        cleaned = re.sub(r'\?\d+[hl]', '', cleaned)
        
        # Remove prompt lines (lines containing the hostname and prompt)
        lines = cleaned.split('\n')
        filtered_lines = []
        for line in lines:
            if not (self.hostname in line and ('#' in line or '$' in line)):
                if line.strip() and not line.strip().startswith('free'):  # Skip command echo
                    filtered_lines.append(line.strip())
        
        return '\n'.join(filtered_lines)
    
    def parse_memory_info(self, output):
        """Parse free -h command output"""
        lines = output.split('\n')
        for line in lines:
            if 'Mem:' in line:
                parts = line.split()
                if len(parts) >= 7:
                    return {
                        "total": parts[1],
                        "used": parts[2], 
                        "free": parts[3],
                        "shared": parts[4],
                        "buff_cache": parts[5],
                        "available": parts[6]
                    }
        return {}
    
    def parse_meminfo(self, output):
        """Parse /proc/meminfo output"""
        info = {}
        lines = output.split('\n')
        for line in lines:
            if ':' in line and not line.startswith('('):
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()
        return info
    
    def connect(self):
        """Connect to device via SSH"""
        try:
            print(f"🔌 Connecting to {self.hostname} ({self.ip_address})...")
            
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            self.ssh_client.connect(
                hostname=self.ip_address,
                username=self.username,
                password=self.password,
                timeout=30
            )
            
            print(f"✅ Connected to {self.hostname}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to connect to {self.hostname}: {str(e)}")
            return False
    
    def access_linux_shell(self):
        """Access the device's Linux shell"""
        try:
            print(f"📡 Accessing Linux shell...")
            
            # Create interactive shell
            self.shell = self.ssh_client.invoke_shell()
            time.sleep(2)
            
            # Clear initial output and wait for CLI prompt
            if self.shell.recv_ready():
                self.shell.recv(4096)
            
            # Wait for CLI prompt
            time.sleep(1)
            prompt_found = False
            for _ in range(10):
                if self.shell.recv_ready():
                    data = self.shell.recv(1024).decode('utf-8', errors='ignore')
                    if '#' in data or '>' in data:
                        prompt_found = True
                        break
                time.sleep(0.5)
            
            if not prompt_found:
                print("⚠️ CLI prompt not clearly detected, continuing...")
            
            # Send "run start shell" command
            self.shell.send("run start shell\n")
            time.sleep(2)
            
            # Send password
            self.shell.send(self.password + '\n')
            time.sleep(3)
            
            # Clear any remaining output
            if self.shell.recv_ready():
                self.shell.recv(4096)
            
            print(f"🐧 Linux shell access established")
            return True
            
        except Exception as e:
            print(f"❌ Error accessing Linux shell: {str(e)}")
            return False
    
    def get_memory_data(self):
        """Get current memory data"""
        try:
            memory_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "memory_summary": {},
                "memory_details": {}
            }
            
            # Get free -h output
            self.shell.send("free -h\n")
            time.sleep(1)
            
            free_output = ""
            if self.shell.recv_ready():
                free_output = self.shell.recv(4096).decode('utf-8', errors='ignore')
            
            cleaned_free = self.clean_output(free_output)
            memory_data["memory_summary"] = self.parse_memory_info(cleaned_free)
            
            # Get /proc/meminfo output
            self.shell.send("cat /proc/meminfo | head -10\n")
            time.sleep(1)
            
            meminfo_output = ""
            if self.shell.recv_ready():
                meminfo_output = self.shell.recv(4096).decode('utf-8', errors='ignore')
            
            cleaned_meminfo = self.clean_output(meminfo_output)
            memory_data["memory_details"] = self.parse_meminfo(cleaned_meminfo)
            
            return memory_data
            
        except Exception as e:
            print(f"❌ Error getting memory data: {str(e)}")
            return None
    
    def display_memory_info(self, data):
        """Display memory information in a nice format"""
        if not data or not data.get("memory_summary"):
            return
            
        # Clear screen (optional)
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 80)
        print(f"🖥️  MEMORY MONITOR - {self.hostname} - {data['timestamp']}")
        print("=" * 80)
        
        mem = data["memory_summary"]
        if mem:
            print(f"💾 MEMORY USAGE:")
            print(f"   Total:      {mem.get('total', 'N/A')}")
            print(f"   Used:       {mem.get('used', 'N/A')}")
            print(f"   Free:       {mem.get('free', 'N/A')}")
            print(f"   Available:  {mem.get('available', 'N/A')}")
            print(f"   Shared:     {mem.get('shared', 'N/A')}")
            print(f"   Buff/Cache: {mem.get('buff_cache', 'N/A')}")
        
        # Calculate usage percentage if possible
        if mem.get('used') and mem.get('total'):
            try:
                used_val = float(re.findall(r'[\d.]+', mem['used'])[0])
                total_val = float(re.findall(r'[\d.]+', mem['total'])[0])
                
                # Convert to same units if needed
                used_unit = mem['used'][-2:]
                total_unit = mem['total'][-2:]
                
                if used_unit == total_unit:
                    usage_pct = (used_val / total_val) * 100
                    print(f"   Usage:      {usage_pct:.1f}%")
                    
                    # Visual progress bar
                    bar_length = 50
                    filled_length = int(bar_length * usage_pct / 100)
                    bar = '█' * filled_length + '░' * (bar_length - filled_length)
                    print(f"   [{bar}] {usage_pct:.1f}%")
                    
            except:
                pass
        
        details = data.get("memory_details", {})
        if details:
            print(f"\n📊 DETAILED MEMORY INFO:")
            interesting_keys = ['MemTotal', 'MemFree', 'MemAvailable', 'Buffers', 'Cached', 'Active', 'Inactive']
            for key in interesting_keys:
                if key in details:
                    # Convert KB to more readable format
                    try:
                        kb_value = int(details[key].split()[0])
                        if kb_value > 1024*1024:
                            readable = f"{kb_value/(1024*1024):.1f} GB"
                        elif kb_value > 1024:
                            readable = f"{kb_value/1024:.1f} MB"
                        else:
                            readable = f"{kb_value} KB"
                        print(f"   {key:<15}: {readable}")
                    except:
                        print(f"   {key:<15}: {details[key]}")
        
        print("\n" + "=" * 80)
        print(f"🔄 Monitoring every 5 seconds... (Press Ctrl+C to stop)")
        print(f"📁 Data saved every 10 seconds to: data/monitoring/{self.hostname}_memory_monitor.json")
        print("=" * 80)
    
    def save_data(self):
        """Save memory data to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Save to data/monitoring directory
            monitoring_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "monitoring")
            os.makedirs(monitoring_dir, exist_ok=True)
            filename = os.path.join(monitoring_dir, f"{self.hostname}_memory_monitor.json")
            
            output_data = {
                "metadata": {
                    "device_hostname": self.hostname,
                    "device_ip": self.ip_address,
                    "monitoring_started": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "total_samples": len(self.memory_data),
                    "interval_seconds": 5,
                    "save_frequency_seconds": 10
                },
                "memory_history": self.memory_data
            }
            
            with open(filename, 'w') as f:
                json.dump(output_data, f, indent=2)
            
            print(f"💾 Saved {len(self.memory_data)} samples to {filename}")
            
        except Exception as e:
            print(f"❌ Error saving data: {str(e)}")
    
    def monitor_memory(self):
        """Main monitoring loop"""
        try:
            self.is_running = True
            
            while self.is_running:
                # Get memory data
                data = self.get_memory_data()
                
                if data:
                    # Store data
                    self.memory_data.append(data)
                    
                    # Display current info
                    self.display_memory_info(data)
                    
                    # Save data every 10 seconds (2 samples * 5 seconds = 10 seconds)
                    self.save_counter += 1
                    if self.save_counter >= 2:
                        self.save_data()
                        self.save_counter = 0
                        
                        # Keep only last 1000 samples to prevent memory issues
                        if len(self.memory_data) > 1000:
                            self.memory_data = self.memory_data[-1000:]
                
                # Wait 5 seconds
                time.sleep(5)
                
        except KeyboardInterrupt:
            print(f"\n🛑 Monitoring stopped by user")
            self.is_running = False
        except Exception as e:
            print(f"❌ Error during monitoring: {str(e)}")
            self.is_running = False
        finally:
            # Final save
            if self.memory_data:
                self.save_data()
    
    def run(self):
        """Main run method"""
        try:
            # Connect to device
            if not self.connect():
                return False
            
            # Access Linux shell
            if not self.access_linux_shell():
                return False
            
            # Start monitoring
            self.monitor_memory()
            
            return True
            
        except Exception as e:
            print(f"❌ Monitor error: {str(e)}")
            return False
        finally:
            self.disconnect()
    
    def disconnect(self):
        """Disconnect from device"""
        try:
            self.is_running = False
            if self.shell:
                self.shell.close()
            if self.ssh_client:
                self.ssh_client.close()
            print(f"\n🔌 Disconnected from {self.hostname}")
        except:
            pass


def load_device_config(target_ip="192.168.162.141"):
    """Load device configuration for target IP"""
    # Look for config in organized data/config directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), "data", "config", "devices_config.json")
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        devices = config.get('devices', [])
        for device in devices:
            if device['ip_address'] == target_ip:
                return device
    else:
        print(f"❌ Config file not found at: {config_path}")
    
    return None


def main():
    """Main function"""
    print("🚀 DNOS Memory Monitor")
    print("=" * 50)
    
    try:
        # Load device configuration
        target_ip = "192.168.162.141"
        device_config = load_device_config(target_ip)
        
        if not device_config:
            print(f"❌ Device configuration not found for IP: {target_ip}")
            return
        
        print(f"📋 Target Device: {device_config['hostname']} ({device_config['ip_address']})")
        print(f"⏱️  Monitoring Interval: 5 seconds")
        print(f"💾 Data saves every 10 seconds")
        
        # Create monitor and run
        monitor = DNOSMemoryMonitor(device_config)
        success = monitor.run()
        
        if success:
            print(f"\n✅ Memory monitoring completed!")
        else:
            print(f"\n❌ Memory monitoring failed!")
            
    except KeyboardInterrupt:
        print(f"\n⚠️ Monitoring interrupted by user")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 