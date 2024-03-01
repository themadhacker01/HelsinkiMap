import os as os
import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox

from shapely.geometry import box

# Read data from geojson file into a geo dataframe
map_data = gpd.read_file('data/buildings.geojson')

# View data types, values and stats of the geo dataframe
# print(map_data.info(), map_data.head(), map_data.describe())

# Visualise the map_data using matplotlib
# map_data.plot()
# plt.show()

# Checking if the folder in the desired path exists
# shp_path = 'data/shp_files'
# if not os.path.exists(shp_path):
    # If they don't exist create the folder
    # os.makedirs(shp_path)

# Writing the map_data to a shapely file
# map_data.to_file(shp_path + '/buildings_copy.shp')

# Bounding box for a given area (Helsinki city center)
bounds = [24.9351773, 60.1641551, 24.9534055, 60.1791068]

# Create a bounding box polygon
bbox = box(*bounds)

# Retrieve building from the given area
buildings = ox.features_from_polygon(bbox, tags={'building': True})
# print(buildings.head())

# Count the number of buildings returned
# print(len(buildings))

# Plot the retrieved data
# buildings.plot()
# plt.show()

# Find the coordinate reference system CRS
# print(buildings.crs)

# Project the CRS of buildings to EPSG:3067
projected = buildings.to_crs(epsg=3067)

# Compare the geometries of the 2 CRS
orig_geom = buildings.iloc[3]['geometry']
proj_geom = projected.iloc[3]['geometry']

# Coordinates have changed from degrees to meters
# print('Original : ', orig_geom, '\n\nProjected : ', proj_geom)

# Get the OSM data for restaurants in Helsinki
restaurants_place = ox.features_from_place('Helsinki, Finland', tags={'amenity': ['restaurant', 'pub', 'bar']})
buildings_place = ox.features_from_place('Helsinki, Finland', tags={'building': True})

# Based on the same location, amenities get plotted on top of buildings
buildings_place.plot()
plt.show()
