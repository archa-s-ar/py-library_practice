# GeoPandas

### What is GeoPandas?

GeoPandas is an open-source Python library that simplifies working with geospatial data by extending Pandas data structures.
It combines the functionalities of Pandas and Shapely, enabling geospatial operations like spatial joins, buffering, intersections, and projections with ease.

```python
pip install geopandas
import geopanda as gpd
```

```text
Pandas
   ↓
Tabular Data

GeoPandas
   ↓
Tabular Data + Geometry
```

### Main Data Structures

| Structure    | Description                    |
| ------------ | ------------------------------ |
| DataFrame    | Tabular data                   |
| GeoDataFrame | Tabular data + geometry column |
| GeoSeries    | Series containing geometries   |

Example:

```python
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
)
```

---

# 2. Reading & Writing Data

## Read Data

```python
gdf = gpd.read_file("file.geojson")
```

Supported formats:

| Format     | Extension |
| ---------- | --------- |
| GeoJSON    | .geojson  |
| Shapefile  | .shp      |
| GeoPackage | .gpkg     |

## Write Data

```python
gdf.to_file("data.geojson", driver="GeoJSON")
gdf.to_file("data.shp")
gdf.to_file("data.gpkg", driver="GPKG")
```

⚠️ GeoJSON/Shapefile generally expect one active geometry column.

---

# 3. Accessing Data

## Set Index

```python
gdf = gdf.set_index("BoroName")
```

```text
Before
0
1
2

After
Manhattan
Queens
Brooklyn
```

## Select Rows

```python
gdf.loc["Manhattan"]
```

## Select Specific Value

```python
gdf.loc["Manhattan", "geometry"]
```

---

# 4. Geometry Measurements

## Area

```python
gdf["area"] = gdf.area
```

Returns polygon area.

---

## Mean

```python
gdf["area"].mean()
```

Returns average area.

---

# 5. Boundaries & Centroids

## Boundary

```python
gdf["boundary"] = gdf.boundary
```

Returns polygon outlines.

```text
Polygon
██████

Boundary
▢
```

---

## Centroid

```python
gdf["centroid"] = gdf.centroid
```

Returns center point.

```text
Polygon
██████
██•███
██████
```

---

# 6. Distance Calculations

## Distance Between Geometries

```python
gdf["distance"] = gdf["centroid"].distance(reference_point)
```

Used for:

- Nearest city
- Nearest hospital
- Distance from Manhattan

---

# 7. Plotting

## Basic Plot

```python
gdf.plot()
```

---

## Thematic Map

```python
gdf.plot(
    column="area",
    legend=True
)
```

```text
Light Color  → Small Value
Dark Color   → Large Value
```

---

## Overlay Layers

```python
ax = gdf["geometry"].plot()

gdf["centroid"].plot(
    ax=ax,
    color="red"
)
```

```text
Polygon Layer
     +
Centroid Layer
```

---

# 8. Interactive Maps

## Explore

For doing gdf.explore() for interactive map, which uses GeoPandas + Folium + Branca + Mapclassify + Leaflet

```python
pip install folium mapclassify branca
```

```python
m = gdf.explore(
    column="area",
    legend=True
)
```

Save:

```python
m.save("map.html")
```

Uses:

```text
GeoPandas
   ↓
Folium
   ↓
Leaflet
```

Interactive Features:

- Zoom
- Pan
- Legend
- Popups

---

# 9. Geometry Manipulations

## Buffer

```python
gdf["buffered"] = gdf.buffer(10000)
```

### Concept

```text
Original Polygon
     ███

Buffered Polygon
  █████████
```

Meaning:

Grow geometry outward.

Use Cases:

- Flood zones
- Hospital coverage
- Airport influence area

---

## Convex Hull

```python
gdf["convex_hull"] = gdf.convex_hull
```

### Concept

Imagine wrapping a rubber band around a geometry.

```text
Irregular Shape
  /\__
 /    \

Convex Hull
 _______
/       \
\_______/
```

Definition:

Smallest convex polygon enclosing a geometry.

---

# 10. Spatial Queries

## Intersects

```python
gdf["buffered"].intersects(
    manhattan_geometry
)
```

Checks whether geometries touch or overlap.

Returns:

```text
True
False
```

---

## Within

```python
gdf["centroid"].within(
    gdf["geometry"]
)
```

Checks whether a geometry lies inside another.

Example:

```text
Point inside polygon?
→ True
```

---

# 11. CRS (Coordinate Reference Systems)

## Check CRS

```python
print(gdf.crs)
```

Example:

```text
EPSG:2263
```

---

## Reproject Data

```python
gdf_wgs84 = gdf.to_crs(
    epsg=4326
)
```

### Common CRS

| EPSG | Description     |
| ---- | --------------- |
| 4326 | WGS84 (Lat/Lon) |
| 3857 | Web Mercator    |
| 2263 | NY State Plane  |

---

# GeoPandas Workflow

```text
Read Data
    ↓
Inspect Columns
    ↓
Set Index
    ↓
Calculate Area
    ↓
Create Boundary
    ↓
Create Centroid
    ↓
Spatial Analysis
    ↓
Plot / Explore
    ↓
Export Results
```

---

# Memory Tricks

```text
Boundary
= Outline

Centroid
= Center Point

Buffer
= Grow Geometry

Convex Hull
= Rubber Band

Intersects
= Touches?

Within
= Inside?

CRS
= Coordinate System

Explore()
= Interactive Map

Plot()
= Static Map
```
