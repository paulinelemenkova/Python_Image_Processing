# python3.10 -m pip install earthpy
# /usr/local/bin/python3.10 -m pip install --upgrade pip
# python3.10 -m pip install plotly==5.10.0

python3.10

# Set the home directory
import os
os.chdir('/Users/polinalemenkova/Documents/Python/Image_Processing')
os. getcwd()

from glob import glob
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
from rasterio.plot import plotting_extent
import geopandas as gpd

# 1. --- Plotting a stack from all of the 7 Landsat.tif files (one per band). This creates a numpy array with each "layer" representing a single band. Nodata = parameter to mask nodata values
landsat_path = glob("/Users/polinalemenkova/Documents/Python/Image_Processing/LC08_L1TP_197055_20151218_20170331_01_T1/*B?*.TIF")
landsat_path
# sort bands by ascending band number
landsat_path.sort()

# 2. --- Combine 7 Landsat bands in one plot for plotting (create image stack and apply nodata values)
array_stack, meta_data = es.stack(landsat_path, nodata=-9999)
arr_st, meta = es.stack(landsat_path, nodata=-9999)

titles = ["Ultra Blue", "Blue", "Green", "Red", "NIR", "SWIR 1", "SWIR 2", "Cirrus", "TIRS 1", "TIRS 2"]
# sphinx_gallery_thumbnail_number = 1
ep.plot_bands(array_stack, title=titles, cmap = 'gist_earth', cols = 5, figsize = (20, 12))
ep.plot_bands(array_stack, title=titles, cols = 5, figsize = (20, 12))
#plt.show()

# 3. --- merged all bands in one stack (create a figure with one plot)
ep.plot_bands(array_stack[4], cbar=False, cmap = 'plasma')
#plt.show()

#----- 4. --- Plot RGB combinations of raster bands using EarthPy
# Create image stack and apply nodata value for Landsat
array_stack, meta_data = es.stack(landsat_path, nodata=-9999)
arr_st, meta = es.stack(landsat_path)

landsat_bands_data_path = glob("/Users/polinalemenkova/Documents/Python/Image_Processing/LC08_L1TP_197055_20151218_20170331_01_T1_RGB/*B?*.TIF")
landsat_bands_data_path
stack_band_paths = glob("/Users/polinalemenkova/Documents/Python/Image_Processing/LC08_L1TP_197055_20151218_20170331_01_T1_RGB/*B?*.TIF")
stack_band_paths.sort()

# Create image stack and apply nodata value for Landsat
#arr_st, meta = es.stack(stack_band_paths, nodata=-9999)
arr_st, meta = es.stack(stack_band_paths)

# Create figure with one plot
fig, ax = plt.subplots(figsize=(12, 12))

# Plot Plot RGB Composite Image: red, green, and blue bands
ep.plot_rgb(arr_st, rgb=(3, 2, 1), stretch=False, ax=ax, title="Landsat 8 RGB Image, bands 3-2-1 \n(True Color Composite)")
plt.show()

ep.plot_rgb(arr_st, rgb=(4, 3, 2), stretch=False, title="Landsat 8 RGB Image, bands 4-3-2 \n(False Color Composite)")
plt.show()
ep.plot_rgb(
    arr_st,
    rgb=(4, 3, 2),
    ax=ax,
    stretch=True,
    title="Landsat 8 CIR Image with Polygon Boundary",
)

plt.show()

ep.plot_rgb(array_stack, rgb=(7, 5, 1), ax=ax, title="Landsat 8 RGB Image, bands 7-5-1")
plt.show()
