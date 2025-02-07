import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import Normalize
import matplotlib.cm as cm

th_path = '../data/th_2001.nc'
vs_path = '../data/vs_2001.nc'

SKIP = 20

VMIN=0
VMAX=15
OUTPUT_PATH = "../outputs/constant_length_colored_speed_scale_height1.gif"

# Function to convert wind speed and direction to u and v vector components
def wind_components(speed, direction):
    rad = np.deg2rad(direction)
    u = speed * np.cos(rad)
    v = speed * np.sin(rad)
    return u, v

# Function to update quiver for each frame in the animation
def update_quiver(day_idx):
    ax.set_title(f"Wind Vectors on {np.datetime_as_string(dates[selected_indices[day_idx]], unit='D')}")
    
    # Get the current day's wind speed and direction data, downsampled
    speed = wind_speed[selected_indices[day_idx]][::SKIP, ::SKIP]
    direction = wind_direction[selected_indices[day_idx]][::SKIP, ::SKIP]
    u, v = wind_components(speed, direction)
    
    # Normalize u and u components to have constant length
    magnitude = np.sqrt(u**2 + v**2)
    u_normalized = u / magnitude   #remove normalization to get varying legth vectors
    v_normalized = v / magnitude
    
    # Update quiver plot with normalized u, v components and color-coded by speed
    qv.set_UVC(u_normalized, v_normalized)
    qv.set_array(speed.values.ravel())  # Color by speed values
    
    return qv,

# Open the netCDF files
th_data = xr.open_dataset(th_path)
vs_data = xr.open_dataset(vs_path)

# Extract necessary data
lat = th_data['lat'].values
lon = th_data['lon'].values
dates = th_data['day'].values
wind_direction = th_data['wind_from_direction']
wind_speed = vs_data['wind_speed']

#select dates to plot
selected_days = [
    np.datetime64(f'2001-01-{day:02d}') for day in [10, 20, 30]
] + [
    np.datetime64(f'2001-02-{day:02d}') for day in [10, 20, 28]
] + [
    np.datetime64(f'2001-03-{day:02d}') for day in [10, 20, 28]
]
selected_indices = [np.where(dates == day)[0][0] for day in selected_days]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
ax.set_extent([-125, -67, 25, 50])  # Extent covering the US

# Set color normalization based on the expected range of wind speed
norm = Normalize(vmin=wind_speed.min().values, vmax=wind_speed.max().values)
cmap = cm.viridis

# Downsample grid for plotting
lon_ds = lon[::SKIP]
lat_ds = lat[::SKIP]
lon_grid, lat_grid = np.meshgrid(lon_ds, lat_ds)

# Use the first selected day's data to initialize the quiver plot with constant length arrows
speed_initial = wind_speed[selected_indices[0]][::SKIP, ::SKIP]
direction_initial = wind_direction[selected_indices[0]][::SKIP, ::SKIP]
u_initial, v_initial = wind_components(speed_initial, direction_initial)

# Normalize U and V for constant length arrows
magnitude_initial = np.sqrt(u_initial**2 + v_initial**2)   #remove normalization to get veried length vectors
u_normalized_initial = u_initial / magnitude_initial
v_normalized_initial = v_initial / magnitude_initial

# Plot quiver with constant arrow length and color-coded by speed
qv = ax.quiver(
    lon_grid, lat_grid, u_initial, v_initial, speed_initial.values.ravel(),
    scale=60, cmap='viridis', clim=(VMIN, VMAX), transform=ccrs.PlateCarree()
)

# Create color bar for the speed
cbar = plt.colorbar(qv, ax=ax, orientation='vertical', pad=0.02, fraction=0.046, shrink=0.8)
cbar.set_label("Wind Speed (m/s)")
qv.set_clim(VMIN, VMAX)

# Create the animation with only the selected days
anim = FuncAnimation(fig, update_quiver, frames=len(selected_indices), interval=500, blit=True)

# Save the animation as a GIF
anim.save(OUTPUT_PATH, writer=PillowWriter(fps=2))
