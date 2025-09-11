# DNOS Boot Monitor Script

## Overview
The `boot_monitor.py` script is designed to perform automated restart testing on DNOS devices with comprehensive monitoring and core file collection capabilities.

## Features

### 🔄 Restart Types
- **Warm Restart**: `request system restart warm` - Software-only restart
- **Cold Restart**: `request system restart` - Complete power cycle restart  
- **Both**: Performs both warm and cold restarts in sequence

### 📊 Monitoring Capabilities
- **Boot Time Measurement**: Precise timing from restart initiation to full operational state
- **System Health Verification**: Checks for "System status: running" and active processes
- **Core File Detection**: Automatically collects core files generated during restart cycles
- **Comprehensive Logging**: Detailed logs for troubleshooting and analysis

### 📁 File Organization
```
monitorAPP/
├── boot_monitor.py          # Main script
├── logs/                    # Execution logs
│   └── boot_monitor_YYYYMMDD_HHMMSS.log
├── monitor/                 # Monitoring results
│   ├── {device}_warm_restart_results.json
│   ├── {device}_cold_restart_results.json
│   └── core_files/
│       └── {device}-core_files_restartcycle_{type}_{num}/
│           └── core_files_info.json
```

## Usage

### Interactive Mode
```bash
python3 boot_monitor.py
```

Follow the interactive prompts:
1. **Select Device**: Choose from available devices in `/Devices/` directory
2. **Select Restart Type**: warm, cold, or both
3. **Number of Cycles**: How many restart cycles to perform
4. **Confirmation**: Review settings and confirm

### Example Session
```
==================================================
DNOS BOOT MONITOR
==================================================

Available devices:
1. NEW-NCP3
2. R1_CL16_Eddie
3. R2_SA40_Eddie

Select device (1-3): 1

Restart types:
1. Warm restart
2. Cold restart
3. Both (warm and cold)

Select restart type (1-3): 3

Number of restart cycles: 5

Configuration:
Device: NEW-NCP3
Restart type: both
Number of cycles: 5
Total restarts: 10 (5 warm + 5 cold)

Proceed with monitoring? (y/n): y
```

## DNOS Commands Used

### Restart Commands Found:
- **Cold Restart**: `request system restart`
- **Warm Restart**: `request system restart warm`

Both commands prompt for confirmation:
```
Warning: Are you sure you want to perform a system restart? (Yes/No) [No]?
```

### System Status Commands:
- `show system | no-more` - Check system operational status
- `show system process-state running | no-more` - Verify processes
- `show system uptime | no-more` - Get device time
- `show file all core list | no-more` - List core files

## Output Files

### Restart Results JSON Format
```json
[
  {
    "cycle": 1,
    "restart_time": "2025-09-10 15:30:00",
    "operational_time": "2025-09-10 15:32:45", 
    "total_time": "165.23 seconds",
    "status": "SUCCESS"
  }
]
```

### Core Files JSON Format
```json
[
  {
    "node_type": "NCC",
    "node_id": "0", 
    "filename": "routing_engine/core-snmpd.51866.sig-6.2020-06-03.13-21-16.tar",
    "size": "720K",
    "timestamp": "03-Jun-2020 13:21:00 UTC",
    "restart_cycle": "warm_1"
  }
]
```

## Key Features

### 🕐 Precise Timing
- Measures exact time from restart command to full system operational state
- Excludes core file collection time from boot measurements
- Fast detection mechanism to minimize timing overhead

### 🔍 Core File Management
- Checks for core files generated in the last 3 hours
- Avoids duplicate core file entries
- Organizes core files by device and restart cycle
- Only collects core files AFTER restart measurements are complete

### 🛡️ Robust Operation
- Graceful shutdown handling (Ctrl+C)
- Connection retry logic for device recovery
- Error handling and detailed logging
- Background operation capability for overnight runs

### 📈 Comprehensive Reporting
- Real-time progress logging
- Final summary with statistics
- Success rates and average recovery times
- Separate tracking for warm vs cold restarts

## Background Operation

The script is designed to run in the background and automatically terminate when complete:

```bash
# Run in background
nohup python3 boot_monitor.py &

# Monitor progress
tail -f logs/boot_monitor_*.log
```

## Requirements

### Device Prerequisites
- DNOS device accessible via SSH
- Device information in `Devices/{device_name}/{device_name}_System_Information.json`
- Admin-level access (required for restart commands)

### Python Dependencies
- `paramiko` - SSH connections
- `json` - Data serialization
- `logging` - Comprehensive logging
- Standard library modules (time, datetime, os, sys, etc.)

## Troubleshooting

### Common Issues
1. **Connection Timeouts**: Device may take longer to recover - increase timeout values
2. **Permission Denied**: Ensure user has admin privileges for restart commands
3. **Core File Access**: Some core files may be restricted - script handles gracefully

### Log Locations
- Main log: `logs/boot_monitor_YYYYMMDD_HHMMSS.log`
- Results: `monitor/{device}_*_restart_results.json`
- Core files: `monitor/core_files/{device}-core_files_restartcycle_*`

## Safety Features
- Confirmation prompts before starting
- Graceful shutdown on interruption
- Connection cleanup on exit
- Error recovery and continuation
- No hanging processes after completion

## Performance Considerations
- Optimized for minimal timing overhead
- Efficient SSH connection management
- Background-friendly operation
- Automatic resource cleanup
