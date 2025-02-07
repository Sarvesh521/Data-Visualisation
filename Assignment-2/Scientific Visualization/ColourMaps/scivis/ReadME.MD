# Scientific Visualization of gridMET Dataset

## Introduction
This project focuses on the scientific visualization of the gridMET dataset for the first quarter of 2001. The aim is to analyze and visualize various meteorological variables to understand climatic patterns and changes over this period. The visualizations help in interpreting the spatial and temporal variations of different atmospheric parameters across the United States.

## Dataset
The dataset used is the gridMET dataset, which provides high-resolution gridded surface meteorological data. The time frame selected for this project is from January 1, 2001, to March 31, 2001

## Tools Used
- **Python 3.x**
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Cartopy**: A library providing cartographic tools for Python for plotting geospatial data.
- **xarray**: For handling multi-dimensional arrays (netCDF data) efficiently.
- **netCDF4**: To read and write netCDF files.
- **Imageio**: For creating animations (GIFs) from a series of images.

## Installation

To run this project, you need to have Python 3.x installed along with the necessary libraries. Follow the steps below to set up your environment:

1. **Install Python 3.x**

   Download and install Python from the [official website](https://www.python.org/downloads/) if you haven't already.

2. **Install Required Python Libraries**

   Open your terminal or command prompt and run the following command to install the necessary libraries using `pip`:

   ```bash
   pip install -r requirements.txt


## Project Structure

### Data Files
NetCDF (`.nc`) files for different meteorological variables:
- `https://www.northwestknowledge.net/metdata/data/pr_2001.nc`: Precipitation data.
- `https://www.northwestknowledge.net/metdata/data/vpd_2001.nc`: Vapor Pressure Deficit data.
- `https://www.northwestknowledge.net/metdata/data/vpd_2001.nc`: Relative Max Humidity data.
- `https://www.northwestknowledge.net/metdata/data/vpd_2001.nc`: Relative Min Humidity data.

### Python Scripts
- `scivis.py`: Main script for visualization tasks.

### Output Directories
Each script generates a directory containing plotted images and an animation GIF:
- `images/precipitation`
- `images/precipitation_log`
- `images/vpd`
- `images/vpd_extreme_local`
- `images/vpd_extreme_global`
- `images/rmax`
- `images/rmin`

## Visualizations

### 1. Precipitation
- **Objective**: Visualize precipitation amounts over the selected dates.
- **Method**:  
  Loaded the `pr_2001.nc` file using `xarray`. Selected data for specified dates and plotted maps using Cartopy with the 'viridis' colormap.
- **Observations**:  
  Displayed spatial distribution of precipitation with temporal changes visualized in the GIF.

### 2. Precipitation Log
- **Objective**: Visualize logarithmic precipitation amounts to highlight variations.
- **Method**:  
  Applied a logarithmic transformation to the precipitation data and plotted using Cartopy.
- **Observations**:  
  Enhanced visibility of lower precipitation values.

### 3. Vapor Pressure Deficit (VPD)
- **Objective**: Visualize vapor pressure deficit across the dataset.
- **Method**:  
  Loaded the `vpd_2001.nc` file and plotted using Cartopy.
- **Observations**:  
  Highlighted areas with high atmospheric moisture demand.

### 4. VPD Extreme Local
- **Objective**: Identify and visualize extreme local VPD values.
- **Method**:  
  Processed VPD data to extract extreme local values and plotted accordingly.
- **Observations**:  
  Identified hotspots of extreme VPD.

### 5. VPD Extreme Global
- **Objective**: Visualize global extremes in vapor pressure deficit.
- **Method**:  
  Aggregated VPD data globally and plotted extremes using Cartopy.
- **Observations**:  
  Global distribution of extreme VPD values.

### 6. Rmax and Rmin
- **Objective**: Visualize maximum and minimum values of selected meteorological variables.
- **Method**:  
  Calculated `Rmax` and `Rmin` from the dataset and plotted using Cartopy.
- **Observations**:  
  Displayed spatial extremes in the dataset.

## How to Run the Scripts

1. Ensure all NetCDF files are placed in a directory named `data` within the same directory as the scripts.
2. Open the integrated terminal in Visual Studio Code.
3. Run the main script using the command:
   ```bash
   python scivis.py

4. The scripts will generate images and save them in their respective directories. Animation GIFs are also created to visualize changes over time.

## Requirements

- **Python**: 3.x  
- **Dependencies**: Listed in `requirements.txt`
