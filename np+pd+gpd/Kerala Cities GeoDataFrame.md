# Kerala Districts GeoPandas Practice

## Objective

Learn how to use GeoPandas for:

* Reading geospatial data
* Understanding CRS
* Plotting maps
* Calculating centroids
* Creating buffers
* Spatial analysis
* Extracting latitude and longitude

---

# Dataset

Kerala District Boundaries (GeoJSON)

Columns available:

| Column       | Description        |
| ------------ | ------------------ |
| DISTRICT     | District Name      |
| Area         | Area of district   |
| Perimeter    | District perimeter |
| Shape_Area   | Geometry area      |
| Shape_Length | Geometry perimeter |
| geometry     | District polygon   |

---

# Workflow

```text
Load GeoJSON
      ↓
Inspect Data
      ↓
Check CRS
      ↓
Plot Districts
      ↓
Set District as Index
      ↓
Project CRS (3857)
      ↓
Calculate Centroids
      ↓
Extract Latitude/Longitude
      ↓
Create Buffers
      ↓
Spatial Analysis
      ↓
Export Results
```

---

# 1. Read Dataset

```python
gdf = gpd.read_file(url)
```

Check columns:

```python
gdf.columns
```

---

# 2. Plot Kerala Districts

```python
gdf.plot(
    figsize=(8,8),
    edgecolor="black"
)
plt.show()
```

Purpose:

* Visualize district boundaries
* Verify geometry is loaded correctly

---

# 3. Check CRS

```python
gdf.crs
```

Output:

```text
EPSG:4326
```

Meaning:

| Property    | Value                |
| ----------- | -------------------- |
| CRS         | WGS84                |
| Units       | Degrees              |
| Coordinates | Latitude & Longitude |

---

# 4. Why Reproject?

EPSG:4326 is good for:

✅ GPS

✅ Web Maps

✅ Latitude & Longitude

---

# 5. Reproject to Metric CRS

```python
gdf_proj = gdf.to_crs(epsg=3857)
```

EPSG:3857 uses:

```text
Meters
```

Useful for:

* Distance
* Buffer
* Area
* Centroid

---

# 6. Calculate Centroids

Wrong:

```python
gdf["centroid"] = gdf.centroid
```

Reason:

```text
Geometry is in a geographic CRS
```

Correct:

```python
gdf_proj["centroid"] = gdf_proj.centroid
```

Convert back:

```python
gdf["centroid"] = (
    gdf_proj["centroid"]
    .to_crs(epsg=4326)
)
```

---

# 7. Extract Latitude & Longitude

Important:

```text
x → Longitude
y → Latitude
```

Correct:

```python
gdf["Longitude"] = gdf["centroid"].x
gdf["Latitude"] = gdf["centroid"].y
```

View:

```python
gdf[
    ["DISTRICT",
     "Latitude",
     "Longitude"]
]
```

Example:

| DISTRICT  | Latitude | Longitude |
| --------- | -------- | --------- |
| Kollam    | ...      | ...       |
| Kottayam  | ...      | ...       |
| Ernakulam | ...      | ...       |

---

# 8. Set District as Index

Correct:

```python
gdf = gdf.set_index("DISTRICT")
```

Useful:

```python
gdf.loc["Kollam"]
```

---

# 9. Create Buffer

Goal:

```text
20 km Buffer
```

Conversion:

```text
1 km = 1000 m

20 km = 20000 m
```

Create:

```python
gdf_proj["buffer"] = (
    gdf_proj.buffer(20000)
)
```

---

# 10. Plot Buffer

```python
gdf_proj["buffer"].plot(
    alpha=0.5,
    edgecolor="black"
)

plt.show()
```

Better:

```python
ax = gdf_proj["buffer"].plot(
    alpha=0.5,
    edgecolor="black"
)

gdf_proj["geometry"].plot(
    ax=ax,
    color="red"
)

plt.show()
```

---

# Buffer Concept

```text
Original District
      ↓

Grow Geometry Outward
      ↓

Buffered District
```

Use Cases:

* Flood zones
* Hospital coverage
* Satellite coverage
* Protected regions

---

# 11. Common GeoPandas Mistakes

## Mistake 1

```python
gdf("DISTRICT")
```

Error:

```text
GeoDataFrame is not callable
```

Correct:

```python
gdf["DISTRICT"]
```

---

## Mistake 2

```python
gdf.set_index["DISTRICT"]
```

Error:

```text
method object is not subscriptable
```

Correct:

```python
gdf.set_index("DISTRICT")
```

---

## Mistake 3

```python
gdf["Latitude"] = gdf["centroid"].x
```

Wrong because:

```text
x = Longitude
```

Correct:

```python
gdf["Longitude"] = gdf["centroid"].x
gdf["Latitude"] = gdf["centroid"].y
```

---

# Quick Memory Tricks

```text
Geometry.x
      ↓
Longitude

Geometry.y
      ↓
Latitude
```

---

```text
EPSG:4326
      ↓
Display / GPS

EPSG:3857
      ↓
Distance / Area / Buffer / Centroid
```

---
