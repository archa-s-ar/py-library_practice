import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#Creating a GeoDataFrames
data={
    "City":['Tokyo','New York','London','Paris'],
    "Latitude":[35.6895, 40.7128, 51.5074, 48.8566],
    "Longitude": [139.6917, -74.0060, -0.1278, 2.3522],
}
df=pd.DataFrame(data)
print("Using Pandas:\n",df)
gdf=gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude,df.Latitude)) #A GeoDataFrame is a tabular data structure that contains a *geometry* column, which holds the geometric shapes. Fom the file, selecting one column as x, other as y. df.Latitude is same as df["Latitude"]
print("Using GeoPandas:\n",gdf)
#in df, geometry is hidden

#******Reading and Writing Geospatial Data*******

#GeoPandas allows reading and writing a variety of geospatial formats, such as Shapefiles, GeoJSON, and more
print(gdf.columns)
url="https://github.com/opengeos/datasets/releases/download/vector/nybb.geojson"
#if file path, r"filepath"
gdf= gpd.read_file(url)
print(gdf.head())

#Writing to a GeoJSON File
out_file="nyc_boroughs.geojson"
gdf.to_file(out_file, driver="GeoJSON")
print("GeoDataFrame has been writing to ", out_file) #GeoDataFrame has been written to nyc_boroughs.geojson

#Similarly, you can write GeoDataFrames to other formats, such as Shapefiles, GeoPackage, and more.
output_file = "nyc_boroughs.shp"
gdf.to_file(output_file)

output_file = "nyc_boroughs.gpkg" #geopackage
gdf.to_file(output_file, driver="GPKG")

#******Simple Accessors and Methods****
#Measuring Area
gdf=gdf.set_index('BoroName') #It makes a column BoroName as the index of the DataFrame.
print("After indexing:\n",gdf)

#Calculate area
gdf['area']=gdf.area #to create a new coloumn for area
print('Area:\n',gdf)

#****Getting Polygon Boundaries and Centroids****

# Get the boundary of each polygon
gdf["boundary"] = gdf.boundary

# Get the centroid of each polygon
gdf["centroid"] = gdf.centroid

#gdf=gdf[["boundary", "centroid"]]
#print('New gdf=',gdf) #remove all other columns

#*****FILTERING*****
print(gdf.loc['Manhattan']) ## Select the record whose index is 'Manhattan'
#print(gdf.loc['Manhattan','geometry']) # Get the geometry of Manhattan

# Calculate the distance from each centroid to Manhattan's centroid
manhattan_centroid=gdf.loc['Manhattan','centroid']
gdf["distance_to_manhattan"] = gdf["centroid"].distance(manhattan_centroid)
print(gdf[["centroid", "distance_to_manhattan"]]) #gdf still contains all the columns. But prints only centroid, distance_to_manhattan. 

#****MEAN OF A COLUMN******
mean_dist=gdf['distance_to_manhattan'].mean()
print("Mean distance to Manhattan= ",mean_dist," units")

#gdf.drop(columns=["boundary","centroid"],inplace=True) #GeoJSON, Shapefiles, and many GIS formats are designed to have one active geometry column.
#gdf.to_file("nyc_dst.geojson")

#*****Plotting Geospatial Data*******
#GeoPandas integrates with Matplotlib

gdf.plot()

gdf.plot("area", # column used for coloring
         legend=True, # show color scale legend
           figsize=(10,6)) # figure size (width, height)
plt.title("NYC Boroughs By Area")
plt.show()
#LEGEND: area contains numeric values, GeoPandas colors boroughs based on those values. The legend explains what the colors mean.

#Plot the boundaries and centroids
ax= gdf['geometry'].plot(figsize=(10,6),edgecolor="black")
gdf["centroid"].plot(ax=ax, #adds red centroid points to that same map (ax)
                      color="red",
                      markersize=50)
plt.title("NYC Borough Boundaries and Centroids")
plt.show()

#We can explore our data interactively using GeoDataFrame.explore(). Behaves in the same way plot() does but returns an interactive map. It will be a webpage

m=gdf.explore("area",legend=True) #uses GeoPandas + Folium + Branca + Mapclassify + Leaflet
m.save("nyc_interactive_map.html")

#****Geometry Manipulations***
#Buffering Geometries
#Buffer the borough by 10000 feet
gdf["buffered"]=gdf.buffer(10000)

#Plot the buffered geometries
gdf["buffered"].plot(alpha=0.5,edgecolor="black")
plt.title("Buffered NYC Boroughs (10,000 feet)")
plt.show()
#borough are similar to districts in Kerala. NYC have 5 Borough: Manhattan, Brooklyn, Queens, Bronx, Staten Island

#Convex Hulls
#calculate convex hull
gdf["convex hull"]=gdf.convex_hull

#plot
gdf["convex hull"].plot(alpha=0.5,edgecolor="black",color="lightgreen")
plt.title("Convex Hull of NYC Boroughs")
plt.show()
# Convex hull is the smallest convex polygon that completely encloses a geometry, like a rubber band wrapped around it.
#Buffer → "grow" the geometry outward.
#Convex hull → "wrap a rubber band" around the geometry.

#******Spatial Queries and Relations*******
#Checking for Intersections
# find which boroughs’ buffered areas intersect with the original geometry of Manhattan

#Get the geometry of Manhattan
manhattan_geo=gdf.loc["Manhattan","geometry"]

#check which buffered boroughs intersect with Manhattan's geometry
gdf["intersects_manhattan"]=gdf["buffered"].intersects(manhattan_geo)
print(gdf[["intersects_manhattan"]])

#Checking for Containment
# we can check if the centroids are contained within the borough boundaries

#check if centroids are within the original borough geometries.
gdf["centroid_within_borough"]=gdf["centroid"].within(gdf["geometry"])
print(gdf[["centroid_within_borough"]])

#*****Projections and Coordinate Reference Systems (CRS)******
#Each GeoSeries and GeoDataFrame has a crs attribute that defines its CRS.

#checking crs
print(gdf.crs)
#EPSG:2263 : EPSG stands for European Petroleum Survey Group, which was a scientific organization that standardized geodetic and coordinate reference systems. EPSG codes are unique identifiers that represent coordinate systems and other geodetic properties. 
# The CRS for this dataset is EPSG:2263 (NAD83 / New York State Plane). We can reproject the geometries to WGS84 (EPSG:4326), which uses latitude and longitude coordinates.

#Reprojecting to WGS84
gdf_new=gdf.to_crs(epsg=4326)

#plot
gdf_new_plot=gdf_new.plot(figsize=(10,6),edgecolor="black")
plt.title("NYC Boroughs in WGS84")
plt.show()