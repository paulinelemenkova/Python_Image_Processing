python3.10 -m pip install earthpy

/usr/local/bin/python3.10 -m pip install --upgrade pip
python3.10 -m pip install plotly==5.10.0

python3.10

# Set the home directory
import os
os.chdir('/Users/polinalemenkova/Documents/Python/Image_Processing')
os. getcwd()
dtm = "n06_w007_3arc_v2.tif"

from glob import glob
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go
np.seterr(divide='ignore', invalid='ignore')

# 1. --------------- Plotting Digital Elevation Model (DEM) ----------------#
# Open the DEM with Rasterio
with rio.open(dtm) as src:
    elevation = src.read(1)
# Set masked values to np.nan (in case of bathimetry <0)
#    elevation[elevation < 0] = np.nan

# Plot the data
ep.plot_bands(
    elevation,
    cmap="gist_earth",
    title="Ditigal Terrain Model (DTM)",
    figsize=(10, 6),
)
plt.show()


# 2.---------------- Create the Hillshade ----------------#
hillshade = es.hillshade(elevation)

ep.plot_bands(
    hillshade,
    cbar=False,
    title="Hillshade made from DTM",
    figsize=(10, 6),
)
plt.show()

# 3.---------------- Changing the Azimuth of the Sun of the hillshade layer ----------------#
# Changing the Azimuth of the Sun of the hillshade layer to 210 degrees
hillshade_azimuth_210 = es.hillshade(elevation, azimuth=210)
# Plotting the hillshade layer with the modified azimuth
ep.plot_bands(
    hillshade_azimuth_210,
    cbar=False,
    title="Hillshade with Azimuth set to 210 Degrees",
    figsize=(10, 6),
)
plt.show()

# 4.---------------- Change the Angle Altitude of the Sun ----------------#
# Adjust the azimuth value
hillshade_angle_10 = es.hillshade(elevation, altitude=10)

# Plot the hillshade layer with the modified angle altitude
ep.plot_bands(
    hillshade_angle_10,
    cbar=False,
    title="Hillshade with Angle Altitude set to 10 Degrees",
    figsize=(10, 6),
)
plt.show()

# 5.---------------- Overlay a DEM on top of the Hillshade ----------------#
# Plot the DEM and hillshade at the same time
# sphinx_gallery_thumbnail_number = 5
fig, ax = plt.subplots(figsize=(10, 6))
ep.plot_bands(
    elevation,
    ax=ax,
    cmap="terrain",
    title="LiDAR DEM of \n overlayed on top of a hillshade",
)
ax.imshow(hillshade, cmap="Greys", alpha=0.5)
plt.show()
