#!/usr/bin/env python3
"""
Interface Monitor and Database Updater
Connects to devices, monitors interfaces, and updates JSON database files
Automatically syncs database with real device interface information
"""

import json
import paramiko
import threading
import time
import sys
import os
import re
from datetime import datetime


class DeviceInterfaceMonitor:
    """Monitor interfaces on a device and update database"""
    
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
        """Parse interface table row from device output - ENHANCED for all interface types"""
        try:
            # Look for lines that start with | and contain interface data
            if line.strip().startswith('| ') and not line.strip().startswith('| Interface'):
                # Split by | and clean up fields
                parts = [part.strip() for part in line.split('|')]
                
                # Check if this looks like an interface line (has at least interface name)
                if len(parts) >= 10 and parts[1]:  # Interface name should not be empty
                    interface_name = parts[1]
                    
                    # OPTIMIZATION: Accept ANY interface name format, not just ge100-*
                    # This captures bundle, lo, irb, enabled, and other interface types
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
        except:
            pass
        return None

    def enhanced_multiline_parser(self, all_lines):
        """Enhanced parser for devices with multi-line interface entries (like WDY1B77800019)"""
        interfaces = {}
        current_interface = None
        current_data = None
        
        for line in all_lines:
            line = line.strip()
            if not line or line.startswith('| Interface') or '----' in line:
                continue
                
            if line.startswith('| '):
                parts = [part.strip() for part in line.split('|')]
                parts = [p for p in parts if p]  # Remove empty parts
                
                if len(parts) >= 1 and parts[0]:
                    # Check if this looks like an interface name
                    interface_name = parts[0]
                    if (interface_name.startswith('ge') or interface_name.startswith('lo') or 
                        interface_name.startswith('bundle') or interface_name.startswith('irb') or
                        interface_name == 'enabled'):
                        
                        # Save previous interface if complete AND VALID
                        if current_interface and current_data and self._is_valid_interface(current_data):
                            interfaces[current_interface] = current_data
                        
                        # Start new interface
                        current_interface = interface_name
                        current_data = {
                            "Interface": interface_name,
                            "Admin": parts[1] if len(parts) > 1 else "",
                            "Operational": parts[2] if len(parts) > 2 else "",
                            "IPv4_Address": parts[3] if len(parts) > 3 else "",
                            "IPv6_Address": parts[4] if len(parts) > 4 else "",
                            "VLAN": parts[5] if len(parts) > 5 else "",
                            "MTU": parts[6] if len(parts) > 6 else "",
                            "Network_Service": parts[7] if len(parts) > 7 else "",
                            "Bundle_Id": parts[8] if len(parts) > 8 else ""
                        }
                    elif current_data and len(parts) >= 1:
                        # This might be a continuation line - try to fill missing fields
                        if not current_data["Admin"] and len(parts) > 0:
                            current_data["Admin"] = parts[0]
                        if not current_data["Operational"] and len(parts) > 1:
                            current_data["Operational"] = parts[1]
                        if not current_data["IPv4_Address"] and len(parts) > 2:
                            current_data["IPv4_Address"] = parts[2]
                        if not current_data["IPv6_Address"] and len(parts) > 3:
                            current_data["IPv6_Address"] = parts[3]
                        if not current_data["VLAN"] and len(parts) > 4:
                            current_data["VLAN"] = parts[4]
                        if not current_data["MTU"] and len(parts) > 5:
                            current_data["MTU"] = parts[5]
                        if not current_data["Network_Service"] and len(parts) > 6:
                            current_data["Network_Service"] = parts[6]
                        if not current_data["Bundle_Id"] and len(parts) > 7:
                            current_data["Bundle_Id"] = parts[7]
        
        # Save last interface ONLY if valid
        if current_interface and current_data and self._is_valid_interface(current_data):
            interfaces[current_interface] = current_data
        
        return interfaces

    def _is_valid_interface(self, interface_data):
        """Validate that an interface entry is complete and not a parsing fragment"""
        interface_name = interface_data.get("Interface", "")
        
        # Filter out ONLY the most obvious parsing fragments (too strict before)
        if interface_name in ["ge", "ge100-", "ge100-0/0/"]:
            return False
        
        # Keep these potentially valid interfaces that were filtered before:
        # - "ge10" could be a valid interface name
        # - "ge100-0/" might be a valid interface path
        # - Subinterfaces like "ge100-0/0/38.665"
        # - Physical interfaces like "ge100-0/0/14"
        
        # Accept any interface name that looks legitimate
        if re.match(r'^[a-zA-Z]+[\w\-\/\.]*$', interface_name) and len(interface_name) >= 2:
            return True
        
        return False
    
    def save_database(self):
        """Save interface database to JSON file"""
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
                "collection_method": "enhanced_multiline_parser" if self.hostname in ['WDY1B77800019'] else "extended_optimized_stream"
            },
            "interfaces": interfaces_list
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(database, f, indent=2)
            
            # Check if interface count changed
            current_count = len(self.interfaces)
            if current_count != self.last_interface_count:
                print(f"[{self.hostname}] 🔄 Interface count changed: {self.last_interface_count} → {current_count}")
                self.last_interface_count = current_count
            
            print(f"[{self.hostname}] 💾 Database updated: {current_count} interfaces")
            
            # Show admin state summary
            enabled_count = sum(1 for data in self.interfaces.values() if data['Admin'].lower() == 'enabled')
            disabled_count = current_count - enabled_count
            
            print(f"[{self.hostname}] 📊 Admin states: {enabled_count} enabled, {disabled_count} disabled")
            
            # Show operational state summary
            up_count = sum(1 for data in self.interfaces.values() if data['Operational'].lower() == 'up')
            down_count = current_count - up_count
            
            print(f"[{self.hostname}] 🔌 Operational: {up_count} up, {down_count} down")
            
            # OPTIMIZATION: Interface type analysis - shows what types of interfaces we found
            interface_types = {}
            for interface_name in self.interfaces.keys():
                # Extract interface type (prefix before numbers)
                import re
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
            
            # Check for missing interfaces in expected sequence
            interface_names = sorted(self.interfaces.keys())
            missing_interfaces = []
            
            # Extract slot/port numbers and check for gaps
            slot_ports = []
            for name in interface_names:
                if 'ge100-' in name:
                    try:
                        parts = name.replace('ge100-', '').split('/')
                        slot = int(parts[0])
                        port = int(parts[2])
                        slot_ports.append((slot, port, name))
                    except:
                        pass
            
            slot_ports.sort()
            
            # Check for gaps in each slot
            for slot in [0, 1]:  # Check both slots
                ports_in_slot = [port for s, port, name in slot_ports if s == slot]
                if ports_in_slot:
                    min_port = min(ports_in_slot)
                    max_port = max(ports_in_slot)
                    expected_ports = set(range(min_port, max_port + 1))
                    actual_ports = set(ports_in_slot)
                    missing_ports = expected_ports - actual_ports
                    
                    for port in missing_ports:
                        missing_interface = f"ge100-{slot}/0/{port}"
                        missing_interfaces.append(missing_interface)
            
            if missing_interfaces:
                print(f"[{self.hostname}] ⚠️  {len(missing_interfaces)} ge100 interfaces missing from sequence:")
                for missing in missing_interfaces[:10]:  # Show first 10 only
                    print(f"[{self.hostname}]    - {missing}")
                if len(missing_interfaces) > 10:
                    print(f"[{self.hostname}]    ... and {len(missing_interfaces) - 10} more")
                print(f"[{self.hostname}] 🎯 Expected total ge100: {len(slot_ports) + len(missing_interfaces)} interfaces")
            elif disabled_count > 0:
                print(f"[{self.hostname}] ⚠️  Warning: {disabled_count} interfaces are disabled")
            
            print()
            
        except Exception as e:
            print(f"[{self.hostname}] ❌ Error saving database: {str(e)}")
    
    def monitor_interfaces(self):
        """Monitor interfaces continuously and update database"""
        try:
            # Check if SSH client is available
            if not self.ssh_client:
                print(f"[{self.hostname}] ❌ No SSH connection available")
                return
            
            command = "show interfaces | monitor interval 5"
            print(f"[{self.hostname}] 🔄 Starting interface monitoring...")
            print(f"[{self.hostname}] 📡 Command: {command}")
            
            # Create shell
            shell = self.ssh_client.invoke_shell()
            self.is_running = True
            
            # Wait for shell
            time.sleep(2)
            
            # Clear initial output
            if shell.recv_ready():
                shell.recv(4096)
            
            # Send command (encode to bytes)
            shell.send((command + '\n').encode('utf-8'))
            print(f"[{self.hostname}] ⚡ Monitoring started")
            
            save_counter = 0
            cycle_counter = 0
            interfaces_found = 0
            first_save_done = False
            last_report_time = time.time()
            shell_start_time = time.time()  # Track start time for rate calculation
            
            # OPTIMIZATION: For devices that need multi-line parsing, collect all lines first
            needs_multiline_parsing = self.hostname in ['WDY1B77800019']  # Add other devices as needed
            all_lines = [] if needs_multiline_parsing else None
            
            # Monitor loop
            while self.is_running:
                if shell.recv_ready():
                    chunk = shell.recv(4096).decode('utf-8', errors='ignore')
                    
                    if needs_multiline_parsing:
                        # For multi-line parsing devices, collect all lines first
                        all_lines.extend(chunk.split('\n'))
                    else:
                        # Process each line immediately for other devices
                        for line in chunk.split('\n'):
                            if line.strip():
                                # Try to parse interface data
                                interface_data = self.parse_interface_row(line)
                                if interface_data:
                                    interface_name = interface_data["Interface"]
                                    # Only count as new if we haven't seen this interface before
                                    if interface_name not in self.interfaces:
                                        interfaces_found += 1
                                        # OPTIMIZATION: Better progress reporting every 500 interfaces
                                        if interfaces_found % 500 == 0:
                                            elapsed = time.time() - shell_start_time
                                            rate = interfaces_found / elapsed if elapsed > 0 else 0
                                            print(f"[{self.hostname}] 📊 {interfaces_found} unique interfaces collected ({rate:.1f}/sec)")
                                    self.interfaces[interface_name] = interface_data
                
                # OPTIMIZATION: Extended timing for large interface counts
                # Wait longer before first save to collect all interfaces
                # Then save every 10 seconds after that
                save_counter += 1
                if not first_save_done:
                    # OPTIMIZATION: Wait 300 seconds (5 minutes) for first save to collect through multiple cycles
                    if save_counter >= 3000:  # 3000 * 0.1s = 300 seconds (5 minutes)
                        if needs_multiline_parsing and all_lines:
                            # Use enhanced parser for multi-line devices
                            print(f"[{self.hostname}] 🔧 Using enhanced multi-line parser...")
                            self.interfaces = self.enhanced_multiline_parser(all_lines)
                            print(f"[{self.hostname}] ✅ Enhanced parsing found {len(self.interfaces)} interfaces")
                        
                        if self.interfaces:
                            print(f"[{self.hostname}] 🔄 Extended collection complete, saving database...")
                            self.save_database()
                            first_save_done = True
                        save_counter = 0
                else:
                    # Regular saves every 15 seconds
                    if save_counter >= 150:  # 150 * 0.1s = 15 seconds
                        if self.interfaces:
                            self.save_database()
                        save_counter = 0
                
                # Progress report every 60 seconds during extended collection
                current_time = time.time()
                if not first_save_done and current_time - last_report_time >= 60:
                    elapsed = current_time - shell_start_time
                    if needs_multiline_parsing:
                        print(f"[{self.hostname}] ⏰ Progress: {elapsed:.0f}s elapsed, {len(all_lines)} lines collected")
                    else:
                        print(f"[{self.hostname}] ⏰ Progress: {elapsed:.0f}s elapsed, {len(self.interfaces)} total interfaces in memory")
                    last_report_time = current_time
                
                time.sleep(0.1)
            
            # Final save
            if self.interfaces:
                self.save_database()
            
            shell.close()
            print(f"[{self.hostname}] ✅ Monitoring stopped")
            
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


class InterfaceMonitorManager:
    """Manages interface monitoring for multiple devices"""
    
    def __init__(self):
        self.monitors = []
        self.active_monitors = []
    
    def load_devices(self):
        """Load device configurations"""
        # Look for config file in the correct locations
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
            monitor = DeviceInterfaceMonitor(device_config)
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
        """Start monitoring all devices"""
        if not self.active_monitors:
            print("❌ No devices connected")
            return
        
        print(f"\n🚀 Starting OPTIMIZED interface monitoring on {len(self.active_monitors)} devices")
        print("📊 Using enhanced parser for ALL interface types (ge, bundle, lo, irb, etc.)")
        print("⏱️  Extended 5-minute initial collection period for large interface counts")
        print("💾 Database updates every 15 seconds after initial collection")
        print("🔄 Interface counts will be synced with device reality")
        print("⚠️  Press Ctrl+C to stop all monitoring")
        print("=" * 70)
        
        # Start monitoring threads
        threads = []
        for monitor in self.active_monitors:
            thread = threading.Thread(target=monitor.monitor_interfaces, daemon=True)
            thread.start()
            threads.append((thread, monitor))
            print(f"🟢 Started monitoring {monitor.hostname} → {monitor.hostname}_interfaces_info.json")
        
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
        """Run the interface monitor"""
        print("🚀 Interface Monitor and Database Updater")
        print("=" * 50)
        print("📡 Connects to devices and updates interface database files")
        print("🔄 Automatically syncs with real device interface information")
        print()
        
        if not self.load_devices():
            return
        
        if not self.connect_all():
            return
        
        self.start_monitoring()


def main():
    """Main function"""
    try:
        manager = InterfaceMonitorManager()
        manager.run()
    except KeyboardInterrupt:
        print("\n⚠️ Program stopped by user")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main() 