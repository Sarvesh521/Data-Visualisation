# Quiver plot visualizations for wind data

This directory contains Python scripts for generating visualizations of wind data, including quiver plots with color-coded wind speed and animation support. These scripts utilize `xarray` for data manipulation and `cartopy` for geographical plotting.

## Prerequisites

Before running the scripts, ensure Python and the following Python libraries are installed in your environment:

- `xarray`
- `cartopy`
- `numpy`
- `matplotlib`

### Installing the Necessary Libraries

Use the following commands in a Linux terminal to install the required dependencies:

```bash
# Update the package manager
sudo apt update

# Install pip if not already installed
sudo apt install python3-pip

# Install the required Python libraries
pip install xarray cartopy numpy matplotlib
```

# Running the Scripts
To execute any of the Python scripts, use the following command in the terminal:

```bash
python <filename>.py
```
Replace <filename> with the actual name of the script.

# Customizing Quiver Plot Scale
The scale basis of the quiver plot arrows can be adjusted using the global variable  `SCALE_UNITS` within the scripts. Modify its value to suit the visualization requirements.

# Other Instructions
- Ensure the dataset files required by the scripts are in the correct directory or provide the full path in the code where necessary.
- The scripts automatically handle date selection, downsampling, and arrow length adjustment based on the dataset. Adjustments to these features can be made directly in the code if needed.
- The input path for the dataset can be modified by changing the `th_path` and `vs_path` variable in the code.
- The output path for th gif can be specified by modifying the `OUTPUT_PATH` variable in the code. ENsure that the directory exists before running the script.

# Notes
- The scripts support visualizing wind data for January to March.
- Specific date ranges can be selected within the scripts by modifying the relevant variables.
- Color-mapping for wind speed is handled automatically but can be customized by editing the colormap settings in the Matplotlib code section.
