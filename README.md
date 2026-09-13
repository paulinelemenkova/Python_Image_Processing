# Python Raster & Satellite Image Processing with EarthPy

Python scripts for raster and satellite image processing built on the EarthPy library together with rasterio, geopandas, matplotlib and Plotly. They demonstrate reusable earth-observation workflows on example elevation and Landsat data: hillshading and 3D visualisation of a digital elevation model, stacking and plotting multispectral bands, building RGB colour composites, and computing band histograms.

## Scripts

- `Python-earthpy.py` — EarthPy setup, DEM hillshade and an interactive 3D surface (Plotly) of an SRTM elevation tile
- `Python-earthpy_DEM.py` — reading and visualising a digital elevation model — hillshade, colour relief and terrain plots
- `Python-earthpy_bands.py` — stacking and plotting Landsat multispectral bands and RGB composites (earthpy, rasterio)
- `Python-earthpy_histograms.py` — histograms of Landsat spectral bands with earthpy.plot

## Data

The scripts use example raster data — an SRTM 3-arc-second DEM tile (`n06_w007_3arc_v2.tif`) and a Landsat scene (`Landsat.tif`). Adjust the input paths and the `os.chdir` at the top of each script to your own data directory.

## Requirements

Python 3 with `earthpy`, `rasterio`, `geopandas`, `numpy`, `matplotlib` and `plotly`.

## Author

Polina Lemenkova — ORCID: https://orcid.org/0000-0002-5759-1089

## License

MIT — see the LICENSE file (Copyright Polina Lemenkova).
