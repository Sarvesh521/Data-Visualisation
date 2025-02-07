import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import imageio

# tmmn = nc.Dataset(r'GridMet\tmmn_2001.nc') # to check the metadata of the file

tmmn = xr.open_dataset(r'GridMet\tmmn_2001.nc')

tmmn = tmmn.sel(day=slice('2001-01-01T00:00:00.000', '2001-03-31T00:00:00.000'))

lon = tmmn['lon']
lat = tmmn['lat']
days = tmmn['day']

plot_dir = 'min_near_surface_air_temperature_plots_cartopy'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

projection = ccrs.PlateCarree()

for day in range(0, len(days), 10):
    date = str(days[day].values)[:10] 
    
    min_near_surface_air_temperature_day = tmmn['air_temperature'].sel(day=days[day])
    
    # Create the figure and axis with Cartopy projection
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': projection})
    
    # Add coastlines and other geographic features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES, linestyle=':')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    
    # Create contour plot
    contour = ax.contourf(lon, lat, min_near_surface_air_temperature_day, 
                          levels=20, cmap='coolwarm', 
                          transform=ccrs.PlateCarree())
    
    # Add colorbar
    cbar = plt.colorbar(contour, ax=ax, orientation='vertical', pad=0.02, shrink=0.7)
    cbar.set_label("Min Near Surface Air Temperature (K)")
    
    # Add title
    ax.set_title(f"Min Near Surface Air Temperature - {date}", fontsize=14)
    
    # Save the plot
    plot_path = os.path.join(plot_dir, f"min_near_surface_air_temperature_{date}.png")
    plt.savefig(plot_path, bbox_inches='tight')

print("Contour plots with Cartopy saved successfully!")

images = []

image_dir = 'min_near_surface_air_temperature_plots_cartopy'

# Get a sorted list of file paths to ensure correct order in GIF
images = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')])
n_frames=len(images)

# Create a GIF
with imageio.get_writer('min_near_surface_air_temperature_animation.gif', mode='I', duration=n_frames*100) as writer:
    for filename in images:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")