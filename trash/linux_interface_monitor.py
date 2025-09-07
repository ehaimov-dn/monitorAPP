#!/usr/bin/env python3
"""
Interactive Interface Monitor
Connects to device, enters inband namespace, discovers real interfaces, and monitors interface state changes
"""

import paramiko
import time
import os
import sys
from datetime import datetime
import signal
import json
import glob
import re


def load_available_devices():
    """Load available devices from JSON files"""
    devices = {}
    
    # Look for interface JSON files
    json_files = glob.glob("data/interfaces/*_interfaces_info.json")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            device_name = data['metadata']['device_hostname']
            device_ip = data['metadata']['device_ip']
            
            # We'll discover actual interfaces after connecting to the device
            devices[device_name] = {
                'ip': device_ip,
                'json_file': json_file
            }
                
        except Exception as e:
            print(f"Warning: Could not load {json_file}: {e}")
    
    return devices


def interactive_device_selection():
    """Interactive device selection only (interface selection happens after connecting)"""
    print("=" * 60)
    print("🐧 Linux Interface Monitor - Device Selection")
    print("=" * 60)
    
    # Load available devices
    devices = load_available_devices()
    
    if not devices:
        print("❌ No devices found in data/interfaces/")
        print("   Make sure interface monitoring has been run to generate JSON files")
        return None
    
    # Display available devices
    print("\n📋 Available Devices:")
    device_list = list(devices.keys())
    for i, device_name in enumerate(device_list, 1):
        device = devices[device_name]
        print(f"  {i}. {device_name} ({device['ip']})")
    
    # Get device selection
    while True:
        try:
            choice = input(f"\n🎯 Select device (1-{len(device_list)}): ").strip()
            device_index = int(choice) - 1
            if 0 <= device_index < len(device_list):
                selected_device = device_list[device_index]
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(device_list)}")
        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n🛑 Selection cancelled")
            return None
    
    print(f"\n✅ Selected device: {selected_device}")
    return selected_device


class LinuxInterfaceMonitor:
    """Monitor Linux interface state changes on device"""
    
    def __init__(self, device_name=None, interface_name=None, disable_internal_logging=False):
        # If interactive mode, get device selection
        if device_name is None:
            device_name = interactive_device_selection()
            if device_name is None:
                print("❌ No device selected. Exiting.")
                sys.exit(1)
        
        # Load device configuration
        self.device_name = device_name
        self.ip_address = self.get_device_ip(device_name)
        self.hostname = device_name.lower()
        self.username = "dnroot"
        self.password = "dnroot"
        
        # SSH connection
        self.ssh_client = None
        self.shell = None
        self.is_running = False
        
        # Interface monitoring
        self.interface = interface_name  # Set from parameter if provided
        self.last_state = None
        
        # Logging setup
        self.disable_internal_logging = disable_internal_logging
        
        if not self.disable_internal_logging:
            # Only create internal log file if not disabled
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.log_file = f"logs/linux_interface_monitor_{self.hostname}_{timestamp}.log"
            
            # Ensure logs directory exists
            os.makedirs("logs", exist_ok=True)
        else:
            self.log_file = None
        
        # Setup signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def get_device_ip(self, device_name):
        """Get device IP from devices config or interface JSON"""
        # Try to get IP from devices_config.json
        config_files = [
            "data/config/devices_config.json",
            "devices_config.json"
        ]
        
        for config_file in config_files:
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r') as f:
                        config = json.load(f)
                    
                    for device in config.get('devices', []):
                        if device['hostname'] == device_name:
                            return device['ip_address']
                except:
                    pass
        
        # Try to get IP from interface JSON files
        json_files = glob.glob("data/interfaces/*_interfaces_info.json")
        for json_file in json_files:
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                if data['metadata']['device_hostname'] == device_name:
                    return data['metadata']['device_ip']
            except:
                pass
        
        # Fallback to device name
        return device_name.lower()
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.log_message("🛑 Received shutdown signal, cleaning up...")
        self.is_running = False
        self.cleanup()
        sys.exit(0)
    
    def log_message(self, message: str, level: str = "INFO"):
        """Log message to file and console"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {level} - {message}"
        
        # Log to file
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(log_entry + '\n')
                f.flush()  # Force file write immediately
        
        # Print to console (handle broken pipe gracefully)
        try:
            print(log_entry)
            sys.stdout.flush()  # Force immediate console output
        except BrokenPipeError:
            # Pipe was broken (likely due to output redirection), silently continue
            pass
    
    def connect(self):
        """Connect to device via SSH"""
        try:
            self.log_message(f"🔗 Connecting to {self.device_name} ({self.ip_address})")
            
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Try IP address first
            try:
                self.ssh_client.connect(
                    hostname=self.ip_address,
                    username=self.username,
                    password=self.password,
                    timeout=30
                )
                self.log_message(f"✅ Connected via IP: {self.ip_address}")
                return True
                
            except Exception as ip_error:
                self.log_message(f"❌ IP connection failed: {ip_error}")
                
                # Try hostname as fallback
                try:
                    self.ssh_client.connect(
                        hostname=self.hostname,
                        username=self.username,
                        password=self.password,
                        timeout=30
                    )
                    self.log_message(f"✅ Connected via hostname: {self.hostname}")
                    return True
                    
                except Exception as hostname_error:
                    self.log_message(f"❌ Hostname connection failed: {hostname_error}")
                    return False
            
        except Exception as e:
            self.log_message(f"❌ Failed to connect: {str(e)}")
            return False
    
    def enter_inband_namespace(self):
        """Enter the inband namespace and verify we're in the correct namespace"""
        try:
            self.log_message("🐧 Setting up inband namespace access...")
            
            # Create interactive shell
            if self.ssh_client:
                self.shell = self.ssh_client.invoke_shell()
                self.shell.settimeout(10)
                time.sleep(2)
            
            # Clear initial output
            if self.shell and self.shell.recv_ready():
                initial_output = self.shell.recv(4096).decode('utf-8', errors='ignore')
                self.log_message(f"📝 Initial output: {initial_output.strip()}")
            
            # Send command to enter inband engine shell
            if self.shell:
                shell_command = "run start shell ncc 0 container inband-engine"
                self.log_message(f"📤 Command: {shell_command}")
                self.shell.send(shell_command.encode() + b"\n")
                time.sleep(3)
                
                # Send password
                self.log_message(f"📤 Sending password: {self.password}")
                self.shell.send(self.password.encode() + b"\n")
                time.sleep(3)
            
            # Check response
            if self.shell and self.shell.recv_ready():
                response = self.shell.recv(4096).decode('utf-8', errors='ignore')
                self.log_message(f"📝 Shell response: {response.strip()}")
            
            # Enter inband namespace
            if self.shell:
                namespace_command = "ip netns exec inband_ns bash"
                self.log_message(f"📤 Command: {namespace_command}")
                self.shell.send(namespace_command.encode() + b"\n")
                time.sleep(3)
            
            # Verify we're in the inband namespace
            if self.shell and self.shell.recv_ready():
                namespace_response = self.shell.recv(4096).decode('utf-8', errors='ignore')
                self.log_message(f"📝 Namespace response: {namespace_response.strip()}")
                
                # Check for [inband_ns] in the prompt
                if '[inband_ns]' in namespace_response:
                    self.log_message("✅ Successfully entered inband namespace - found [inband_ns] prompt")
                    return True
                else:
                    self.log_message("⚠️  [inband_ns] prompt not found, but continuing...")
            
            # Send a test command to verify namespace
            if self.shell:
                self.shell.send(b"echo 'namespace test'\n")
                time.sleep(1)
                
                if self.shell.recv_ready():
                    test_response = self.shell.recv(4096).decode('utf-8', errors='ignore')
                    if '[inband_ns]' in test_response:
                        self.log_message("✅ Confirmed inband namespace access")
                        return True
            
            self.log_message("✅ Namespace access established")
            return True
            
        except Exception as e:
            self.log_message(f"❌ Error setting up namespace: {str(e)}")
            return False
    
    def discover_interfaces(self):
        """Discover interfaces using simple ip -brief link show with hex to network translation"""
        try:
            self.log_message("🔍 Discovering available interfaces using ip -brief link show...")
            
            if not self.shell:
                return []
            
            # Send simple command to list interfaces
            command = "ip -brief link show"
            self.log_message(f"📤 Command: {command}")
            self.shell.send(command.encode() + b"\n")
            time.sleep(2)  # Give time for command execution
            
            # Read response
            full_response = ""
            max_attempts = 5
            
            for attempt in range(max_attempts):
                if self.shell.recv_ready():
                    chunk = self.shell.recv(4096).decode('utf-8', errors='ignore')
                    full_response += chunk
                    time.sleep(0.5)
                else:
                    break
            
            self.log_message(f"📝 Interface discovery response:")
            self.log_message(f"--- START RESPONSE ---")
            self.log_message(full_response)
            self.log_message(f"--- END RESPONSE ---")
            
            # Parse interfaces from response
            interfaces = []
            lines = full_response.split('\n')
            
            for line in lines:
                line = line.strip()
                # Skip empty lines, command echoes, and prompts
                if (not line or 
                    line.startswith('ip -brief') or
                    'root@' in line or
                    line.startswith('#') or
                    line.startswith('$') or
                    '[inband_ns]' in line):
                    continue
                
                # Parse interface line - format: "interface_name STATE flags..."
                parts = line.split()
                if len(parts) >= 2:
                    interface_name = parts[0].strip()
                    state = parts[1].strip()
                    
                    # Filter for Linux ethernet interfaces only (e00000, e00001, etc.)
                    if (interface_name and 
                        interface_name.startswith('e') and 
                        len(interface_name) >= 6 and  # e00000 is 6 chars
                        interface_name not in ['lo'] and  # No loopback
                        not interface_name.startswith(('br', 'virbr', 'docker', 'vnet', 'veth')) and
                        '@' not in interface_name):  # No tunnel interfaces
                        
                        # Translate Linux hex interface name to network interface name
                        network_interface = self.translate_interface_name(interface_name)
                        
                        self.log_message(f"🔍 Found interface: {interface_name} → {network_interface} ({state})")
                        
                        interfaces.append({
                            'name': interface_name,
                            'network_name': network_interface,
                            'state': state,
                            'raw_line': line
                        })
            
            self.log_message(f"🔍 Total interfaces found: {len(interfaces)} physical interfaces")
            
            if interfaces:
                # Sort interfaces by hexadecimal interface names
                def sort_interface_key(iface):
                    name = iface['name']
                    # Extract hexadecimal part from interface names like e00001, e0001f
                    if name.startswith('e') and len(name) > 1:
                        try:
                            hex_part = name[1:]  # Remove 'e' prefix
                            return int(hex_part, 16)  # Convert hex to int for proper sorting
                        except ValueError:
                            return float('inf')  # Put non-hex names at the end
                    return float('inf')  # Put non-standard names at the end
                
                # Sort interfaces
                sorted_interfaces = sorted(interfaces, key=sort_interface_key)
                
                self.log_message("📋 Physical interfaces (sorted with translation):")
                for iface in sorted_interfaces:
                    self.log_message(f"   • {iface['name']} → {iface['network_name']} ({iface['state']})")
                
                return sorted_interfaces
            else:
                self.log_message("❌ No physical interfaces found!")
            
            return interfaces
            
        except Exception as e:
            self.log_message(f"❌ Error discovering interfaces: {str(e)}")
            return []
    
    def translate_interface_name(self, linux_interface):
        """Translate Linux hex interface name to network interface name"""
        try:
            # Extract hex number from interface name (e.g., e00001 → 00001)
            if linux_interface.startswith('e') and len(linux_interface) > 1:
                hex_part = linux_interface[1:]  # Remove 'e' prefix
                interface_number = int(hex_part, 16)  # Convert hex to decimal
                
                # Translate to network interface format: ge100-0/0/X
                network_interface = f"ge100-0/0/{interface_number}"
                return network_interface
            else:
                # If it doesn't match expected pattern, return as-is
                return linux_interface
                
        except Exception as e:
            self.log_message(f"⚠️  Warning: Could not translate interface {linux_interface}: {e}")
            return linux_interface
    
    def select_interface(self, interfaces):
        """Let user select interface to monitor"""
        if not interfaces:
            self.log_message("❌ No interfaces available for monitoring")
            return None
        
        # Sort interfaces by hexadecimal interface names for display
        def sort_interface_key(iface):
            name = iface['name']
            # Extract hexadecimal part from interface names like e00001, e0001f
            if name.startswith('e') and len(name) > 1:
                try:
                    hex_part = name[1:]  # Remove 'e' prefix
                    return int(hex_part, 16)  # Convert hex to int for proper sorting
                except ValueError:
                    return float('inf')  # Put non-hex names at the end
            return float('inf')  # Put non-standard names at the end
        
        # Sort interfaces for display
        sorted_interfaces = sorted(interfaces, key=sort_interface_key)
        
        print("\n" + "=" * 60)
        print("🔍 Available Physical Interfaces (sorted with network translation):")
        print("=" * 60)
        
        for i, iface in enumerate(sorted_interfaces, 1):
            linux_name = iface['name']
            network_name = iface['network_name']
            state = iface['state']
            print(f"  {i}. {linux_name} → {network_name} ({state})")
        
        # Get interface selection
        while True:
            try:
                choice = input(f"\n🎯 Select interface to monitor (1-{len(sorted_interfaces)}): ").strip()
                interface_index = int(choice) - 1
                if 0 <= interface_index < len(sorted_interfaces):
                    selected_interface = sorted_interfaces[interface_index]['name']
                    selected_network = sorted_interfaces[interface_index]['network_name']
                    break
                else:
                    print(f"❌ Please enter a number between 1 and {len(sorted_interfaces)}")
            except ValueError:
                print("❌ Please enter a valid number")
            except KeyboardInterrupt:
                print("\n🛑 Selection cancelled")
                return None
        
        print(f"\n✅ Selected interface: {selected_interface} → {selected_network}")
        return selected_interface
    
    def monitor_interface(self):
        """Monitor interface state changes by polling every second"""
        if not self.interface:
            self.log_message("❌ No interface selected for monitoring")
            return
        
        self.log_message(f"🔍 Starting continuous state monitoring for interface: {self.interface}")
        self.log_message(f"📊 Logging interface state every 1 second")
        self.log_message(f"📁 Log file: {self.log_file}")
        self.log_message("🛑 Press Ctrl+C to stop monitoring")
        
        self.is_running = True
        check_count = 0
        
        while self.is_running:
            try:
                check_count += 1
                
                # Send command to check interface state
                if self.shell:
                    command = f"ip -brief link show {self.interface}"
                    self.shell.send(command.encode() + b"\n")
                    time.sleep(0.5)
                    
                    # Read response
                    if self.shell.recv_ready():
                        response = self.shell.recv(4096).decode('utf-8', errors='ignore')
                        
                        # Clean ANSI escape sequences
                        import re
                        clean_response = re.sub(r'\x1b\[[0-9;]*[mK]', '', response)
                        clean_response = re.sub(r'\x1b\[\?[0-9]*[lh]', '', clean_response)
                        clean_response = clean_response.replace('\r', '')
                        
                        # Parse response for interface state
                        for line in clean_response.split('\n'):
                            line = line.strip()
                            # Look for the actual interface status line (starts with interface name)
                            if line.startswith(self.interface + ' ') or line.startswith(self.interface + '\t'):
                                parts = line.split()
                                if len(parts) >= 2:
                                    interface_name = parts[0]
                                    current_state = parts[1]
                                    
                                    # Generate timestamp for current check
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                                    
                                    # Log current state every second (continuous monitoring)
                                    state_log_entry = f"[{timestamp}] {interface_name} {current_state}"
                                    self.log_message(state_log_entry)
                                    
                                    # Also log to a separate continuous state file
                                    if self.log_file:
                                        continuous_log_file = self.log_file.replace('.log', '_continuous.log')
                                        with open(continuous_log_file, 'a') as f:
                                            f.write(f"{state_log_entry}\n")
                                            f.flush()  # Force immediate write
                                    
                                    # Additionally, log state changes with special notation
                                    if current_state != self.last_state:
                                        # Log state changes with clean output
                                        state_message = f"{interface_name} → {current_state}"
                                        self.log_message(f"📊 Interface State Change: {state_message}")
                                        self.last_state = current_state
                                        
                                        # Also log to a separate state changes file
                                        if self.log_file:
                                            changes_log_file = self.log_file.replace('.log', '_changes.log')
                                            with open(changes_log_file, 'a') as f:
                                                f.write(f"{timestamp} {interface_name} CHANGED_TO {current_state}\n")
                                                f.flush()  # Force immediate write
                                    
                                    break  # Found the interface line, stop parsing
                
                # Log monitoring status every 60 checks (1 minute)
                if check_count % 60 == 0:
                    self.log_message(f"🔄 Monitoring active - {check_count} checks completed, current state: {self.last_state or 'UNKNOWN'}")
                
                # Wait 1 second before next check
                time.sleep(1)
                
            except Exception as e:
                self.log_message(f"❌ Error during monitoring: {str(e)}")
                time.sleep(1)
        
        self.log_message(f"🔍 Interface monitoring stopped after {check_count} checks")
        if self.log_file:
            self.log_message(f"📁 Continuous state log saved to: {self.log_file.replace('.log', '_continuous.log')}")
            self.log_message(f"📁 State changes log saved to: {self.log_file.replace('.log', '_changes.log')}")
    
    def cleanup(self):
        """Clean up SSH connection"""
        try:
            if self.shell:
                self.shell.close()
            if self.ssh_client:
                self.ssh_client.close()
            self.log_message("🔌 SSH connection closed")
        except Exception as e:
            self.log_message(f"❌ Error during cleanup: {str(e)}")
    
    def run(self):
        """Main run method"""
        self.log_message("🚀 Starting Linux Interface Monitor")
        self.log_message(f"🎯 Target Device: {self.device_name} ({self.ip_address})")
        if self.interface:
            self.log_message(f"🎯 Target Interface: {self.interface}")
        self.log_message("=" * 60)
        
        try:
            # Connect to device
            if not self.connect():
                self.log_message("❌ Failed to connect to device")
                return False
            
            # Enter inband namespace
            if not self.enter_inband_namespace():
                self.log_message("❌ Failed to enter inband namespace")
                return False
            
            # Discover available interfaces
            interfaces = self.discover_interfaces()
            if not interfaces:
                self.log_message("❌ No interfaces found")
                return False
            
            # Select interface to monitor
            if self.interface:
                # Validate that the provided interface exists
                interface_names = [iface['name'] for iface in interfaces]
                if self.interface not in interface_names:
                    self.log_message(f"❌ Interface '{self.interface}' not found on device")
                    self.log_message(f"Available interfaces: {', '.join(interface_names)}")
                    return False
                
                # Find the network interface translation for logging
                network_interface = None
                for iface in interfaces:
                    if iface['name'] == self.interface:
                        network_interface = iface['network_name']
                        break
                
                if network_interface:
                    self.log_message(f"✅ Using provided interface: {self.interface} → {network_interface}")
                else:
                    self.log_message(f"✅ Using provided interface: {self.interface}")
            else:
                # Interactive selection
                self.interface = self.select_interface(interfaces)
                if not self.interface:
                    self.log_message("❌ No interface selected")
                    return False
            
            # Start monitoring
            self.monitor_interface()
            
            return True
            
        except Exception as e:
            self.log_message(f"❌ Monitor error: {str(e)}")
            return False
        finally:
            self.cleanup()


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Linux Interface Monitor with Real Device Discovery')
    parser.add_argument('--device', type=str, help='Device name (skips interactive selection)')
    parser.add_argument('--interface', type=str, help='Interface name to monitor (skips interactive selection)')
    parser.add_argument('--config-mode', action='store_true', help='Run in configuration mode and save selections to temp file')
    parser.add_argument('--no-internal-logging', action='store_true', help='Disable internal logging (for use with external log redirection)')
    
    args = parser.parse_args()
    
    # Special configuration mode
    if args.config_mode:
        # For config mode, we need to connect and discover interfaces
        monitor = LinuxInterfaceMonitor(args.device, args.interface, args.no_internal_logging)
        
        try:
            # Connect and discover interfaces
            if not monitor.connect():
                try:
                    print("❌ Failed to connect to device")
                except BrokenPipeError:
                    pass
                return
            
            if not monitor.enter_inband_namespace():
                try:
                    print("❌ Failed to enter inband namespace")
                except BrokenPipeError:
                    pass
                return
            
            interfaces = monitor.discover_interfaces()
            if not interfaces:
                try:
                    print("❌ No interfaces found")
                except BrokenPipeError:
                    pass
                return
            
            selected_interface = monitor.select_interface(interfaces)
            if selected_interface:
                # Save selections to temporary file
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', prefix='monitor_config_', suffix='.tmp', delete=False) as f:
                    f.write(f"DEVICE={monitor.device_name}\n")
                    f.write(f"INTERFACE={selected_interface}\n")
                    try:
                        print(f"CONFIG_FILE={f.name}")
                    except BrokenPipeError:
                        pass
        finally:
            monitor.cleanup()
        
        return
    
    try:
        print("🚀 Linux Interface Monitor with Real Device Discovery")
        print("=" * 60)
    except BrokenPipeError:
        pass
    
    monitor = LinuxInterfaceMonitor(args.device, args.interface, args.no_internal_logging)
    
    try:
        monitor.run()
    except KeyboardInterrupt:
        try:
            print("\n🛑 Interrupted by user")
        except BrokenPipeError:
            pass
    except Exception as e:
        try:
            print(f"❌ Unexpected error: {str(e)}")
        except BrokenPipeError:
            pass
    finally:
        try:
            print("👋 Monitor finished")
        except BrokenPipeError:
            pass


if __name__ == "__main__":
    main() 