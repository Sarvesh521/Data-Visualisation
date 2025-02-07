import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import imageio

# fm1000 = nc.Dataset(r'GridMet\fm1000_2001.nc') # to check the metadata of the file

fm1000 = xr.open_dataset(r'GridMet\fm1000_2001.nc')

fm1000 = fm1000.sel(day=slice('2001-01-01T00:00:00.000', '2001-03-31T00:00:00.000'))

lon = fm1000['lon']
lat = fm1000['lat']
days = fm1000['day']

plot_dir = 'dead_fuel_moisture_1000hr_plots_cartopy'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

projection = ccrs.PlateCarree()

for day in range(0, len(days), 10):
    date = str(days[day].values)[:10]

    fuel_moisture_day = fm1000['dead_fuel_moisture_1000hr'].sel(day=days[day])

    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': projection})

    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAND, facecolor='white')
    ax.add_feature(cfeature.STATES, linestyle=':')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    
    # Create contour plot
    contour = ax.contourf(lon, lat, fuel_moisture_day, 
                          levels=20, cmap='viridis', 
                          transform=ccrs.PlateCarree())
    
    # Add colorbar
    cbar = plt.colorbar(contour, ax=ax, orientation='vertical', pad=0.02, shrink=0.7)
    cbar.set_label("Dead Fuel Moisture (1000 hr) (%)")
    
    # Add title
    ax.set_title(f"Dead Fuel Moisture (1000 hr) - {date}", fontsize=14)
    
    # Save the plot
    plot_path = os.path.join(plot_dir, f"dead_fuel_moisture_1000hr_{date}.png")
    plt.savefig(plot_path, bbox_inches='tight')

print("Contour plots with Cartopy saved successfully!")

images = []

image_dir = 'dead_fuel_moisture_1000hr_plots_cartopy'

# Get a sorted list of file paths to ensure correct order in GIF
images = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')])
n_frames=len(images)

# Create a GIF
with imageio.get_writer('dead_fuel_moisture_1000hr_animation.gif', mode='I', duration=n_frames*100) as writer:
    for filename in images:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")