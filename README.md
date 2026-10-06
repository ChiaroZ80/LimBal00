# lim_bal - Serial Communication & Data Visualization

**README in:** [English](README.md) | [Português](docs/README_pt-br.md) | [Español](docs/README_es.md) | [Deutsch](docs/README_de.md) | [Français](docs/README_fr.md)

---

## Overview

lim_bal is a desktop application for serial communication and real-time data visualization. Connect to Arduino or other serial devices, collect numeric measurements, and create dynamic graphs. The interface is available in English, Portuguese, Spanish, German, and French.

![lim_bal screenshot](docs/shot.png)

![lim_bal screenshot](docs/shot_stacked.png)

## Features

### 🌍 **Multiple Languages**
- Available in English, Portuguese, Spanish, German, and French
- Change language from the menu (requires restart)
- All settings preserved when switching languages

### 📡 **Easy Serial Connection**
- Connect to real serial devices (Arduino, sensors, etc.)
- Built-in simulation mode for testing without hardware
- Automatic port detection with one-click refresh
- Full Arduino IDE baudrate compatibility (300-2000000 bps)
- Default baudrate: 9600
- Quick hardware commands: SI, SIR, Zerar, and Tara
- Send custom text commands; each send appends CRLF

### 📊 **Professional Data Visualization**
- **Time Series Charts**: Plot up to 5 data columns simultaneously
- **Stacked Area Charts**: Compare data as absolute values or percentages
- **Customizable Appearance**: Choose colors, markers, and line types for each data series
- **Real-time Updates**: Configurable refresh rates (1-30 FPS)
- **Export**: Save graphs as high-quality PNG images
- **Interactive Controls**: Pause/resume charts, zoom, and pan
- **Device Controls**: SI, SIR, and Stop buttons on the Graph tab

### 💾 **Smart Data Management**
- **Manual Save/Load**: Export and import your data anytime
- **Automatic Backup**: Optional autosave with timestamped filenames
- **Data Safety**: Clear data with confirmation prompts
- **All Settings Saved**: Preferences automatically preserved between sessions
- **Plot data**: Choose whether incoming measurements are added to Data and used by charts
- **Receive data**: View every received line with a sequence number and elapsed connection time

## Getting Started

### Requirements
- Python 3.7 or newer
- Internet connection for dependency installation

### Installation
```bash
# Clone the repository
git clone https://github.com/ChiaroZ80/LimBal00.git
cd LimBal00

# Create and activate a virtual environment
python -m venv .venv
# Windows Command Prompt: .venv\Scripts\activate.bat
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

# Install required packages and run lim_bal
python -m pip install matplotlib pyserial PyYAML
python lim_bal.py
```

### First Steps
1. **Language**: Choose your language from the Language menu
2. **Connection**: In Configuration, select the serial port and baudrate, then connect
3. **Receive**: View incoming lines and elapsed time in Configuration
4. **Data**: Enable Plot data to record numeric measurements in Data and use them in charts
5. **Visualization**: Use Graph to create charts or send SI, SIR, and Stop commands

## How to Use

### Configuration Tab
- **Mode**: Choose "Hardware" for real devices, "Simulated" for testing
- **Port**: Select your serial port (click Refresh to update the list)
- **Baudrate**: Set the communication speed (default: 9600; match your device settings)
- **Plot data**: Enable or disable recording received values in Data
- **SI / SIR / Zerar / Tara**: Send the corresponding hardware command
- **Send data**: Send custom text followed by CRLF
- **Receive data**: View all incoming lines with a line counter and elapsed seconds
- **Connect / Disconnect**: Start or stop the hardware connection

### Data Tab
- **View Data**: See numeric measurements, line counter, and elapsed time when Plot data is enabled
- **Save Data**: Export current data to a text file
- **Load Data**: Import previously saved data files
- **Clear Data**: Reset the current dataset (with confirmation)
- **Autosave**: Toggle automatic backup with timestamped filenames

### Graph Tab
- **Choose Columns**: Select X-axis and up to 5 Y-axis columns from your data
- **Chart Types**:
  - **Time Series**: Individual line/scatter plots for each data series
  - **Stacked Area**: Layered charts showing cumulative data or percentages
- **Customize**: Expand "Show Advanced Options" to change colors, markers, refresh rate
- **Export**: Save your graphs as PNG images
- **Control**: Pause/resume real-time updates anytime
- **SI / SIR**: Send device commands from the Graph tab
- **Stop**: Send `@` followed by CRLF; the next received line is omitted from Data but remains visible in Receive data

### Language Menu
- **Switch Language**: Select from 5 available languages
- **Restart Required**: Application will prompt you to restart for language change
- **Settings Preserved**: All your preferences are kept when changing languages

## Data Format

Your serial device should send data in simple text format:

```
# Numeric data rows (space or tab separated)
1.0 3.3 0.125 25.4
2.0 3.2 0.130 25.6
3.0 3.4 0.122 25.2
```

**Supported formats:**
- Space or tab-separated columns
- Numbers in any column
- Non-numeric protocol/status lines are not added to Data
- Real-time streaming or batch data loading

## Troubleshooting

**Connection Issues:**
- Make sure your device is connected and powered on
- Check that no other program is using the serial port
- Try different baudrates if data appears garbled
- Use Simulated mode to test the interface without hardware

**Data Problems:**
- Ensure data is space or tab-separated
- Check that numbers are in standard format (use . for decimals)
- Verify your device is sending data continuously
- Try saving and reloading data to check format

**Performance:**
- Lower the refresh rate if charts are slow
- Reduce the data window size for better performance
- Close other programs if the system becomes unresponsive

## Development

This application is built with Python and uses tkinter for the interface and matplotlib for graphs.

**For developers:**
- The codebase uses a modular architecture with separate components for GUI, data management, and visualization
- Translations are stored in YAML files in the `languages/` directory
- Configuration uses a hierarchical preference system saved in `config/prefs.yml`
- The chart refresh system is decoupled from data arrival for optimal performance

**Contributing:**
- Fork the repository and create a feature branch
- Test changes with multiple languages and data scenarios
- Submit pull requests with clear descriptions
- Focus areas: new languages, visualization types, protocol support

## License

Developed by CBPF-LIM (Brazilian Center for Research in Physics - Light and Matter Laboratory).

---

**lim_bal** - Serial communication and data visualization.
