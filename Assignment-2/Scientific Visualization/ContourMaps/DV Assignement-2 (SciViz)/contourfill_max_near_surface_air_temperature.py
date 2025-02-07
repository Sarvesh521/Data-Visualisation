import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import imageio

# tmmx = nc.Dataset(r'GridMet\tmmx_2001.nc') # to check the metadata of the file

tmmx = xr.open_dataset(r'GridMet\tmmx_2001.nc')

tmmx = tmmx.sel(day=slice('2001-01-01T00:00:00.000', '2001-03-31T00:00:00.000'))

lon = tmmx['lon']
lat = tmmx['lat']
days = tmmx['day']

plot_dir = 'max_near_surface_air_temperature_plots_cartopy'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

projection = ccrs.PlateCarree()

for day in range(0, len(days), 10):
    date = str(days[day].values)[:10] 
    
    max_near_surface_air_temperature_day = tmmx['air_temperature'].sel(day=days[day])
    
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': projection})
    
    # Add coastlines and other geographic features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAND, facecolor='white')
    ax.add_feature(cfeature.STATES, linestyle=':')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    
    # Create contour plot
    contour = ax.contourf(lon, lat, max_near_surface_air_temperature_day, 
                          levels=20, cmap='coolwarm', 
                          transform=ccrs.PlateCarree())
    
    # Add colorbar
    cbar = plt.colorbar(contour, ax=ax, orientation='vertical', pad=0.02, shrink=0.7)
    cbar.set_label("Max Near Surface Air Temperature (K)")
    
    # Add title
    ax.set_title(f"Max Near Surface Air Temperature - {date}", fontsize=14)
    
    # Save the plot
    plot_path = os.path.join(plot_dir, f"max_near_surface_air_temperature_{date}.png")
    plt.savefig(plot_path, bbox_inches='tight')

print("Contour plots with Cartopy saved successfully!")

images = []

image_dir = 'max_near_surface_air_temperature_plots_cartopy'

# Get a sorted list of file paths to ensure correct order in GIF
images = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')])
n_frames=len(images)

# Create a GIF
with imageio.get_writer('max_near_surface_air_temperature_animation.gif', mode='I', duration=n_frames*100) as writer:
    for filename in images:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")