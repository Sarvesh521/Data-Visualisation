import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import netCDF4 as nc
import datetime
import imageio.v2 as imageio
import os
import glob
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import ListedColormap

def precip():
    print('Creating precipitation images and gif..')
    if not os.path.exists('images/precipitation'):
        os.makedirs('images/precipitation')
    data = nc.Dataset('data/pr_2001.nc', 'r')
    cmap = plt.get_cmap('viridis', 1024)

    lon = data['lon'][:]
    lat = data['lat'][:]
    prp = data['precipitation_amount'][:]


    for i in range(0,90,9):
        plt.figure(figsize=(12, 7))
        plt.pcolormesh(lon, lat, prp[i], cmap=cmap)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.colorbar()

        plt.title(date + '\nPrecipitation')

        plt.savefig('images/precipitation/precipitation_' + date + '.png')

        plt.close()

    images = []
    filenames = glob.glob('images/precipitation/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/precipitation/precipitation.gif', images, fps=2)

    data.close()

def precip_log():
    print('Creating precipitation log images and gif...')
    if not os.path.exists('images/precipitation_log'):
        os.makedirs('images/precipitation_log')
    data = nc.Dataset('data/pr_2001.nc', 'r')
    cmap = plt.get_cmap('viridis', 1024)

    lon = data['lon'][:]
    lat = data['lat'][:]
    prp = data['precipitation_amount'][:]
    prp = prp + 0.1
    temp = prp[:90]
    min_val = np.min(temp)
    max_val = np.max(temp)

    for i in range(0,90,9):
        plt.figure(figsize=(12, 7))
        plt.pcolormesh(lon, lat, prp[i], cmap=cmap, norm=matplotlib.colors.LogNorm(vmax=max_val, vmin=min_val))
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.colorbar()

        plt.title(date + '\nPrecipitation')

        plt.savefig('images/precipitation_log/precipitation_' + date + '.png')

        plt.close()

    images = []
    filenames = glob.glob('images/precipitation_log/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/precipitation_log/precipitation_log.gif', images, fps=2)

    data.close()

def vpd():
    print('Creating vapor pressure deficit images..')
    if not os.path.exists('images/vpd'):
        os.makedirs('images/vpd')

    data = nc.Dataset('data/vpd_2001.nc', 'r')
    cmap = plt.get_cmap('viridis', 1024)

    lon = data['lon'][:]
    lat = data['lat'][:]
    vpd = data['mean_vapor_pressure_deficit'][:]
    for i in range(0, 90, 9):
        plt.figure(figsize=(10, 10))
        plt.pcolormesh(lon, lat, vpd[i], cmap=cmap)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        #plt.ylim(20, 55)

        divider = make_axes_locatable(plt.gca())
        axBar = divider.append_axes("top", size="5%", pad='7%')
        axHist = divider.append_axes("top", '30%', pad='7%')

        cbar = plt.colorbar(cax=axBar, orientation='horizontal')
        axHist.hist(vpd[i].flatten(), bins=50)
        axHist.margins(x=0)

        plt.title(date + '\nVapor Pressure Deficit')
        plt.savefig('images/vpd/vpd_' + date + '.png')
        plt.close()

    data.close()
    images = []
    filenames = glob.glob('images/vpd/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/vpd/vpd.gif', images, fps=2)

def vpd_extreme_local():
    print('Creating vapor pressure deficit images with extreme values and local cmap..')
    if not os.path.exists('images/vpd_extreme_local'):
        os.makedirs('images/vpd_extreme_local')

    data = nc.Dataset('data/vpd_2001.nc', 'r')

    lon = data['lon'][:]
    lat = data['lat'][:]
    vpd = data['mean_vapor_pressure_deficit'][:]

    for i in range(0,90,9):
        temp = vpd[i]
        plt.figure(figsize=(10, 10))

        #find extreme values to change the colorbar
        #calculate q1 and q3 not including 32767.0 (mask value)
        temp = np.array(temp)
        temp = temp[temp != 32767.0]
        q1 = np.percentile(temp, 5)
        q3 = np.percentile(temp, 95)

        min_val = np.min(temp)
        max_val = np.max(temp)
        q1_scaled = (q1 - min_val) / (max_val - min_val)
        q3_scaled = (q3 - min_val) / (max_val - min_val)

        q1_scaled = int(q1_scaled * 256)
        q3_scaled = int(q3_scaled * 256)

        col_map = matplotlib.colormaps['Reds'].resampled(256)
        c1 = col_map(75)
        c1_n = col_map(125)
        c3_n = col_map(200)
        c3 = col_map(250)
        newcolors = col_map(np.linspace(0, 1, 256))
        newcolors[:q1_scaled] = c1
        newcolors[q1_scaled:q3_scaled] = np.linspace(c1_n, c3_n, q3_scaled - q1_scaled)
        newcolors[q3_scaled:] = c3

        newcmp = ListedColormap(newcolors)

        plt.pcolormesh(lon, lat, vpd[i], cmap=newcmp)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        divider = make_axes_locatable(plt.gca())
        axBar = divider.append_axes("top", size="5%", pad='7%')
        axHist = divider.append_axes("top", '30%', pad='7%')

        cbar = plt.colorbar(cax=axBar, orientation='horizontal')
        axHist.hist(vpd[i].flatten(), bins=50)
        axHist.margins(x=0)

        plt.title(date + '\nVapor Pressure Deficit')
        plt.savefig('images/vpd_extreme_local/vpd_' + date + '.png')
        plt.close()
    images = []
    filenames = glob.glob('images/vpd_extreme_local/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/vpd_extreme_local/vpd_extreme_local.gif', images, fps=2)

    data.close()

def vpd_extreme_global():
    print('Creating vapor pressure deficit images with extreme values and global cmap..')
    if not os.path.exists('images/vpd_extreme_global'):
        os.makedirs('images/vpd_extreme_global')

    data = nc.Dataset('data/vpd_2001.nc', 'r')

    lon = data['lon'][:]
    lat = data['lat'][:]
    vpd = data['mean_vapor_pressure_deficit'][:]
    vpd1  = vpd[:90]
    temp = vpd1.flatten()
    #find extreme values to change the colorbar
    #calculate q1 and q3 not including 32767.0 (mask value)
    temp = np.array(temp)
    temp = temp[temp != 32767.0]
    q1 = np.percentile(temp, 5)
    q3 = np.percentile(temp, 95)

    min_val = np.min(temp)
    max_val = np.max(temp)
    q1_scaled = (q1 - min_val) / (max_val - min_val)
    q3_scaled = (q3 - min_val) / (max_val - min_val)

    q1_scaled = int(q1_scaled * 256)
    q3_scaled = int(q3_scaled * 256)

    col_map = matplotlib.colormaps['Reds'].resampled(256)
    c1 = col_map(75)
    c1_n = col_map(125)
    c3_n = col_map(200)
    c3 = col_map(250)
    newcolors = col_map(np.linspace(0, 1, 256))
    newcolors[:q1_scaled] = c1
    newcolors[q1_scaled:q3_scaled] = np.linspace(c1_n, c3_n, q3_scaled - q1_scaled)
    newcolors[q3_scaled:] = c3

    newcmp = ListedColormap(newcolors)
    for i in range(0,90,9):
        plt.figure(figsize=(10, 10))

        plt.pcolormesh(lon, lat, vpd[i], cmap=newcmp, vmin=min_val, vmax=max_val)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        divider = make_axes_locatable(plt.gca())
        axBar = divider.append_axes("top", size="5%", pad='7%')
        axHist = divider.append_axes("top", '30%', pad='7%')

        cbar = plt.colorbar(cax=axBar, orientation='horizontal')
        axHist.hist(vpd[i].flatten(), bins=50, range=(min_val, max_val))
        axHist.margins(x=0)

        plt.title(date + '\nVapor Pressure Deficit')
        plt.savefig('images/vpd_extreme_global/vpd_' + date + '.png')
        plt.close()

    images = []
    filenames = glob.glob('images/vpd_extreme_global/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/vpd_extreme_global/vpd_extreme_global.gif', images, fps=2)

    data.close()

def rmax():
    print('Creating max relative humidity images..')
    if not os.path.exists('images/rmax'):
        os.makedirs('images/rmax')

    data = nc.Dataset('data/rmax_2001.nc', 'r')

    cmap = plt.get_cmap('viridis', 1024)

    lon = data['lon'][:]
    lat = data['lat'][:]
    rm = data['relative_humidity'][:]

    min_val = np.min(rm[:90])
    max_val = np.max(rm[:90])

    for i in range(0, 90, 9):
        plt.figure(figsize=(10, 10))
        newcolors = cmap(np.linspace(0, 1, 256))
        newcolors[-1] = [0, 0, 0, 1]

        cmap = ListedColormap(newcolors)

        plt.pcolormesh(lon, lat, rm[i], cmap=cmap, vmin=min_val, vmax=max_val)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        #plt.ylim(20, 55)

        divider = make_axes_locatable(plt.gca())
        axBar = divider.append_axes("top", size="5%", pad='7%')
        axHist = divider.append_axes("top", '30%', pad='7%')

        cbar = plt.colorbar(cax=axBar, orientation='horizontal')
        axHist.hist(rm[i].flatten(), bins=50, range=(min_val, max_val))
        axHist.margins(x=0)

        plt.title(date + '\nMax Relative Humidity')
        plt.savefig('images/rmax/rmax_' + date + '.png')
        plt.close()
    images = []
    filenames = glob.glob('images/rmax/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/rmax/rmax.gif', images, fps=2)

def rmin():
    print('Creating min relative humidity images..')
    if not os.path.exists('images/rmin'):
        os.makedirs('images/rmin')
    data = nc.Dataset('data/rmin_2001.nc', 'r')
    cmap = plt.get_cmap('RdBu', 1024)

    lon = data['lon'][:]
    lat = data['lat'][:]
    rm = data['relative_humidity'][:]

    min_val = np.min(rm[:90])
    max_val = np.max(rm[:90])

    for i in range(0,90,9):
        plt.figure(figsize=(10, 10))
        plt.pcolormesh(lon, lat, rm[i], cmap=cmap, vmin=min_val, vmax=max_val)
        date = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=int(data['day'][i]))
        date = date.strftime('%Y-%m-%d')

        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        #plt.ylim(20, 55)

        divider = make_axes_locatable(plt.gca())
        axBar = divider.append_axes("top", size="5%", pad='7%')
        axHist = divider.append_axes("top", '30%', pad='7%')

        cbar = plt.colorbar(cax=axBar, orientation='horizontal')
        axHist.hist(rm[i].flatten(), bins=50, range=(min_val, max_val))
        axHist.margins(x=0)

        plt.title(date + '\nMin Relative Humidity')
        plt.savefig('images/rmin/rmin_' + date + '.png')
        plt.close()
    images = []
    filenames = glob.glob('images/rmin/*.png')
    filenames.sort()
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('images/rmin/rmin.gif', images, fps=2)




if not os.path.exists('images'):
    os.makedirs('images')

precip()
precip_log()
vpd()
vpd_extreme_local()
vpd_extreme_global()
rmax()
rmin()
