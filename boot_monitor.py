#!/usr/bin/env python3
"""
Boot Monitor Script for DNOS Devices
Automatically performs restart testing with automatic "Yes" confirmation
"""

import paramiko
import json
import logging
import time
import re
import sys
import os
from datetime import datetime, timedelta
import signal

class BootMonitor:
    def __init__(self):
        self.setup_logging()
        self.setup_directories()
        self.device_info = {}
        self.connection = None
        self.channel = None
        self.restart_results = {
            'warm': [],
            'cold': []
        }
        self.running = True
        self.current_cycle = 0
        self.total_cycles = 0
        self.restart_type = ""
        self.device_name = ""
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.logger.info(f"Received signal {signum}. Shutting down gracefully...")
        self.running = False
        if self.connection:
            try:
                self.connection.close()
            except:
                pass
        sys.exit(0)
        
    def setup_logging(self):
        """Setup comprehensive logging system"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"logs/boot_monitor_{timestamp}.log"
        
        logging.basicConfig(
            level=logging.DEBUG,  # Enable debug logging to see what's happening
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Boot Monitor initialized")
        
    def setup_directories(self):
        """Create necessary directories for monitoring and logs"""
        directories = ['logs', 'monitor', 'monitor/core_files']
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                
    def get_available_devices(self):
        """Get list of available devices from Devices directory"""
        devices_dir = "Devices"
        if not os.path.exists(devices_dir):
            self.logger.error("Devices directory not found!")
            return []
            
        devices = []
        for item in os.listdir(devices_dir):
            device_path = os.path.join(devices_dir, item)
            if os.path.isdir(device_path):
                sys_info_file = os.path.join(device_path, f"{item}_System_Information.json")
                if os.path.exists(sys_info_file):
                    devices.append(item)
                    
        return sorted(devices)
    
    def load_device_info(self, device_name):
        """Load device information from JSON file"""
        sys_info_file = f"Devices/{device_name}/{device_name}_System_Information.json"
        
        try:
            with open(sys_info_file, 'r') as f:
                device_data = json.load(f)
                
            self.device_info = {
                'name': device_name,
                'hostname': device_data['login_credentials']['hostname'],
                'username': device_data['login_credentials']['username'],
                'password': device_data['login_credentials']['password']
            }
            
            self.logger.info(f"Loaded device info for {device_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load device info for {device_name}: {e}")
            return False
    
    def connect_to_device(self, timeout=30):
        """Establish SSH connection to device"""
        try:
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            self.connection.connect(
                hostname=self.device_info['hostname'],
                username=self.device_info['username'],
                password=self.device_info['password'],
                timeout=timeout,
                allow_agent=False,
                look_for_keys=False
            )
            
            self.channel = self.connection.invoke_shell()
            time.sleep(2)
            
            # Clear any initial output
            if self.channel.recv_ready():
                self.channel.recv(4096)
                
            self.logger.info(f"Connected to device {self.device_info['name']}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to connect to device: {e}")
            if self.connection:
                try:
                    self.connection.close()
                except:
                    pass
                self.connection = None
                self.channel = None
            return False
    
    def send_command(self, command, timeout=30):
        """Send command to device and return output"""
        if not self.channel:
            return None
            
        try:
            self.channel.send(command + '\n')
            time.sleep(1)
            
            output = ""
            start_time = time.time()
            
            while time.time() - start_time < timeout:
                if self.channel.recv_ready():
                    chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                    output += chunk
                    
                    if re.search(r'[#>]\s*$', output):
                        break
                        
                time.sleep(0.1)
                
            return output
            
        except Exception as e:
            self.logger.error(f"Failed to send command '{command}': {e}")
            return None
    
    def check_system_status(self):
        """Check if system is fully operational"""
        try:
            output = self.send_command("show system")
            if not output:
                return False
                
            if "System status: running" in output and ("active-up" in output or "up" in output):
                self.logger.info("System status check passed")
                return True
                    
            self.logger.warning("System status check failed")
            return False
            
        except Exception as e:
            self.logger.error(f"Failed to check system status: {e}")
            return False
    
    def perform_restart(self, restart_type):
        """Perform system restart using EXACT method from successful test"""
        try:
            if restart_type == "warm":
                command = "request system restart warm"
            else:
                command = "request system restart"
                
            self.logger.info(f"Initiating {restart_type} restart...")
            self.logger.info(f"Using EXACT method from successful test")
            
            # DON'T use send_command method - use direct channel send like successful test
            
            # Clear any existing output (like in successful test)
            if self.channel.recv_ready():
                old_output = self.channel.recv(4096).decode('utf-8', errors='ignore')
                self.logger.debug(f"Cleared existing output: {repr(old_output)}")
            
            # Send restart command - EXACT same as successful test
            self.logger.info(f"Sending restart command: {command}")
            self.channel.send(command + '\n')
            time.sleep(3)  # EXACT same timing as successful test
            
            # Handle confirmation - EXACT same approach as successful test
            output = ""
            if self.channel.recv_ready():
                output = self.channel.recv(4096).decode('utf-8', errors='ignore')
                self.logger.info(f"Restart prompt: {repr(output)}")
            
            if "Warning:" in output and "restart" in output and "(yes/no)" in output:
                self.logger.info("✅ Got restart confirmation prompt!")
                self.logger.info("Automatically answering 'yes'...")
                
                # Send yes confirmation - EXACT same as successful test
                self.channel.send('yes\n')
                time.sleep(3)  # EXACT same timing
                
                self.logger.info("✅ Restart command confirmed!")
                self.logger.info("Device should now be restarting...")
                
                # Try to read any final output - EXACT same as test
                try:
                    if self.channel.recv_ready():
                        final = self.channel.recv(4096).decode('utf-8', errors='ignore')
                        self.logger.info(f"Final output: {repr(final)}")
                except:
                    self.logger.info("Connection lost (expected during restart)")
                
                return True
            else:
                self.logger.error(f"❌ No restart confirmation prompt received")
                self.logger.error(f"Output was: {repr(output)}")
                return False
            
        except Exception as e:
            self.logger.error(f"Failed to perform {restart_type} restart: {e}")
            return False
    
    def wait_for_device_recovery(self, max_wait_time=600):
        """Wait for device to come back online after restart - test every 5 seconds"""
        self.logger.info("Waiting for device to recover...")
        start_time = time.time()
        
        # Close existing connection
        if self.connection:
            try:
                self.connection.close()
            except:
                pass
            self.connection = None
            self.channel = None
        
        # Wait a bit before trying to reconnect
        self.logger.info("Waiting 30 seconds before first reconnection attempt...")
        time.sleep(30)
        
        attempt = 1
        while time.time() - start_time < max_wait_time and self.running:
            try:
                elapsed = time.time() - start_time
                self.logger.info(f"Recovery attempt #{attempt} (elapsed: {elapsed:.0f}s)...")
                
                if self.connect_to_device(timeout=10):
                    if self.check_system_status():
                        recovery_time = time.time() - start_time
                        self.logger.info(f"✅ Device recovered in {recovery_time:.2f} seconds")
                        return recovery_time
                    else:
                        self.logger.info("Device connected but not fully operational yet")
                        
                # Close connection before next attempt
                if self.connection:
                    try:
                        self.connection.close()
                    except:
                        pass
                    self.connection = None
                    self.channel = None
                    
            except Exception as e:
                self.logger.debug(f"Recovery attempt #{attempt} failed: {e}")
                
            # Wait 5 seconds before next attempt as requested
            self.logger.info("Waiting 5 seconds before next attempt...")
            time.sleep(5)
            attempt += 1
            
        self.logger.error("Device failed to recover within timeout period")
        return None
    
    def get_device_date(self):
        """Get current date from device"""
        try:
            output = self.send_command("show system uptime")
            if output:
                match = re.search(r'Current Time: ([^\r\n]+)', output)
                if match:
                    time_str = match.group(1).strip()
                    try:
                        date_part = time_str.split()[0]
                        return datetime.strptime(date_part, '%d-%b-%Y').date()
                    except:
                        pass
                        
            return datetime.now().date()
            
        except Exception as e:
            self.logger.error(f"Failed to get device date: {e}")
            return datetime.now().date()
    
    def collect_core_files(self, device_date, restart_cycle):
        """Collect core files generated during restart cycle"""
        try:
            self.logger.info("Checking for core files...")
            
            output = self.send_command("show file all core list")
            if not output:
                self.logger.info("No core files found")
                return
                
            core_files = []
            lines = output.split('\n')
            
            for line in lines:
                line = line.strip()
                if '|' in line and ('NCC' in line or 'NCP' in line or 'NCF' in line or 'NCM' in line):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 5:
                        try:
                            node_type = parts[1]
                            node_id = parts[2]
                            filename = parts[3]
                            size = parts[4]
                            timestamp_str = parts[5] if len(parts) > 5 else ""
                            
                            if timestamp_str:
                                try:
                                    core_time = datetime.strptime(timestamp_str, '%d-%b-%Y %H:%M:%S %Z')
                                    time_diff = datetime.now() - core_time
                                    
                                    if time_diff <= timedelta(hours=3):
                                        core_files.append({
                                            'node_type': node_type,
                                            'node_id': node_id,
                                            'filename': filename,
                                            'size': size,
                                            'timestamp': timestamp_str,
                                            'restart_cycle': restart_cycle
                                        })
                                except:
                                    core_files.append({
                                        'node_type': node_type,
                                        'node_id': node_id,
                                        'filename': filename,
                                        'size': size,
                                        'timestamp': timestamp_str,
                                        'restart_cycle': restart_cycle
                                    })
                        except Exception as e:
                            self.logger.debug(f"Failed to parse core file line: {line}")
                            continue
            
            if core_files:
                core_folder = f"monitor/core_files/{self.device_name}-core_files_restartcycle_{restart_cycle}"
                os.makedirs(core_folder, exist_ok=True)
                
                core_info_file = os.path.join(core_folder, "core_files_info.json")
                
                existing_cores = []
                if os.path.exists(core_info_file):
                    try:
                        with open(core_info_file, 'r') as f:
                            existing_cores = json.load(f)
                    except:
                        existing_cores = []
                
                new_cores = []
                for core in core_files:
                    is_duplicate = False
                    for existing in existing_cores:
                        if (core['filename'] == existing['filename'] and 
                            core['timestamp'] == existing['timestamp']):
                            is_duplicate = True
                            break
                    if not is_duplicate:
                        new_cores.append(core)
                
                if new_cores:
                    all_cores = existing_cores + new_cores
                    with open(core_info_file, 'w') as f:
                        json.dump(all_cores, f, indent=2)
                    
                    self.logger.info(f"Found {len(new_cores)} new core files for restart cycle {restart_cycle}")
                    
                    for core in new_cores:
                        self.logger.info(f"Core file: {core['filename']} ({core['size']}) - {core['timestamp']}")
                else:
                    self.logger.info("No new core files found")
            else:
                self.logger.info("No core files found in the last 3 hours")
                
        except Exception as e:
            self.logger.error(f"Failed to collect core files: {e}")
    
    def save_restart_results(self, restart_type):
        """Save restart monitoring results to file"""
        try:
            results_file = f"monitor/{self.device_name}_{restart_type}_restart_results.json"
            
            with open(results_file, 'w') as f:
                json.dump(self.restart_results[restart_type], f, indent=2)
                
            self.logger.info(f"Saved {restart_type} restart results to {results_file}")
            
        except Exception as e:
            self.logger.error(f"Failed to save restart results: {e}")
    
    def run_restart_cycle(self, restart_type, cycle_num):
        """Run a single restart cycle"""
        self.logger.info(f"Starting {restart_type} restart cycle {cycle_num}/{self.total_cycles}")
        
        restart_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Perform restart (automatically confirms with "Yes")
        if not self.perform_restart(restart_type):
            self.logger.error(f"Failed to initiate {restart_type} restart for cycle {cycle_num}")
            
            cycle_result = {
                'cycle': cycle_num,
                'restart_time': restart_timestamp,
                'operational_time': 'FAILED',
                'total_time': 'FAILED',
                'status': 'FAILED'
            }
            self.restart_results[restart_type].append(cycle_result)
            return False
        
        # Wait for device recovery
        recovery_time = self.wait_for_device_recovery()
        
        if recovery_time is None:
            self.logger.error(f"Device failed to recover for {restart_type} restart cycle {cycle_num}")
            
            cycle_result = {
                'cycle': cycle_num,
                'restart_time': restart_timestamp,
                'operational_time': 'FAILED',
                'total_time': 'FAILED',
                'status': 'FAILED'
            }
        else:
            operational_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cycle_result = {
                'cycle': cycle_num,
                'restart_time': restart_timestamp,
                'operational_time': operational_timestamp,
                'total_time': f"{recovery_time:.2f} seconds",
                'status': 'SUCCESS'
            }
            
            self.logger.info(f"Cycle {cycle_num} completed successfully in {recovery_time:.2f} seconds")
        
        self.restart_results[restart_type].append(cycle_result)
        self.save_restart_results(restart_type)
        
        # Collect core files after measurements are complete
        if recovery_time is not None:
            try:
                device_date = self.get_device_date()
                self.collect_core_files(device_date, f"{restart_type}_{cycle_num}")
            except Exception as e:
                self.logger.error(f"Failed to collect core files: {e}")
        
        return recovery_time is not None
    
    def run_monitoring(self, restart_type, num_cycles, device_name):
        """Main monitoring loop"""
        self.device_name = device_name
        self.restart_type = restart_type
        self.total_cycles = num_cycles
        
        self.logger.info(f"Starting boot monitoring for device {device_name}")
        self.logger.info(f"Restart type: {restart_type}, Cycles: {num_cycles}")
        
        if not self.load_device_info(device_name):
            return False
        
        if not self.connect_to_device():
            self.logger.error("Failed to establish initial connection to device")
            return False
        
        try:
            restart_types = []
            if restart_type == "both":
                restart_types = ["warm", "cold"]
            else:
                restart_types = [restart_type]
            
            for rtype in restart_types:
                if not self.running:
                    break
                    
                self.logger.info(f"Starting {rtype} restart cycles")
                
                for cycle in range(1, num_cycles + 1):
                    if not self.running:
                        break
                        
                    self.current_cycle = cycle
                    
                    # Ensure we're connected before starting cycle (skip system status check to avoid channel interference)
                    if not self.connection:
                        self.logger.info("Re-establishing connection before restart cycle")
                        if not self.connect_to_device():
                            self.logger.error(f"Failed to connect for {rtype} restart cycle {cycle}")
                            continue
                    else:
                        self.logger.info("Connection available, proceeding with restart")
                    
                    success = self.run_restart_cycle(rtype, cycle)
                    
                    if not success:
                        self.logger.error(f"Cycle {cycle} failed, continuing with next cycle")
                    
                    if cycle < num_cycles and self.running:
                        self.logger.info("Waiting 30 seconds before next cycle...")
                        time.sleep(30)
                
                self.logger.info(f"Completed all {rtype} restart cycles")
            
            self.print_summary()
            
        except Exception as e:
            self.logger.error(f"Error during monitoring: {e}")
            return False
        finally:
            if self.connection:
                try:
                    self.connection.close()
                except:
                    pass
        
        self.logger.info("Boot monitoring completed")
        return True
    
    def print_summary(self):
        """Print summary of all restart cycles"""
        self.logger.info("\n" + "="*60)
        self.logger.info("BOOT MONITORING SUMMARY")
        self.logger.info("="*60)
        
        for rtype in ['warm', 'cold']:
            if self.restart_results[rtype]:
                self.logger.info(f"\n{rtype.upper()} RESTART RESULTS:")
                self.logger.info("-" * 40)
                
                successful_cycles = 0
                total_time = 0
                
                for result in self.restart_results[rtype]:
                    status_msg = f"Restart #{result['cycle']} - "
                    status_msg += f"Started: {result['restart_time']} - "
                    
                    if result['status'] == 'SUCCESS':
                        status_msg += f"Operational: {result['operational_time']} - "
                        status_msg += f"Total Time: {result['total_time']}"
                        successful_cycles += 1
                        
                        try:
                            time_val = float(result['total_time'].split()[0])
                            total_time += time_val
                        except:
                            pass
                    else:
                        status_msg += "FAILED"
                    
                    self.logger.info(status_msg)
                
                if successful_cycles > 0:
                    avg_time = total_time / successful_cycles
                    success_rate = (successful_cycles / len(self.restart_results[rtype])) * 100
                    
                    self.logger.info(f"\nStatistics for {rtype} restarts:")
                    self.logger.info(f"Success Rate: {success_rate:.1f}% ({successful_cycles}/{len(self.restart_results[rtype])})")
                    self.logger.info(f"Average Recovery Time: {avg_time:.2f} seconds")
        
        self.logger.info("\n" + "="*60)

def main():
    """Main function with user interaction"""
    monitor = BootMonitor()
    
    try:
        print("\n" + "="*50)
        print("DNOS BOOT MONITOR")
        print("="*50)
        
        devices = monitor.get_available_devices()
        
        if not devices:
            print("No devices found in Devices directory!")
            return
        
        print("\nAvailable devices:")
        for i, device in enumerate(devices, 1):
            print(f"{i}. {device}")
        
        while True:
            try:
                device_choice = input(f"\nSelect device (1-{len(devices)}): ").strip()
                device_idx = int(device_choice) - 1
                
                if 0 <= device_idx < len(devices):
                    selected_device = devices[device_idx]
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        print("\nRestart types:")
        print("1. Warm restart")
        print("2. Cold restart") 
        print("3. Both (warm and cold)")
        
        while True:
            restart_choice = input("\nSelect restart type (1-3): ").strip()
            
            if restart_choice == "1":
                restart_type = "warm"
                break
            elif restart_choice == "2":
                restart_type = "cold"
                break
            elif restart_choice == "3":
                restart_type = "both"
                break
            else:
                print("Invalid selection. Please try again.")
        
        while True:
            try:
                num_cycles = int(input("\nNumber of restart cycles: ").strip())
                if num_cycles > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
        
        print(f"\nConfiguration:")
        print(f"Device: {selected_device}")
        print(f"Restart type: {restart_type}")
        print(f"Number of cycles: {num_cycles}")
        
        if restart_type == "both":
            print(f"Total restarts: {num_cycles * 2} ({num_cycles} warm + {num_cycles} cold)")
        
        print("\n⚠️  IMPORTANT: Restarts will be performed automatically!")
        print("The script will automatically answer 'Yes' to all restart confirmations.")
        
        confirm = input("\nProceed with monitoring? (y/n): ").strip().lower()
        
        if confirm != 'y':
            print("Monitoring cancelled.")
            return
        
        print(f"\nStarting boot monitoring...")
        print("Press Ctrl+C to stop monitoring gracefully")
        
        success = monitor.run_monitoring(restart_type, num_cycles, selected_device)
        
        if success:
            print("\nBoot monitoring completed successfully!")
        else:
            print("\nBoot monitoring completed with errors. Check logs for details.")
    
    except KeyboardInterrupt:
        print("\n\nMonitoring interrupted by user.")
    except Exception as e:
        print(f"\nError: {e}")
        monitor.logger.error(f"Main function error: {e}")

if __name__ == "__main__":
    main()
