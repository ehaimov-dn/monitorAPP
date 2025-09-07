#!/usr/bin/env python3
"""
Optimized Interface Monitor and Database Updater
Connects to devices, monitors interfaces, and updates JSON database files
Optimized for devices with large numbers of interfaces (10k+)
"""

import json
import paramiko
import threading
import time
import sys
import os
import re
from datetime import datetime


class OptimizedDeviceInterfaceMonitor:
    """Optimized monitor for devices with large interface counts"""
    
    def __init__(self, device_config):
        self.hostname = device_config['hostname']
        self.ip_address = device_config['ip_address']
        self.username = device_config['username']
        self.password = device_config['password']
        self.ssh_client = None
        self.is_running = False
        self.interfaces = {}
        self.last_interface_count = 0
        
    def connect(self):
        """Connect to device"""
        try:
            print(f"[{self.hostname}] 🔗 Connecting...")
            
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            self.ssh_client.connect(
                hostname=self.ip_address,
                username=self.username,
                password=self.password,
                timeout=30
            )
            
            print(f"[{self.hostname}] ✅ Connected successfully")
            return True
            
        except Exception as e:
            print(f"[{self.hostname}] ❌ Connection failed: {str(e)}")
            return False
    
    def parse_interface_row(self, line):
        """Enhanced parser for interface table rows"""
        try:
            # Look for lines that start with | and contain interface data
            if line.strip().startswith('| ') and not line.strip().startswith('| Interface'):
                # Split by | and clean up fields
                parts = [part.strip() for part in line.split('|')]
                
                # Check if this looks like an interface line (has at least interface name)
                if len(parts) >= 10 and parts[1]:  # Interface name should not be empty
                    interface_name = parts[1]
                    
                    # Accept any interface name format, not just ge100-*
                    if interface_name and not interface_name.startswith('-'):
                        interface_data = {
                            "Interface": interface_name,
                            "Admin": parts[2] if len(parts) > 2 else "",
                            "Operational": parts[3] if len(parts) > 3 else "",
                            "IPv4_Address": parts[4] if len(parts) > 4 else "",
                            "IPv6_Address": parts[5] if len(parts) > 5 else "",
                            "VLAN": parts[6] if len(parts) > 6 else "",
                            "MTU": parts[7] if len(parts) > 7 else "",
                            "Network_Service": parts[8] if len(parts) > 8 else "",
                            "Bundle_Id": parts[9] if len(parts) > 9 else ""
                        }
                        return interface_data
        except Exception as e:
            # Silently continue on parse errors
            pass
        return None
    
    def get_all_interfaces_batch(self):
        """Get all interfaces using optimized batch command"""
        try:
            print(f"[{self.hostname}] 📡 Fetching all interfaces in batch mode...")
            
            # Use the correct command that works on this device
            command = "show interfaces | monitor interval 5"
            
            # Use shell method like original script since exec_command doesn't work
            shell = self.ssh_client.invoke_shell()
            time.sleep(2)
            
            # Clear initial output
            if shell.recv_ready():
                shell.recv(4096)
            
            # Send command (encode to bytes)
            shell.send((command + '\n').encode('utf-8'))
            print(f"[{self.hostname}] ⚡ Command sent: {command}")
            
            # Collect data for longer period to get all interfaces
            collection_time = 300  # 5 minutes to collect all interfaces (proven to work)
            start_time = time.time()
            all_output = []
            
            print(f"[{self.hostname}] ⏱️ Collecting for {collection_time} seconds to capture all interfaces...")
            
            interfaces_found = 0
            parse_errors = 0
            last_report_time = start_time
            
            while time.time() - start_time < collection_time:
                if shell.recv_ready():
                    chunk = shell.recv(4096).decode('utf-8', errors='ignore')
                    lines = chunk.split('\n')
                    
                    for line in lines:
                        if line.strip():
                            interface_data = self.parse_interface_row(line)
                            if interface_data:
                                interface_name = interface_data["Interface"]
                                # Only count as new if we haven't seen this interface before
                                if interface_name not in self.interfaces:
                                    interfaces_found += 1
                                    if interfaces_found % 500 == 0:  # Report every 500 interfaces
                                        elapsed = time.time() - start_time
                                        rate = interfaces_found / elapsed if elapsed > 0 else 0
                                        remaining_time = (collection_time - elapsed)
                                        print(f"[{self.hostname}] 📊 {interfaces_found} unique interfaces collected ({rate:.1f}/sec, {remaining_time:.0f}s remaining)")
                                self.interfaces[interface_name] = interface_data
                            elif '|' in line and line.strip().startswith('|'):
                                parse_errors += 1
                
                # Progress report every 60 seconds for multiple devices
                current_time = time.time()
                if current_time - last_report_time >= 60:
                    elapsed = current_time - start_time
                    print(f"[{self.hostname}] ⏰ Progress: {elapsed:.0f}s elapsed, {len(self.interfaces)} total interfaces in memory")
                    last_report_time = current_time
                
                time.sleep(0.1)  # Small delay to prevent overwhelming CPU
            
            shell.close()
            
            print(f"[{self.hostname}] ✅ Batch collection complete!")
            print(f"[{self.hostname}] 📈 Found {interfaces_found} unique interfaces")
            print(f"[{self.hostname}] 🔄 Total interfaces in memory: {len(self.interfaces)}")
            print(f"[{self.hostname}] ⚠️ Parse errors: {parse_errors} lines")
            
            return len(self.interfaces) > 0
            
        except Exception as e:
            print(f"[{self.hostname}] ❌ Batch collection error: {str(e)}")
            return False
    
    def get_interface_summary(self):
        """Get a quick interface count to verify completeness"""
        try:
            command = "show interfaces summary"
            stdin, stdout, stderr = self.ssh_client.exec_command(command, timeout=60)
            output = stdout.read().decode('utf-8', errors='ignore')
            
            # Look for total interface count in summary
            for line in output.split('\n'):
                if 'total' in line.lower() and 'interface' in line.lower():
                    print(f"[{self.hostname}] 📋 Summary: {line.strip()}")
                    
        except Exception as e:
            print(f"[{self.hostname}] ⚠️ Could not get interface summary: {str(e)}")
    
    def save_database(self):
        """Save interface database to JSON file with enhanced reporting"""
        # Save to data/interfaces directory
        interfaces_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "interfaces")
        os.makedirs(interfaces_dir, exist_ok=True)
        filename = os.path.join(interfaces_dir, f"{self.hostname}_interfaces_info.json")
        
        # Convert interfaces dict to list format
        interfaces_list = []
        for interface_name, interface_data in self.interfaces.items():
            interface_entry = {
                "interface": interface_data["Interface"],
                "admin": interface_data["Admin"].lower(),
                "operational": interface_data["Operational"].lower(),
                "ipv4_address": interface_data["IPv4_Address"],
                "ipv6_address": interface_data["IPv6_Address"],
                "vlan": interface_data["VLAN"],
                "mtu": interface_data["MTU"],
                "network_service": interface_data["Network_Service"],
                "bundle_id": interface_data["Bundle_Id"]
            }
            interfaces_list.append(interface_entry)
        
        database = {
            "metadata": {
                "device_hostname": self.hostname,
                "device_ip": self.ip_address,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_interfaces": len(self.interfaces),
                "collection_method": "batch_optimized"
            },
            "interfaces": interfaces_list
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(database, f, indent=2)
            
            # Enhanced reporting
            current_count = len(self.interfaces)
            if current_count != self.last_interface_count:
                print(f"[{self.hostname}] 🔄 Interface count changed: {self.last_interface_count} → {current_count}")
                self.last_interface_count = current_count
            
            print(f"[{self.hostname}] 💾 Database updated: {current_count} interfaces")
            
            # Admin state summary
            enabled_count = sum(1 for data in self.interfaces.values() if data['Admin'].lower() == 'enabled')
            disabled_count = current_count - enabled_count
            print(f"[{self.hostname}] 📊 Admin states: {enabled_count} enabled, {disabled_count} disabled")
            
            # Operational state summary
            up_count = sum(1 for data in self.interfaces.values() if data['Operational'].lower() == 'up')
            down_count = current_count - up_count
            print(f"[{self.hostname}] 🔌 Operational: {up_count} up, {down_count} down")
            
            # Interface type analysis
            interface_types = {}
            for interface_name in self.interfaces.keys():
                # Extract interface type (prefix before numbers)
                match = re.match(r'^([a-zA-Z]+)', interface_name)
                if match:
                    iface_type = match.group(1)
                    interface_types[iface_type] = interface_types.get(iface_type, 0) + 1
            
            print(f"[{self.hostname}] 🏷️ Interface types:")
            for iface_type, count in sorted(interface_types.items()):
                print(f"[{self.hostname}]    {iface_type}: {count}")
            
            # File size info
            file_size = os.path.getsize(filename)
            print(f"[{self.hostname}] 📁 Database file: {file_size:,} bytes")
            
            print()
            
        except Exception as e:
            print(f"[{self.hostname}] ❌ Error saving database: {str(e)}")
    
    def monitor_interfaces_optimized(self):
        """Optimized interface monitoring for large interface counts"""
        try:
            if not self.ssh_client:
                print(f"[{self.hostname}] ❌ No SSH connection available")
                return
            
            print(f"[{self.hostname}] 🚀 Starting optimized interface collection...")
            self.is_running = True
            
            # Get interface summary first
            self.get_interface_summary()
            
            # Collect all interfaces in batch mode
            success = self.get_all_interfaces_batch()
            
            if success and self.interfaces:
                print(f"[{self.hostname}] ✅ Collection successful!")
                self.save_database()
            else:
                print(f"[{self.hostname}] ❌ Collection failed or no interfaces found")
            
            print(f"[{self.hostname}] ✅ Optimized monitoring completed")
            
        except KeyboardInterrupt:
            print(f"[{self.hostname}] 🛑 Stopped by user")
        except Exception as e:
            print(f"[{self.hostname}] ❌ Monitoring error: {str(e)}")
        finally:
            self.is_running = False
    
    def stop(self):
        """Stop monitoring"""
        self.is_running = False
        if self.ssh_client:
            self.ssh_client.close()


class OptimizedInterfaceMonitorManager:
    """Manages optimized interface monitoring for multiple devices"""
    
    def __init__(self):
        self.monitors = []
        self.active_monitors = []
    
    def load_devices(self):
        """Load device configurations"""
        config_files = [
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "config", "devices_config.json"),
            "../data/config/devices_config.json",
            "data/config/devices_config.json",
            "devices_config.json"
        ]
        
        config_path = None
        for path in config_files:
            if os.path.exists(path):
                config_path = path
                break
        
        if not config_path:
            print("❌ devices_config.json not found")
            print("   Searched in:")
            for path in config_files:
                print(f"     - {path}")
            return False
        
        print(f"📁 Using config file: {config_path}")
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        devices = config.get('devices', [])
        print(f"📋 Loaded {len(devices)} devices from config")
        
        for device_config in devices:
            monitor = OptimizedDeviceInterfaceMonitor(device_config)
            self.monitors.append(monitor)
        
        return True
    
    def connect_all(self):
        """Connect to all devices"""
        print("🔄 Connecting to all devices...")
        
        for monitor in self.monitors:
            if monitor.connect():
                self.active_monitors.append(monitor)
        
        print(f"✅ Connected to {len(self.active_monitors)}/{len(self.monitors)} devices")
        return len(self.active_monitors) > 0
    
    def start_monitoring(self):
        """Start optimized monitoring for all devices"""
        if not self.active_monitors:
            print("❌ No devices connected")
            return
        
        print(f"\n🚀 Starting OPTIMIZED interface monitoring on {len(self.active_monitors)} devices")
        print("⚡ Using batch collection method for better performance")
        print("📊 Enhanced parsing for all interface types")
        print("🔄 Improved progress reporting for large datasets")
        print("⚠️ Press Ctrl+C to stop all monitoring")
        print("=" * 70)
        
        # Start monitoring threads
        threads = []
        for monitor in self.active_monitors:
            thread = threading.Thread(target=monitor.monitor_interfaces_optimized, daemon=True)
            thread.start()
            threads.append((thread, monitor))
            print(f"🟢 Started optimized monitoring {monitor.hostname}")
        
        try:
            # Wait for threads
            for thread, monitor in threads:
                thread.join()
        except KeyboardInterrupt:
            print("\n🛑 Stopping all monitoring...")
            for _, monitor in threads:
                monitor.stop()
        
        print("✅ All monitoring stopped")
        
        # Show final database files
        print("\n📊 Final Interface Database Files:")
        for monitor in self.active_monitors:
            interfaces_dir = os.path.join("data", "interfaces")
            filename = os.path.join(interfaces_dir, f"{monitor.hostname}_interfaces_info.json")
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                interface_count = len(monitor.interfaces) if monitor.interfaces else 0
                print(f"✅ {monitor.hostname}_interfaces_info.json ({file_size:,} bytes, {interface_count} interfaces)")
            else:
                print(f"❌ {monitor.hostname}_interfaces_info.json (not created)")
    
    def run(self):
        """Run the optimized interface monitor"""
        print("🚀 OPTIMIZED Interface Monitor and Database Updater")
        print("=" * 60)
        print("⚡ Enhanced for devices with large interface counts (10k+)")
        print("📡 Uses batch collection instead of streaming")
        print("🔄 Improved parsing and progress reporting")
        print()
        
        if not self.load_devices():
            return
        
        if not self.connect_all():
            return
        
        self.start_monitoring()


def main():
    """Main function"""
    try:
        manager = OptimizedInterfaceMonitorManager()
        manager.run()
    except KeyboardInterrupt:
        print("\n⚠️ Program stopped by user")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main() 