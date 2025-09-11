# DNOS Boot Monitor - Usage Guide

## 🚀 Quick Start

```bash
python3 boot_monitor.py
```

## ✅ What's Working

The boot monitor successfully:
- **Automatically restarts DNOS devices** (warm/cold/both)
- **Measures precise boot times** (last test: 118.53 seconds)
- **Uses only valid DNOS commands** from documentation
- **Polls device status every 5 seconds** during recovery
- **Collects core files** automatically after restart
- **Runs in background** for overnight testing

## 📊 Last Successful Test Results

**Device:** NEW-NCP3
**Restart Type:** Warm restart
**Recovery Time:** 118.53 seconds
**Success Rate:** 100%
**Status:** FULLY OPERATIONAL

## 🎯 Available Options

1. **Restart Types:**
   - Warm restart (`request system restart warm`)
   - Cold restart (`request system restart`)
   - Both (performs warm + cold cycles)

2. **Devices Available:**
   - NEW-NCP3
   - R1_CL16_Eddie
   - R2_SA40_Eddie
   - R3_SA40_Eddie
   - R4_SA40_Eddie

## 📁 Output Files

- **Results:** `monitor/{device}_{type}_restart_results.json`
- **Logs:** `logs/boot_monitor_YYYYMMDD_HHMMSS.log`
- **Core Files:** `monitor/core_files/{device}-core_files_restartcycle_{type}_{num}/`

## ⚠️ Important Notes

- Script automatically answers 'yes' to all restart confirmations
- No user intervention required during restart process
- Device recovery monitored every 5 seconds
- Safe to run overnight with multiple cycles
