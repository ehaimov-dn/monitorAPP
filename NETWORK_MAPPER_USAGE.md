# Network Mapper Usage Guide

## Overview
The `network_mapper.py` script connects to network devices via SSH and collects:
- System information
- Interface details
- LLDP neighbor connections

All data is saved in JSON format under the `Devices/` folder.

## Directory Structure
```
/home/dn/Eddie-scripts/monitorAPP/
├── network_mapper.py          # Main script
├── Devices/                   # Device data storage
│   └── [device_name]/         # Each device gets its own folder
│       ├── [device]_System_Information.json
│       ├── [device]_interfaces.json
│       └── [device]_LLDP_Connections.json
├── logs/                      # Script execution logs
└── data/                      # Legacy interface data (existing)
```

## How to Run

### 1. Basic Execution
```bash
cd /home/dn/Eddie-scripts/monitorAPP
python3 network_mapper.py
```

### 2. Make it executable (optional)
```bash
chmod +x network_mapper.py
./network_mapper.py
```

## Usage Flow

1. **Device Selection Menu**
   - Choose "0" for new device (SSH connection)
   - Or select existing device from list

2. **For New Devices**
   - Enter hostname/IP address
   - Enter username
   - Enter password (hidden input)

3. **Data Collection**
   - System information (`show system | no-more`)
   - Interface details (`show interfaces | no-more`)
   - LLDP neighbors (`show lldp neighbors | no-more`)

4. **Data Validation**
   - Automatically validates collected data
   - Reports any discrepancies
   - Updates JSON files if needed

## Output Files

### System Information
- File: `Devices/[device_name]/[device_name]_System_Information.json`
- Contains: Device name, model, serial, uptime, credentials, etc.

### Interface Information
- File: `Devices/[device_name]/[device_name]_interfaces.json`
- Contains: All interfaces with admin/operational states, IPs, VLANs, etc.

### LLDP Connections
- File: `Devices/[device_name]/[device_name]_LLDP_Connections.json`
- Contains: Neighbor relationships and topology information

## Supported Devices
- DRIVENETS devices (auto-detected)
  - Supports ge100-, ge400-, bundle-, and lo interfaces
- Cisco devices
- Juniper devices
- Any device supporting standard CLI commands

## Troubleshooting

### Connection Issues
1. Verify SSH connectivity: `ssh username@hostname`
2. Check device supports required commands
3. Ensure proper credentials

### Missing LLDP Data
- LLDP may not be enabled on device
- Script will create empty LLDP file with status "unavailable"

### Logs
Check `logs/network_mapper_[timestamp].log` for detailed execution information.

## Dependencies
- Python 3.x
- paramiko (SSH client)
- Standard Python libraries (json, logging, re, etc.)

All dependencies are already available on this system.
