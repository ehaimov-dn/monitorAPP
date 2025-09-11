# Monitor Applications

This folder contains three Python-based monitoring applications for network devices and system resources.

## 📊 Available Monitors

### 1. **interface_monitor.py** - Network Interface Database Monitor
**Purpose**: Multi-device interface monitoring and database synchronization

**Key Features**:
- 🔗 SSH connection to multiple network devices
- 📡 Real-time interface monitoring using `show interfaces | monitor interval 5`
- 💾 Auto-saves interface data to JSON databases in `data/interfaces/`
- 📈 Tracks admin/operational states, IP addresses, VLANs, MTU
- 🔄 60-second initial collection, then saves every 15 seconds
- 📊 Interface statistics and gap detection
- 🧵 Multi-threaded for concurrent device monitoring

**Usage**:
```bash
python3 interface_monitor.py
```

**Output Files**: `data/interfaces/{hostname}_interfaces_info.json`

---

### 2. **linux_interface_monitor.py** - Linux Namespace Interface Monitor
**Purpose**: Interactive Linux interface discovery and real-time state monitoring

**Key Features**:
- 🖥️ Interactive device and interface selection
- 🐧 Enters device inband namespace (`ip netns exec inband_ns bash`)
- 🔍 Discovers Linux ethernet interfaces using `ip -brief link show`
- 🔄 Translates hex interface names (e00001) → network names (ge100-0/0/X)
- ⚡ Real-time state monitoring every 1 second
- 📝 Continuous logging with state change detection
- 🧹 Advanced ANSI sequence cleaning and shell handling

**Usage**:
```bash
# Interactive mode
python3 linux_interface_monitor.py

# Direct mode
python3 linux_interface_monitor.py --device DEVICE_NAME --interface INTERFACE_NAME

# Configuration mode
python3 linux_interface_monitor.py --config-mode
```

**Output Files**: 
- `logs/linux_interface_monitor_{hostname}_{timestamp}.log`
- `logs/linux_interface_monitor_{hostname}_{timestamp}_continuous.log`
- `logs/linux_interface_monitor_{hostname}_{timestamp}_changes.log`

---

### 3. **memory_monitor.py** - System Memory Monitor
**Purpose**: Continuous memory usage monitoring on DNOS devices

**Key Features**:
- 🖥️ Connects to DNOS devices and accesses Linux shell
- 📊 Real-time memory monitoring using `free -h` and `/proc/meminfo`
- 📈 Visual progress bars and usage percentages
- 💾 Auto-saves memory history every 10 seconds
- 📉 Detailed memory statistics (Total, Used, Free, Available, etc.)
- 🗃️ Automatic data retention (keeps last 1000 samples)

**Usage**:
```bash
python3 memory_monitor.py
```

**Target Device**: 192.168.162.141 (configured in script)

**Output Files**: `data/monitoring/{hostname}_memory_monitor.json`

---

## 🛠️ Requirements

### Python Dependencies
```bash
pip install paramiko
```

### Configuration Files
- `data/config/devices_config.json` - Device connection configuration
- Existing interface JSON files for device discovery

### Directory Structure
```
data/
├── config/
│   └── devices_config.json
├── interfaces/
│   └── {hostname}_interfaces_info.json
└── monitoring/
    └── {hostname}_memory_monitor.json
logs/
└── linux_interface_monitor_*.log
```

---

## 🚀 Quick Start

1. **Configure devices** in `data/config/devices_config.json`
2. **Run interface monitoring** to populate device databases:
   ```bash
   python3 interface_monitor.py
   ```
3. **Monitor specific interfaces** interactively:
   ```bash
   python3 linux_interface_monitor.py
   ```
4. **Monitor memory usage**:
   ```bash
   python3 memory_monitor.py
   ```

---

## 📝 Notes

- All monitors use SSH (paramiko) for device connections
- Default credentials: username/password = "dnroot"/"dnroot"
- Interface monitors work with ge100-X/Y/Z interface format
- Memory monitor targets specific IP (192.168.162.141)
- Linux interface monitor requires inband namespace access
- All applications support graceful shutdown with Ctrl+C

---

**Last Updated**: December 2024 