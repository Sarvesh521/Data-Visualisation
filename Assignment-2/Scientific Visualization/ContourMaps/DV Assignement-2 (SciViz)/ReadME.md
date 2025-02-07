# Scientific Visualization of gridMET Dataset

## Introduction
This project focuses on the scientific visualization of the gridMET dataset for the first quarter of 2001. The aim is to analyze and visualize various meteorological variables to understand climatic patterns and changes over this period. The visualizations help in interpreting the spatial and temporal variations of different atmospheric parameters across the United States.

## Dataset
The dataset used is the gridMET dataset, which provides high-resolution gridded surface meteorological data. The time frame selected for this project is from January 1, 2001, to March 31, 2001. The specific dates chosen for generating plots are:
- 1st January 2001
- 11th January 2001
- 21st January 2001
- 31st January 2001
- 10th February 2001
- 20th February 2001
- 2nd March 2001
- 12th March 2001
- 22nd March 2001

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

> **Note**: Installing Cartopy may require additional dependencies. It's recommended to follow Cartopy's official installation instructions if you encounter issues.

## Project Structure

### Data Files
NetCDF (.nc) files for different meteorological variables:
Add them inside GridMet folder
- `https://www.northwestknowledge.net/metdata/data/tmmx_2001.nc`: Maximum near-surface air temperature.
- `https://www.northwestknowledge.net/metdata/data/tmmn_2001.nc`: Minimum near-surface air temperature.
- `https://www.northwestknowledge.net/metdata/data/pet_2001.nc`: Grass reference evapotranspiration.
- `https://www.northwestknowledge.net/metdata/data/fm1000_2001.nc`: 1000-hour dead fuel moisture.

### Python Scripts
Separate scripts for each visualization task:
- `contour_max_near_surface_air_temperature.py`
- `contourfill_max_near_surface_air_temperature.py`
- `contourfill_min_near_surface_air_temperature.py`
- `contourfill_temperature_range.py`
- `contourfill_grass_evapotranspiration.py`
- `contourfill_fuel_moisture_1000hr.py`

### Output Directories
Each script generates a directory containing the plotted images and an animation GIF:
- `max_near_surface_air_temperature_plots_cartopy`
- `max_near_surface_air_temperature_plots_cartopy_contour`
- `min_near_surface_air_temperature_plots_cartopy`
- `temperature_range_plots_cartopy`
- `grass_evapotranspiration_plots_cartopy`
- `dead_fuel_moisture_1000hr_plots_cartopy`

## Visualizations

### 1. Max Near Surface Air Temperature
- **Objective**: Visualize the spatial distribution of maximum near-surface air temperatures over the selected dates.
- **Method**: Loaded the `tmmx_2001.nc` file using xarray. Selected the data for the specified dates and plotted contour maps using Cartopy with appropriate color schemes.
- **Observations**: Notable temperature gradients from north to south with a progressive warming trend from January to March.

### 2. Min Near Surface Air Temperature
- **Objective**: Illustrate the minimum near-surface air temperatures across the US.
- **Method**: Used the `tmmn_2001.nc` dataset to generate contour plots similar to the maximum temperature but focusing on minimum values.
- **Observations**: Cooler temperatures are prevalent in northern regions, and nighttime temperatures show significant variations, especially in arid regions.

### 3. Diurnal Temperature Range
- **Objective**: Depict the difference between maximum and minimum temperatures to understand diurnal variations.
- **Method**: Calculated the temperature range by subtracting minimum temperatures from maximum temperatures. Visualized using contour plots with a vibrant color map to highlight differences.
- **Observations**: Higher diurnal ranges in desert and arid areas due to low humidity, with smaller ranges in coastal regions.

### 4. Grass Reference Evapotranspiration
- **Objective**: Visualize the potential evapotranspiration rates as a measure of atmospheric demand for water.
- **Method**: Processed the `pet_2001.nc` file and plotted the data using a sequential color map.

### 5. 1000-hour Dead Fuel Moisture
- **Objective**: Map the moisture content in large dead fuels which is crucial for understanding wildfire risks.
- **Method**: Utilized the `fm1000_2001.nc` dataset and displayed the moisture levels using contour maps with appropriate legends.

## How to Run the Scripts
1. Ensure all the NetCDF files are placed in a directory named `GridMet` within the same directory as the scripts.
2. Run each script individually using the command:
   ```bash
   python script_name.py

Replace `script_name.py` with the actual script you want to run.

The scripts will generate images and save them in their respective directories. Animation GIFs are also created to visualize changes over time.

## Results
- The generated plots provide visual insights into various meteorological parameters.
- The animations effectively showcase temporal changes across the selected dates.
- The observations align with expected climatic patterns for the given time of year.

## Conclusion
This project successfully demonstrates the use of Python libraries for scientific visualization of meteorological data. By analyzing the gridMET dataset, valuable insights into climatic trends and variations during the first quarter of 2001 were obtained. The visualizations aid in understanding the spatial distribution and temporal progression of key atmospheric variables.

## Acknowledgements
- **gridMET Dataset**: Provided by the University of Idaho.
- **Python Community**: For the development of powerful libraries that make data analysis accessible.

## References
- [gridMET Data Documentation](https://www.climatologylab.org/gridmet.html)
- [Cartopy Documentation](https://scitools.org.uk/cartopy/docs/latest/)