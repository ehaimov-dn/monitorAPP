#!/usr/bin/env python3
"""
Network Interface Configuration Tool
Automatically configures interfaces on network devices based on JSON data.
Supports enable/disable, speed configuration, and breakout operations.
"""

import json
import os
import sys
import paramiko
import time
import re
import logging
from datetime import datetime
from network_mapper import NetworkMapper


class InterfaceEnabler:
    def __init__(self):
        self.setup_logging()
        self.devices_dir = "/home/dn/Eddie-scripts/monitorAPP/Devices"
        self.credentials = {
            'username': 'dnroot',
            'password': 'dnroot'
        }
        self.connection = None
        self.channel = None
        
    def setup_logging(self):
        """Setup logging for the interface enabler"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        log_filename = f"logs/interface_enabler_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Interface Enabler started")
    
    def get_available_devices(self):
        """Get list of available devices from the Devices directory"""
        if not os.path.exists(self.devices_dir):
            self.logger.error(f"Devices directory not found: {self.devices_dir}")
            return []
        
        devices = []
        for item in os.listdir(self.devices_dir):
            device_path = os.path.join(self.devices_dir, item)
            if os.path.isdir(device_path):
                interfaces_file = os.path.join(device_path, f"{item}_interfaces.json")
                if os.path.exists(interfaces_file):
                    devices.append(item)
        
        return devices
    
    def load_device_interfaces(self, device_name):
        """Load interface data from device JSON file"""
        interfaces_file = os.path.join(self.devices_dir, device_name, f"{device_name}_interfaces.json")
        
        try:
            with open(interfaces_file, 'r') as f:
                data = json.load(f)
            return data.get('interfaces', {})
        except Exception as e:
            self.logger.error(f"Failed to load interfaces for {device_name}: {str(e)}")
            return {}
    
    def get_physical_interfaces(self, interfaces_data):
        """Extract physical interfaces from the data (excluding bundle and logical interfaces)"""
        physical_interfaces = {}
        
        for interface_name, interface_data in interfaces_data.items():
            # Filter out bundle, loopback, and other logical interfaces
            if not any(interface_name.startswith(prefix) for prefix in ['bundle-', 'lo', 'mgmt', 'ctrl-', 'ice']):
                # Check if it's a physical interface (ge, xe, etc.)
                if re.match(r'^(ge|xe|ce)\d+', interface_name):
                    # Skip interfaces that are not present
                    operational_state = interface_data.get('operational_state', '').lower()
                    if operational_state != 'not-present':
                        physical_interfaces[interface_name] = interface_data
        
        return physical_interfaces
    
    def filter_interfaces_for_lldp(self, interfaces, interfaces_data):
        """Filter interfaces for LLDP configuration, excluding not-present interfaces"""
        filtered_interfaces = []
        
        for interface in interfaces:
            if interface in interfaces_data:
                operational_state = interfaces_data[interface].get('operational_state', '').lower()
                if operational_state != 'not-present':
                    filtered_interfaces.append(interface)
                else:
                    self.logger.info(f"Skipping LLDP configuration for {interface} - interface not present")
        
        return filtered_interfaces
    
    def display_device_menu(self):
        """Display device selection menu"""
        devices = self.get_available_devices()
        
        if not devices:
            print("No devices found in the Devices directory.")
            return None
        
        print("\n=== Interface Configuration Tool ===")
        print("Available devices:")
        
        for i, device in enumerate(devices, 1):
            print(f"  {i}. {device}")
        
        while True:
            try:
                choice = input(f"\nSelect device (1-{len(devices)}): ").strip()
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(devices):
                    return devices[choice_num - 1]
                else:
                    print(f"Invalid choice. Please enter 1-{len(devices)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def display_configuration_menu(self):
        """Display configuration options menu"""
        print("\n=== Configuration Options ===")
        print("1. Enable interfaces")
        print("2. Disable interfaces")
        print("3. Configure port speed")
        print("4. Configure breakout")
        print("5. Enable LLDP on interfaces")
        print("6. Disable LLDP on interfaces")
        print("7. Exit")
        
        while True:
            try:
                choice = input("\nSelect configuration type (1-7): ").strip()
                choice_num = int(choice)
                
                if 1 <= choice_num <= 7:
                    return choice_num
                else:
                    print("Invalid choice. Please enter 1-7")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def select_interfaces(self, physical_interfaces, config_type):
        """Allow user to select which interfaces to configure"""
        interface_list = list(physical_interfaces.keys())
        interface_list.sort()
        
        print(f"\n=== Available Physical Interfaces ({len(interface_list)}) ===")
        for i, interface in enumerate(interface_list, 1):
            status = physical_interfaces[interface].get('admin_state', 'unknown')
            oper_status = physical_interfaces[interface].get('operational_state', 'unknown')
            print(f"  {i:2d}. {interface:<15} (Admin: {status}, Oper: {oper_status})")
        
        print("\nSelection options:")
        print("  - Enter interface numbers separated by commas (e.g., 1,3,5-8)")
        print("  - Enter 'all' to select all interfaces")
        print("  - Enter 'range' for range selection (e.g., 1-10)")
        
        while True:
            selection = input("\nSelect interfaces: ").strip()
            
            if selection.lower() == 'all':
                return interface_list
            
            try:
                selected_interfaces = []
                parts = selection.split(',')
                
                for part in parts:
                    part = part.strip()
                    if '-' in part:
                        # Handle range
                        start, end = map(int, part.split('-'))
                        for i in range(start, end + 1):
                            if 1 <= i <= len(interface_list):
                                selected_interfaces.append(interface_list[i - 1])
                    else:
                        # Handle single number
                        i = int(part)
                        if 1 <= i <= len(interface_list):
                            selected_interfaces.append(interface_list[i - 1])
                
                if selected_interfaces:
                    return list(set(selected_interfaces))  # Remove duplicates
                else:
                    print("No valid interfaces selected. Please try again.")
                    
            except ValueError:
                print("Invalid input format. Please try again.")
    
    def get_speed_configuration(self):
        """Get speed configuration from user"""
        print("\n=== Port Speed Configuration ===")
        print("Available speeds:")
        print("  1. 1G")
        print("  2. 10G")
        print("  3. 25G")
        print("  4. 100G")
        print("  5. 400G")
        
        speed_map = {1: 1, 2: 10, 3: 25, 4: 100, 5: 400}
        
        while True:
            try:
                choice = input("Select speed (1-5): ").strip()
                choice_num = int(choice)
                
                if 1 <= choice_num <= 5:
                    return speed_map[choice_num]
                else:
                    print("Invalid choice. Please enter 1-5")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def get_breakout_configuration(self):
        """Get breakout configuration from user"""
        print("\n=== Breakout Configuration ===")
        print("Available breakout modes:")
        print("  1. 10g-4x (Break 100G into 4x10G)")
        print("  2. 100g-4x (Break 400G into 4x100G)")
        print("  3. 200g-2x (Break 400G into 2x200G)")
        print("  4. 100g-2x (Break 400G into 2x100G)")
        print("  5. 400g-2x (Break 800G into 2x400G)")
        print("  6. none (Remove breakout)")
        
        breakout_map = {
            1: "10g-4x",
            2: "100g-4x", 
            3: "200g-2x",
            4: "100g-2x",
            5: "400g-2x",
            6: "none"
        }
        
        while True:
            try:
                choice = input("Select breakout mode (1-6): ").strip()
                choice_num = int(choice)
                
                if 1 <= choice_num <= 6:
                    return breakout_map[choice_num]
                else:
                    print("Invalid choice. Please enter 1-6")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def generate_bulk_configuration(self, interfaces, config_type, config_value=None):
        """Generate bulk configuration commands"""
        commands = []
        
        if config_type in [5, 6]:  # LLDP configuration
            # LLDP commands don't need interface mode
            commands.append("configure")
            
            for interface in interfaces:
                if config_type == 5:  # Enable LLDP
                    commands.append(f"protocols lldp interface {interface} ^")
                elif config_type == 6:  # Disable LLDP
                    commands.append(f"no protocols lldp interface {interface} ^")
        else:
            # Regular interface configuration
            commands.append("configure")
            commands.append("interfaces")
            
            # Generate interface-specific commands
            for interface in interfaces:
                if config_type == 1:  # Enable
                    commands.append(f"{interface} admin-state enabled")
                elif config_type == 2:  # Disable
                    commands.append(f"{interface} admin-state disabled")
                elif config_type == 3:  # Speed
                    commands.append(f"{interface} speed {config_value}")
                elif config_type == 4:  # Breakout
                    if config_value == "none":
                        commands.append(f"{interface} no breakout")
                    else:
                        commands.append(f"{interface} breakout {config_value}")
        
        # Return to global configuration level instead of exiting
        commands.append("top")
        
        return commands
    
    def generate_breakout_configuration_with_validation(self, interfaces, config_value, device_name):
        """Generate breakout configuration with proper validation and preparation"""
        commands = []
        
        # Enter configuration mode
        commands.append("configure")
        
        # For each interface, prepare for breakout
        for interface in interfaces:
            self.logger.info(f"Preparing breakout configuration for {interface}")
            
            # Step 1: Remove all configurations from the interface
            commands.append(f"no interfaces {interface}")
            
            # Step 2: Remove LLDP if configured (this will be checked during execution)
            commands.append(f"no protocols lldp interface {interface} ^")
        
        # Now configure breakout for all interfaces
        for interface in interfaces:
            if config_value == "none":
                commands.append(f"interfaces {interface} no breakout")
            else:
                commands.append(f"interfaces {interface} breakout {config_value}")
        
        # Return to global configuration level
        commands.append("top")
        
        return commands
    
    def connect_to_device(self, device_name):
        """Connect to the network device via SSH"""
        # Try to get hostname from system information
        system_file = os.path.join(self.devices_dir, device_name, f"{device_name}_System_Information.json")
        hostname = None
        
        try:
            with open(system_file, 'r') as f:
                system_data = json.load(f)
                # Try to get hostname from login_credentials first, then fallback to other fields
                login_creds = system_data.get('login_credentials', {})
                hostname = (login_creds.get('hostname') or 
                           system_data.get('management_ip') or 
                           system_data.get('hostname', device_name))
        except Exception as e:
            self.logger.warning(f"Could not read system info file: {e}")
            hostname = device_name
        
        try:
            self.logger.info(f"Connecting to {hostname}")
            
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            self.connection.connect(
                hostname=hostname,
                username=self.credentials['username'],
                password=self.credentials['password'],
                timeout=30,
                look_for_keys=False,
                allow_agent=False
            )
            
            self.channel = self.connection.invoke_shell()
            time.sleep(2)
            
            # Clear initial output
            if self.channel.recv_ready():
                self.channel.recv(4096)
            
            self.logger.info("Successfully connected to device")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to connect to {hostname}: {str(e)}")
            return False
    
    def execute_commands(self, commands):
        """Execute bulk configuration commands as a single paste operation"""
        if not self.connection or not self.channel:
            self.logger.error("No active connection to device")
            return False
        
        try:
            # Clear any pending data
            if self.channel.recv_ready():
                self.channel.recv(4096)
            
            # Create bulk configuration string
            bulk_config = '\n'.join(commands)
            
            self.logger.info("Executing bulk configuration:")
            self.logger.info(f"Bulk config:\n{bulk_config}")
            
            # Send entire bulk configuration at once
            self.channel.send(bulk_config + '\n')
            
            # Wait longer for bulk operation to complete
            time.sleep(5)
            
            # Collect output
            output = ""
            max_wait = 120  # Increased timeout for bulk operations
            start_time = time.time()
            last_data_time = time.time()
            
            while time.time() - start_time < max_wait:
                if self.channel.recv_ready():
                    chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                    output += chunk
                    last_data_time = time.time()
                    
                    # Check for command completion (looking for prompt in recent output)
                    recent_lines = output.split('\n')[-5:]
                    for line in recent_lines:
                        line = line.strip()
                        # Look for prompt patterns that indicate completion
                        if line and any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                            # Also check for username@hostname patterns or device prompts
                            if '@' in line or 'cfg' in line or line.endswith('#'):
                                self.logger.info("Bulk configuration completed")
                                return output
                else:
                    # If no data for a while, check if command might be complete
                    if time.time() - last_data_time > 10:  # 10 seconds without data
                        self.logger.info("No data received for 10 seconds, assuming completion")
                        break
                    time.sleep(0.5)
            
            self.logger.info("Bulk configuration execution completed")
            return output
            
        except Exception as e:
            self.logger.error(f"Failed to execute bulk commands: {str(e)}")
            return False
    
    def commit_configuration(self):
        """Commit the configuration changes and wait for success confirmation"""
        try:
            self.logger.info("Committing configuration")
            
            # Clear any pending data
            if self.channel.recv_ready():
                self.channel.recv(4096)
            
            # Send commit command
            self.channel.send('commit\n')
            time.sleep(2)
            
            # Collect commit output and wait for success message
            output = ""
            max_wait = 120  # Commit can take longer, especially for bulk operations
            start_time = time.time()
            commit_succeeded = False
            confirmation_sent = False
            
            while time.time() - start_time < max_wait:
                if self.channel.recv_ready():
                    chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                    output += chunk
                    
                    # Check if device is asking for confirmation
                    if ("would you like to commit them" in output.lower() or 
                        "yes/no/cancel" in output.lower()) and not confirmation_sent:
                        self.logger.info("Device asking for commit confirmation - sending 'yes'")
                        self.channel.send('yes\n')
                        confirmation_sent = True
                        time.sleep(2)
                        continue
                    
                    # Check for commit success message
                    if "Commit succeeded by dnroot" in output:
                        commit_succeeded = True
                        self.logger.info("Commit succeeded - confirmed by device")
                        break
                    
                    # Check for commit failure messages
                    if any(failure_msg in output.lower() for failure_msg in 
                           ['commit failed', 'error', 'invalid', 'failed']):
                        self.logger.error(f"Commit failed - device reported error: {output}")
                        return False
                        
                else:
                    time.sleep(0.5)
            
            if commit_succeeded:
                self.logger.info("Configuration committed successfully")
                return output
            else:
                self.logger.error("Commit timeout - did not receive success confirmation")
                self.logger.error(f"Commit output received: {output}")
                return False
            
        except Exception as e:
            self.logger.error(f"Failed to commit configuration: {str(e)}")
            return False
    
    def check_lldp_on_interface(self, interface_name):
        """Check if LLDP is configured on a specific interface"""
        if not self.connection or not self.channel:
            self.logger.error("No active connection to device")
            return False
        
        try:
            self.logger.info(f"Checking LLDP configuration on {interface_name}")
            
            # Clear any pending data
            if self.channel.recv_ready():
                self.channel.recv(4096)
            
            # Send command to check LLDP on specific interface
            command = f"show lldp neighbors {interface_name}"
            self.channel.send(command + '\n')
            time.sleep(2)
            
            # Collect output
            output = ""
            max_wait = 30
            start_time = time.time()
            
            while time.time() - start_time < max_wait:
                if self.channel.recv_ready():
                    chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                    output += chunk
                    
                    # Check for prompt
                    if any(line.strip().endswith(p) for line in output.split('\n')[-3:] 
                           for p in ['>', '#', '$', '% ']):
                        break
                else:
                    time.sleep(0.1)
            
            # Check if LLDP is configured (has neighbors or is enabled)
            # If output contains "No LLDP neighbors" or similar, LLDP might still be enabled
            # If output contains error about LLDP not being configured, then it's not configured
            lldp_configured = not any(error in output.lower() for error in 
                                    ['not configured', 'disabled', 'error', 'invalid'])
            
            self.logger.info(f"LLDP check result for {interface_name}: {'configured' if lldp_configured else 'not configured'}")
            return lldp_configured
            
        except Exception as e:
            self.logger.error(f"Failed to check LLDP on {interface_name}: {str(e)}")
            return False
    
    def disconnect(self):
        """Disconnect from the device"""
        try:
            if self.channel:
                self.channel.close()
            if self.connection:
                self.connection.close()
            self.logger.info("Disconnected from device")
        except:
            pass
    
    def validate_configuration(self, device_name):
        """Validate configuration by running network_mapper on the device"""
        print("\n=== Validating Configuration ===")
        print("Running network_mapper to update device information...")
        
        try:
            # Import and create NetworkMapper instance
            from network_mapper import NetworkMapper
            mapper = NetworkMapper()
            
            # Set the device_name attribute that the mapper needs for saving files
            mapper.device_name = device_name
            
            self.logger.info(f"Starting network_mapper validation for {device_name}")
            print(f"Connecting to {device_name} to update interface and LLDP information...")
            
            # Run the monitoring mode which will update all device information
            if mapper.run_monitoring_mode(device_name):
                print("✅ Connected to device for validation")
                print("✅ Retrieved updated interface information")
                print("✅ Retrieved detailed interface information")
                print("✅ Retrieved updated LLDP information")
                print("✅ Saved and uploaded device configuration")
                print("✅ Device data updated successfully")
                print(f"✅ Updated JSON files in: Devices/{device_name}/")
                return True
            else:
                print("❌ Failed to update device information")
                return False
            
        except Exception as e:
            self.logger.error(f"Validation failed: {str(e)}")
            print(f"❌ Validation error: {str(e)}")
            return False
    
    def run(self):
        """Main execution flow"""
        try:
            # Step 1: Choose device
            print("=== Step 1: Device Selection ===")
            device_name = self.display_device_menu()
            if not device_name:
                return
            
            print(f"\nSelected device: {device_name}")
            
            # Load device interfaces
            interfaces_data = self.load_device_interfaces(device_name)
            if not interfaces_data:
                print("Failed to load device interface data.")
                return
            
            physical_interfaces = self.get_physical_interfaces(interfaces_data)
            print(f"Found {len(physical_interfaces)} physical interfaces")
            
            # Step 2: Choose configuration type
            print("\n=== Step 2: Configuration Type ===")
            config_type = self.display_configuration_menu()
            if config_type == 7:  # Exit
                return
            
            config_names = {1: "Enable", 2: "Disable", 3: "Port Speed", 4: "Breakout", 5: "Enable LLDP", 6: "Disable LLDP"}
            print(f"\nSelected configuration: {config_names[config_type]}")
            
            # Step 3: Select interfaces
            print(f"\n=== Step 3: Interface Selection ===")
            selected_interfaces = self.select_interfaces(physical_interfaces, config_type)
            print(f"\nSelected {len(selected_interfaces)} interfaces:")
            for interface in selected_interfaces:
                print(f"  - {interface}")
            
            # Step 4: Get additional configuration if needed
            config_value = None
            if config_type == 3:  # Speed configuration
                config_value = self.get_speed_configuration()
                print(f"Selected speed: {config_value}G")
            elif config_type == 4:  # Breakout configuration
                config_value = self.get_breakout_configuration()
                print(f"Selected breakout: {config_value}")
            
            # Step 5: Generate bulk configuration
            print(f"\n=== Step 4: Generate Configuration ===")
            
            # Use special breakout configuration method if breakout is selected
            if config_type == 4:  # Breakout configuration
                commands = self.generate_breakout_configuration_with_validation(selected_interfaces, config_value, device_name)
                print("Generated breakout configuration commands (with validation):")
            elif config_type in [5, 6]:  # LLDP configuration
                # Filter out not-present interfaces for LLDP
                filtered_interfaces = self.filter_interfaces_for_lldp(selected_interfaces, interfaces_data)
                if len(filtered_interfaces) != len(selected_interfaces):
                    skipped_count = len(selected_interfaces) - len(filtered_interfaces)
                    print(f"⚠️  Skipped {skipped_count} not-present interfaces for LLDP configuration")
                
                commands = self.generate_bulk_configuration(filtered_interfaces, config_type, config_value)
                lldp_action = "Enable" if config_type == 5 else "Disable"
                print(f"Generated LLDP {lldp_action} configuration commands:")
            else:
                commands = self.generate_bulk_configuration(selected_interfaces, config_type, config_value)
                print("Generated configuration commands:")
            
            for command in commands:
                print(f"  {command}")
            
            # Confirm before applying
            confirm = input("\nApply this configuration? (yes/no): ").strip().lower()
            if confirm not in ['yes', 'y']:
                print("Configuration cancelled.")
                return
            
            # Step 6: Connect and apply configuration
            print(f"\n=== Step 5: Apply Configuration ===")
            if not self.connect_to_device(device_name):
                print("Failed to connect to device.")
                return
            
            # Execute commands
            output = self.execute_commands(commands)
            if output:
                print("Commands executed successfully.")
                
                # Step 7: Commit configuration
                print(f"\n=== Step 6: Commit Configuration ===")
                commit_output = self.commit_configuration()
                if commit_output:
                    print("✅ Configuration committed successfully!")
                    print("✅ Device confirmed: 'Commit succeeded by dnroot'")
                    
                    # Step 8: Validate configuration
                    print(f"\n=== Step 7: Validation ===")
                    if self.validate_configuration(device_name):
                        print("\n🎉 Configuration and validation completed successfully!")
                        print("📊 Device JSON files have been updated with current interface states.")
                    else:
                        print("\n⚠️  Configuration was committed but validation failed.")
                        print("💡 You may need to manually run network_mapper to update the JSON files.")
                    
                else:
                    print("❌ Failed to commit configuration.")
                    print("❌ Device did not confirm successful commit.")
                    print("⚠️  Configuration may not be applied to the device.")
                    return
            else:
                print("Failed to execute commands.")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            print(f"An error occurred: {str(e)}")
        finally:
            self.disconnect()


def main():
    """Main entry point"""
    enabler = InterfaceEnabler()
    enabler.run()


if __name__ == "__main__":
    main()
