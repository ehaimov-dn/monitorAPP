# Network Monitoring and Interface Configuration Toolkit

## 📋 Overview

This toolkit provides comprehensive network device monitoring and interface configuration capabilities for DNOS/DriveNets devices. It consists of two main tools that work independently or together:

- **`network_mapper.py`** - Complete device discovery, monitoring, and data collection
- **`interface_enabler.py`** - Advanced interface configuration with bulk operations

## 🏗️ Project Structure

```
/home/dn/Eddie-scripts/monitorAPP/
├── network_mapper.py              # Main monitoring and discovery tool
├── interface_enabler.py           # Interface configuration tool
├── Devices/                       # Device data storage (excluded from git)
│   └── [device_name]/             # Each device gets its own folder
│       ├── [device]_System_Information.json
│       ├── [device]_interfaces.json
│       ├── [device]_interfaces_detail.json
│       ├── [device]_LLDP_Connections.json
│       └── [device]_config
├── dnos_cli/                      # Complete DNOS CLI documentation
├── logs/                          # Execution logs (excluded from git)
└── .gitignore                     # Git exclusions for security
```

---

# 📡 Network Mapper (`network_mapper.py`)

## 🎯 Purpose
Comprehensive network device discovery, monitoring, and data collection tool that provides complete device documentation and automatic backup capabilities.

## 🚀 How to Run

### Basic Execution
```bash
cd /home/dn/Eddie-scripts/monitorAPP
python3 network_mapper.py
```

### Make Executable (Optional)
```bash
chmod +x network_mapper.py
./network_mapper.py
```

## 🔄 Complete Workflow (6 Stages)

### Stage 1: System Information Collection
- **Command**: `show system | no-more`
- **Purpose**: Collect device details, version, uptime, components
- **Function**: `parse_system_information(output, credentials, existing_device_name=None)`
- **Output**: `{device}_System_Information.json`

### Stage 2: Interface Information Collection  
- **Command**: `show interfaces | no-more`
- **Purpose**: Collect basic interface states, IPs, VLANs, MTU
- **Function**: `parse_interface_information(output, device_name)`
- **Output**: `{device}_interfaces.json`

### Stage 3: Detailed Interface Information Collection
- **Command**: `show interfaces detail | no-more`
- **Purpose**: Collect comprehensive interface details (MAC, speed, FEC, etc.)
- **Function**: `parse_detailed_interface_information(output, device_name)`
- **Output**: `{device}_interfaces_detail.json`

### Stage 4: LLDP Neighbor Discovery
- **Command**: `show lldp neighbors | no-more`
- **Purpose**: Discover network topology and connections
- **Function**: `parse_lldp_information(output, device_name)`
- **Output**: `{device}_LLDP_Connections.json`

### Stage 5: Configuration Backup
- **Commands**: 
  - `configure`
  - `save {device_name}_config`
  - `request file upload config {device_name}_config dn@192.168.166.142:/path out-of-band`
- **Purpose**: Backup device configuration to server
- **Function**: `save_and_upload_config(device_name)`
- **Authentication**: Automatic password handling (`drive1234!`)
- **Output**: `{device}_config`

### Stage 6: Data Validation
- **Purpose**: Validate all collected data against fresh device queries
- **Function**: `validate_saved_data(device_name)`
- **Validation Types**:
  - Interface data validation
  - System information validation  
  - LLDP data validation

## 🔧 Key Functions

### Connection Management
```python
def connect_to_device(self, credentials)
```
- Establishes SSH connection using paramiko
- Handles authentication and shell setup
- Returns True/False for success/failure

```python
def wait_for_cli_ready(self)
```
- Waits for device CLI to be ready
- Detects command prompts
- Handles initial device output

```python
def execute_command(self, command)
```
- Executes commands on connected device
- Handles command output collection
- Detects command completion via prompts

### Data Parsing Functions

```python
def parse_system_information(self, output, credentials, existing_device_name=None)
```
- Parses `show system` output
- Extracts device name, serial, model, version
- Supports both new and existing devices
- Creates device directory structure

```python
def parse_interface_information(self, output, device_name)
```
- Parses `show interfaces` tabular output
- Auto-detects DRIVENETS format
- Extracts admin/operational states, IPs, VLANs
- Handles bundle and physical interfaces

```python
def parse_detailed_interface_information(self, output, device_name)
```
- Parses `show interfaces detail` output
- Extracts comprehensive interface details:
  - MAC addresses (current and hardware)
  - Speed, duplex, MTU values
  - IPv4/IPv6 configuration
  - FEC, encapsulation settings
  - Utilization rates and statistics
- Provides both raw output and parsed fields

```python
def _parse_detailed_interface_fields(self, line, parsed_fields)
```
- Helper function for detailed parsing
- Extracts specific fields from interface detail lines
- Handles various field formats and edge cases

```python
def parse_lldp_information(self, output, device_name)
```
- Parses LLDP neighbor table
- Creates topology mapping
- Handles interfaces without neighbors

### Configuration Backup Functions

```python
def save_and_upload_config(self, device_name)
```
- Saves device configuration to device storage
- Uploads configuration to server via out-of-band
- Handles password authentication automatically
- Error handling and validation

### Validation Functions

```python
def validate_saved_data(self, device_name)
```
- Validates all collected data against fresh device queries
- Detects discrepancies and missing data
- Reports validation results

```python
def _validate_interface_data(self, device_name)
def _validate_system_data(self, device_name)  
def _validate_lldp_data(self, device_name)
```
- Specific validation functions for each data type
- Compare saved JSON data with fresh device data
- Provide detailed validation reports

---

# 🛠️ Interface Enabler (`interface_enabler.py`)

## 🎯 Purpose
Advanced interface configuration tool with bulk operations, smart filtering, and automatic validation. Supports enable/disable, speed configuration, breakout operations, and LLDP management.

## 🚀 How to Run

```bash
cd /home/dn/Eddie-scripts/monitorAPP
python3 interface_enabler.py
```

## 🔄 Complete Workflow (7 Steps)

### Step 1: Device Selection
- **Function**: `display_device_menu()`
- **Purpose**: Choose device from `Devices/` folder
- **Data Source**: Scans for existing device JSON files

### Step 2: Configuration Type Selection
- **Function**: `display_configuration_menu()`
- **Options**:
  1. Enable interfaces
  2. Disable interfaces  
  3. Configure port speed
  4. Configure breakout
  5. Enable LLDP on interfaces
  6. Disable LLDP on interfaces

### Step 3: Interface Selection
- **Function**: `select_interfaces(physical_interfaces, config_type)`
- **Smart Filtering**: Automatically excludes "not-present" interfaces
- **Selection Options**:
  - Individual interfaces (e.g., 1,3,5)
  - Ranges (e.g., 1-10)
  - All interfaces
- **Display**: Shows current admin/operational states

### Step 4: Configuration Generation
- **Functions**:
  - `generate_bulk_configuration()` - Standard operations
  - `generate_breakout_configuration_with_validation()` - Breakout with validation
- **Smart Processing**:
  - Filters not-present interfaces for enable/disable/LLDP
  - Special validation for breakout operations

### Step 5: Apply Configuration
- **Function**: `execute_commands(commands)`
- **Method**: True bulk paste (all commands as single block)
- **Connection**: SSH to device using stored credentials

### Step 6: Commit Configuration
- **Function**: `commit_configuration()`
- **Validation**: Waits for "Commit succeeded by dnroot" confirmation
- **Error Handling**: Detects and reports commit failures

### Step 7: Automatic Validation
- **Function**: `validate_configuration(device_name)`
- **Process**: Runs network_mapper to update all JSON files
- **Updates**: All device data refreshed with current states

## 🔧 Key Functions

### Device Management
```python
def get_available_devices(self)
```
- Scans `Devices/` directory for existing devices
- Validates device folders contain required JSON files
- Returns list of available devices

```python
def load_device_interfaces(self, device_name)
```
- Loads interface data from device JSON file
- Returns interfaces dictionary for processing

```python
def get_physical_interfaces(self, interfaces_data)
```
- Filters physical interfaces from all interfaces
- Excludes logical interfaces (bundle-, lo, mgmt, etc.)
- **Smart Filtering**: Excludes "not-present" interfaces
- Returns only configurable physical interfaces

### Interface Filtering
```python
def filter_interfaces_for_lldp(self, interfaces, interfaces_data)
```
- Filters interfaces for LLDP configuration
- Excludes "not-present" interfaces
- Provides logging for skipped interfaces
- Used for both LLDP and enable/disable operations

### Configuration Generation
```python
def generate_bulk_configuration(self, interfaces, config_type, config_value=None)
```
- Generates bulk configuration commands
- **Config Types**:
  - Type 1: Enable (`admin-state enabled`)
  - Type 2: Disable (`admin-state disabled`)
  - Type 3: Speed (`speed {value}`)
  - Type 5: Enable LLDP (`protocols lldp interface {interface} ^`)
  - Type 6: Disable LLDP (`no protocols lldp interface {interface} ^`)

```python
def generate_breakout_configuration_with_validation(self, interfaces, config_value, device_name)
```
- Special breakout configuration with validation
- **Validation Steps**:
  1. Remove all interface configurations (`no interfaces {interface}`)
  2. Remove LLDP configuration (`no protocols lldp interface {interface} ^`)
  3. Apply breakout (`interfaces {interface} breakout {mode}`)

### Speed and Breakout Configuration
```python
def get_speed_configuration(self)
```
- Interactive speed selection menu
- **Supported Speeds**: 1G, 10G, 25G, 100G, 400G
- Returns numeric speed value

```python
def get_breakout_configuration(self)
```
- Interactive breakout mode selection
- **Supported Modes**:
  - `10g-4x` (Break 100G into 4x10G)
  - `100g-4x` (Break 400G into 4x100G)
  - `200g-2x` (Break 400G into 2x200G)
  - `100g-2x` (Break 400G into 2x100G)
  - `400g-2x` (Break 800G into 2x400G)
  - `none` (Remove breakout)

### SSH Connection and Command Execution
```python
def connect_to_device(self, device_name)
```
- Connects to device using stored credentials
- Reads hostname from system information JSON
- Uses dnroot/dnroot credentials

```python
def execute_commands(self, commands)
```
- **Bulk Paste Operation**: Sends all commands as single block
- **Performance**: ~5 seconds for 60+ interface commands
- **Method**: Joins commands with newlines and sends as one operation
- **Timeout**: 120 seconds for bulk operations

```python
def commit_configuration(self)
```
- Commits configuration changes
- **Validation**: Waits for "Commit succeeded by dnroot"
- **Confirmation Handling**: Automatically responds "yes" to prompts
- **Timeout**: 120 seconds for commit operations

### Validation and Integration
```python
def validate_configuration(self, device_name)
```
- Runs network_mapper in monitoring mode
- Updates all device JSON files
- Validates configuration was applied correctly
- **Integration**: Seamless network_mapper integration

## 📊 Configuration Command Examples

### Enable/Disable Operations
```bash
configure
interfaces
ge400-0/0/0 admin-state enabled
ge400-0/0/1 admin-state enabled
ge400-0/0/2 admin-state disabled
top
```

### Speed Configuration
```bash
configure
interfaces
ge400-0/0/0 speed 100
ge400-0/0/1 speed 100
top
```

### Breakout Configuration (with Validation)
```bash
configure
no interfaces ge400-0/0/0
no protocols lldp interface ge400-0/0/0 ^
interfaces ge400-0/0/0 breakout 100g-2x
top
```

### LLDP Configuration
```bash
configure
protocols lldp interface ge100-0/0/0/0 ^
protocols lldp interface ge100-0/0/0/1 ^
top
```

## 🛡️ Smart Interface Filtering

### Physical Interface Detection
- **Included**: `ge*`, `xe*`, `ce*` interfaces
- **Excluded**: `bundle-*`, `lo*`, `mgmt*`, `ctrl-*`, `ice*`

### Operational State Filtering
- **Included**: Interfaces with operational_state != "not-present"
- **Excluded**: "not-present" interfaces (prevents configuration errors)
- **Applied To**: Enable, Disable, LLDP operations
- **Not Applied To**: Speed and Breakout (user choice)

---

# 📊 Output File Formats

## System Information JSON
```json
{
  "device_name": "NEW-NCP3",
  "login_credentials": {
    "hostname": "YE41F7VK00003B1",
    "username": "dnroot",
    "password": "dnroot"
  },
  "parsed_info": {
    "version": "DNOS [25.4.0] build [41_priv]",
    "uptime": "0 days, 2:04:25",
    "system_type": "SA-36CD-S-SA",
    "components": [...]
  }
}
```

## Interface Information JSON
```json
{
  "device_name": "NEW-NCP3",
  "timestamp": "2025-09-07T15:39:18.057084",
  "total_interfaces": 94,
  "interfaces": {
    "ge400-0/0/0": {
      "interface_name": "ge400-0/0/0",
      "admin_state": "enabled",
      "operational_state": "down",
      "bundle": "",
      "mtu": "1514",
      "vlan": "",
      "vrf": "VRF (default)",
      "ipv4": [],
      "ipv6": []
    }
  }
}
```

## Detailed Interface Information JSON
```json
{
  "device_name": "NEW-NCP3",
  "timestamp": "2025-09-07T16:33:56.974796",
  "total_interfaces": 94,
  "interfaces_detail": {
    "ge400-0/0/0": {
      "interface_name": "ge400-0/0/0",
      "raw_output": [
        "SNMP ifindex: 1, Network-Service: VRF (default)",
        "Admin state: enabled, Physical link state: down, Operational state: down",
        "MAC Address: 34:2c:8e:2a:f8:00 (HW: 34:2c:8e:2a:f8:00)",
        "Speed: 100Gbps, Duplex: FULL, Bundle-id: N/A"
      ],
      "parsed_fields": {
        "snmp_ifindex": "1",
        "network_service": "VRF (default)",
        "admin_state": "enabled",
        "physical_link_state": "down",
        "operational_state": "down",
        "mac_address": "34:2c:8e:2a:f8:00",
        "speed": "100Gbps",
        "duplex": "FULL"
      }
    }
  }
}
```

## LLDP Connections JSON
```json
{
  "device_name": "NEW-NCP3",
  "timestamp": "2025-09-07T15:39:18.057084",
  "lldp_status": "active",
  "total_connections": 9,
  "lldp_connections": {
    "ge100-0/0/10/0": {
      "local_interface": "ge100-0/0/10/0",
      "neighbor_system": "NEW-NCP3",
      "neighbor_interface": "ge100-0/0/20/0",
      "neighbor_ttl": "120"
    }
  }
}
```

---

# 🔗 Integration Between Tools

## Network Mapper → Interface Enabler
- Interface Enabler reads device data from network_mapper JSON files
- Device selection based on existing network_mapper discoveries
- Interface lists populated from network_mapper data

## Interface Enabler → Network Mapper
- After configuration changes, automatically runs network_mapper
- Updates all JSON files with current device state
- Validates that configuration was applied correctly

## Shared Functions and Data
- **Credentials**: Both tools use same credential storage format
- **Device Discovery**: Shared device directory structure
- **SSH Connection**: Similar connection handling patterns
- **Error Handling**: Consistent logging and error reporting

---

# 🎛️ Advanced Features

## Bulk Configuration Operations
- **True Bulk Paste**: All commands sent as single block (not individual)
- **Performance**: 60+ interface operations in ~5 seconds
- **Error Prevention**: Smart filtering prevents invalid configurations
- **Commit Verification**: Waits for actual device confirmation

## Breakout Configuration Validation
- **Prerequisites Checking**:
  1. Interface must be disabled
  2. LLDP must be removed
  3. No bundle membership
- **Automatic Cleanup**: Removes all interface configurations before breakout
- **Error Prevention**: Validates requirements before applying

## LLDP Management
- **Enable**: `protocols lldp interface {interface} ^`
- **Disable**: `no protocols lldp interface {interface} ^`
- **Smart Filtering**: Only configures present interfaces
- **Bulk Operations**: Applies to multiple interfaces simultaneously

## Configuration Backup and Upload
- **Automatic Backup**: Every network_mapper run creates config backup
- **Server Upload**: Direct upload to device folder
- **Authentication**: Automatic password handling
- **Path Format**: `dn@192.168.166.142:/full/path out-of-band`

---

# 🔍 Troubleshooting

## Connection Issues
1. **Check SSH connectivity**: `ssh dnroot@{hostname}`
2. **Verify credentials**: Username/password = dnroot/dnroot
3. **Check device accessibility**: Ensure device is reachable
4. **Verify hostname**: Check system information JSON for correct hostname

## Configuration Issues
1. **Bundle Membership**: Breakout fails if interface is in bundle
2. **Not-Present Interfaces**: Automatically filtered out
3. **LLDP Dependencies**: Automatically removed for breakout
4. **Commit Timeout**: Check device load and network connectivity

## Data Collection Issues
1. **Missing Commands**: Ensure device supports required show commands
2. **LLDP Unavailable**: Normal if LLDP not enabled (creates empty data)
3. **Parsing Errors**: Check device output format compatibility
4. **Upload Failures**: Verify server accessibility and path permissions

## Validation Issues
1. **Interface Mismatches**: Usually indicates device state changes
2. **LLDP Discrepancies**: Normal for interfaces without neighbors
3. **System Info Changes**: Device may have been updated/rebooted

---

# 📝 Logging and Debugging

## Log Files
- **Location**: `logs/` directory (excluded from git)
- **Format**: `{tool}_{timestamp}.log`
- **Content**: Detailed execution logs with timestamps
- **Levels**: INFO, DEBUG, WARNING, ERROR

## Debug Information
- **SSH Connection**: Detailed connection logs
- **Command Execution**: Command input/output logging
- **Data Parsing**: Step-by-step parsing information
- **Validation**: Detailed validation results

## Error Handling
- **SSH Failures**: Connection timeout and retry logic
- **Command Failures**: Graceful handling of failed commands
- **Parsing Errors**: Continue operation with warnings
- **Commit Failures**: Clear error reporting and rollback

---

# 🔒 Security Considerations

## Credential Management
- **Storage**: Credentials stored in device system information JSON
- **Transmission**: SSH encrypted communication
- **Repository**: No credentials in git repository (.gitignore)

## Data Privacy
- **Local Storage**: All device data stored locally
- **Git Exclusions**: Sensitive data excluded from repository
- **Access Control**: Device folder permissions

## Network Security
- **SSH Only**: All communication via encrypted SSH
- **Out-of-band Upload**: Configuration upload via dedicated management network
- **Authentication**: Password-protected file transfers

---

# 🚀 Getting Started

## Prerequisites
- Python 3.x
- paramiko library
- SSH access to DNOS devices
- Network connectivity to devices

## Installation
```bash
git clone https://github.com/ehaimov-dn/monitorAPP.git
cd monitorAPP
pip install paramiko  # if not already installed
```

## First Run
1. **Discover Devices**: `python3 network_mapper.py`
2. **Configure Interfaces**: `python3 interface_enabler.py`
3. **Check Results**: Review JSON files in `Devices/` folder

## Typical Workflow
1. **Initial Discovery**: Run network_mapper on new devices
2. **Interface Configuration**: Use interface_enabler for bulk operations
3. **Validation**: Automatic validation ensures changes were applied
4. **Monitoring**: Regular network_mapper runs for ongoing monitoring

---

# 📈 Performance Characteristics

## Network Mapper Performance
- **Connection Time**: ~3 seconds
- **Interface Collection**: ~5 seconds for 100 interfaces
- **Detailed Collection**: ~25 seconds for 100 interfaces
- **LLDP Collection**: ~4 seconds
- **Configuration Backup**: ~5 seconds with upload
- **Total Time**: ~45 seconds for complete device documentation

## Interface Enabler Performance
- **Configuration Generation**: Instant
- **Bulk Configuration**: ~5 seconds for 60+ interfaces
- **Commit Time**: ~2-5 seconds
- **Validation**: ~45 seconds (full network_mapper run)
- **Total Time**: ~60 seconds for complete configuration cycle

---

# 🆕 Recent Enhancements

## Version 2.0 Features
- ✅ **Detailed Interface Information**: Complete interface parameter collection
- ✅ **Configuration Backup**: Automatic device config save and upload
- ✅ **LLDP Management**: Enable/disable LLDP on interfaces
- ✅ **Smart Filtering**: Excludes not-present interfaces from operations
- ✅ **Enhanced Breakout**: Proper validation and cleanup
- ✅ **Independent Operation**: Both tools work standalone or integrated

## Security Enhancements
- ✅ **Git Ignore**: Sensitive data excluded from repository
- ✅ **Credential Protection**: No hardcoded passwords in code
- ✅ **Data Privacy**: Device data kept local only

## Performance Improvements
- ✅ **Bulk Operations**: True bulk paste instead of individual commands
- ✅ **Parallel Processing**: Efficient data collection
- ✅ **Smart Caching**: Reuses existing device data when appropriate

---

This toolkit provides enterprise-grade network monitoring and configuration capabilities with comprehensive automation, validation, and security features.
