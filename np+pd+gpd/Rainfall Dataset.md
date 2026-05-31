# Kerala Rainfall Analysis using Pandas & GeoPandas

## Objective

Analyze district-wise rainfall data of Kerala and visualize it using GeoPandas.

---

# Dataset

## 1. Rainfall Data (Excel)

| Column    | Description    |
| --------  | -------------- |
| District  | Rainfall       |
| Dist name | Rainfall value |

Example:

| District | Rainfall |
| -------- | -------- |
| Kollam   | 286      |
| Kottayam | 315      |
| Idukki   | 412      |

---

## 2. Kerala District Boundary (GeoJSON)

Contains:

* District boundaries
* Geometry polygons
* CRS information

---

# Workflow

```text
Rainfall Excel (.xlsx)
        ↓
Read using Pandas
        ↓
Explore Data
(mean, max, min, sort)
        ↓
Plot Rainfall Map
```

---

# Step 1: Read Excel

```python
import pandas as pd

df = pd.read_excel(
    "rain.xlsx",
    engine="openpyxl"
)
```

View data:

```python
df.head()
```

---

# Step 2: Inspect Dataset

Columns:

```python
df.columns
```

Output:

```text
District
Rainfall
```

---

# Step 3: Basic Statistics

## Mean Rainfall

```python
df["Rainfall"].mean()
```

## Maximum Rainfall

```python
df["Rainfall"].max()
```

## Minimum Rainfall

```python
df["Rainfall"].min()
```

## Summary Statistics

```python
df["Rainfall"].describe()
```

Returns:

```text
count
mean
std
min
25%
50%
75%
max
```

---

# Step 4: Sort Rainfall

## Ascending

```python
df.sort_values("Rainfall")
```

## Descending

```python
df.sort_values(
    "Rainfall",
    ascending=False
)
```

---

# Step 5: Plot Rainfall Chart

```python
df.plot(
    x="District",
    y="Rainfall",
    kind="bar",
    figsize=(10,5)
)
```

---


# Common Errors

## Wrong

```python
df.mean("Rainfall")
```

Correct:

```python
df["Rainfall"].mean()
```

---

## Wrong

```python
df["Rainfall"].sort()
```

Correct:

```python
df["Rainfall"].sort_values()
```

---

## Wrong

```python
gpd.read_file("rain.xlsx")
```

Reason:

```text
Excel is not a geospatial file.
```

Correct:

```python
pd.read_excel("rain.xlsx")
```

---

# Key Concepts

| Concept          | Meaning                         |
| ---------------- | ------------------------------- |
| Pandas DataFrame | Tabular data                    |
| GeoDataFrame     | Data + Geometry                 |
| Merge            | Join tables using common column |
| GeoJSON          | Geospatial file format          |
| Choropleth Map   | Color districts based on values |
| Geometry         | Spatial shape of districts      |

---

# Quick Revision

```text
Excel
(District, Rainfall)
        ↓
Pandas
        ↓
Statistics
        ↓
Rainfall plot
```

---