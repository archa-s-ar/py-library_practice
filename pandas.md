# Pandas
Pandas is a powerful data manipulation library that provides data structures like Series and DataFrames to work with structured data. It is especially useful for handling tabular data.


## Overview

This project demonstrates:

* Pandas Series
* Pandas DataFrames
* DataFrame operations
* Filtering and selection
* Grouping and aggregation
* Merging DataFrames
* Handling missing values
* Reading CSV files from URLs
* Data visualization with Matplotlib
* Geospatial analysis using the Haversine Formula

---

# 1. Importing Libraries

```python
pip install pandas
import pandas as pd

```

### Purpose

* pandas → Data analysis and tabular data
* numpy → Numerical computations
* matplotlib → Data visualization

---

# 2. Pandas Series

```python
city_series = pd.Series(
    ["Tokyo", "Los Angeles", "London"],
    name="City"
)
```

### Important Points

* Series is one-dimensional.
* Similar to a single column in a spreadsheet.
* Can store numbers, text, dates, etc.

Example:

```text
0 Tokyo
1 Los Angeles
2 London
```

---

# 3. Creating a DataFrame

```python
df = pd.DataFrame(data)
```

### Important Points

* DataFrame is a 2D table.
* Consists of rows and columns.
* Most commonly used Pandas structure.

Example:

```text
City        Latitude   Longitude
Tokyo       35.6895    139.6917
```

---

# 4. Selecting Columns

```python
df["Latitude"]
```

### Important Points

Returns a Series.

Useful for:

* calculations
* plotting
* filtering

---

# 5. Filtering Rows

```python
df[df["Longitude"] < 0]
```

### Important Points

Creates a subset of data.

Returns only rows satisfying the condition.

Example:

```text
Longitude < 0
```

returns London and Los Angeles.

---

# 6. Creating New Columns

```python
df["Lat_Radians"] = np.radians(df["Latitude"])
```

### Important Points

Creates a new column.

Useful for:

* transformations
* calculations
* feature engineering

---

# 7. Grouping and Aggregation

```python
df.groupby("Country")["Population"].sum()
```

### Purpose

Combines rows with the same country.

Calculates total population per country.

Example:

```text
USA
3970000 + 2665000
```

---

# 8. Merging DataFrames

```python
pd.merge(df1, df2, on="City")
```

### Important Points

Equivalent to SQL JOIN.

Combines information from multiple tables.

Common merge types:

```python
inner
left
right
outer
```

---

# 9. Handling Missing Values

### Missing Value

```python
None
```

becomes:

```python
NaN
```

in Pandas.

### Fill Missing Values

```python
df.fillna(
    df["Population"].mean()
)
```

### Important Points

Prevents errors during analysis.

Common methods:

```python
fillna()
dropna()
interpolate()
```

---

# 10. Reading CSV Files

```python
pd.read_csv(url)
```

### Important Points

Loads external datasets.

Can read from:

* local files
* URLs
* APIs

Example:

```python
world_cities.csv
```

---

# 11. NumPy vs Pandas Sum

NumPy:

```python
np.sum(df["population"])
```

Pandas:

```python
df["population"].sum()
```

### Important Points

Pandas:

* Handles NaN values better
* Optimized for DataFrames
* Preferred when working with tabular data

---

# 12. Plotting with Pandas

## Basic Plot

```python
air_quality.plot()
```

Displays all numeric columns.

Requires:

```python
matplotlib
```

---

## Show Plot

```python
plt.show()
```

Without this:

Plot may not appear.

---

# 13. Line Plot

```python
air_quality["station_paris"].plot()
```

### Purpose

Visualizes changes over time.

Useful for:

* temperature
* pollution
* rainfall
* stock prices

---

# 14. Scatter Plot

```python
air_quality.plot.scatter(
    x="station_london",
    y="station_paris",
    alpha=0.5
)
```

### Purpose

Shows relationship between variables.

### Alpha

```python
alpha=0.5
```

Controls transparency.

Useful when many points overlap.

---

# 15. Area Plot

```python
air_quality.plot.area(
    figsize=(12,4),
    subplots=True
)
```

### Purpose

Shows magnitude changes over time.

Useful for:

* environmental monitoring
* time-series analysis
* satellite observations

---

# 16. Geospatial Analysis

## Haversine Formula

Used to calculate:

### Great-Circle Distance

Distance between two points on Earth's surface.

Inputs:

```python
Latitude
Longitude
```

Output:

```python
Distance in kilometers
```

---

# 17. Earth Radius

```python
R = 6371.0
```

### Important Point

6371 km is the average radius of Earth.

Used in most geospatial calculations.

---

# 18. Radians Conversion

```python
np.radians()
```

### Important Point

Trigonometric functions require radians.

Not degrees.

---

# 19. Calculating City-to-City Distances

Example:

```text
Tokyo → London
Tokyo → Los Angeles
Los Angeles → London
```

Stored in:

```python
city_pairs["Distance_km"]
```

This adds a new column containing calculated distances.

---

# Real GIS Applications

The same concepts are used in:

* Remote Sensing
* GIS Analysis
* Navigation Systems
* GPS Applications
* Satellite Tracking
* Drone Mapping
* Earth Observation
* ISRO Geospatial Workflows

---

# Common Pandas Functions Used

```python
pd.Series()
pd.DataFrame()
pd.read_csv()

groupby()
sum()
merge()

fillna()

plot()
plot.scatter()
plot.area()

head()
columns
```

---

# Key Concepts to Remember

✓ Series = 1D data

✓ DataFrame = 2D table

✓ Columns are selected using []

✓ Boolean conditions filter rows

✓ New columns can be created directly

✓ groupby() is used for aggregation

✓ merge() combines datasets

✓ NaN represents missing values

✓ read_csv() loads external datasets

✓ Pandas plotting requires Matplotlib

✓ Scatter plots show relationships

✓ Area plots show trends over time

✓ Haversine formula calculates Earth-surface distances

✓ GIS calculations require latitude and longitude in radians

✓ Pandas + NumPy + Matplotlib form the foundation of Data Science and GeoSpatial Analysis
