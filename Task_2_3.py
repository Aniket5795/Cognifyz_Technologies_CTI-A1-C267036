import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from shapely.geometry import Point

#---------LOAD DATASET----------
df = pd.read_csv("Dataset.csv")

#------DROP ROWS WITH MISSING LATITUDE AND LONGITUDE-------
df_location = df.dropna(subset=['Latitude', 'Longitude'])

#----------PLOTTING RESTAURANT LOCATIONS ON WORLD MAP-----------
lat = df_location['Latitude']
lon = df_location['Longitude']

geometry = [Point(xy) for xy in zip(lon, lat)]

gdf = gpd.GeoDataFrame({'latitude': lat, 'longitude': lon}, geometry=geometry, crs="EPSG:4326")

fig = plt.figure(figsize=(50, 30))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()

ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

gdf.plot(ax=ax, color='red', markersize=8, transform=ccrs.PlateCarree())

ax.set_title("Restaurant Locations on World Map")
plt.show()