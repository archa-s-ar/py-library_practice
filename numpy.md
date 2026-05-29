# py-library_practice
numpy, geopandas, pandas, matplotlib for geo analysis

NumPy (Numerical Python) is a library used for scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

```python
pip install numpy
import numpy as np
```

# 1. Creating Arrays

### 1D Array

```python
array1 = np.array([1,2,3,4,5])
```

Creates a one-dimensional array.

Useful attributes:

```python
type(array1)
```

Output:

```python
<class 'numpy.ndarray'>
```

---

### 2D Array

```python
array2 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
```

Represents rows and columns.

Check dimensions:

```python
array2.shape
```

Output:

```python
(2,5)
```

Meaning:

* 2 rows
* 5 columns

---

# 2. Special Array Creation Functions

### Array of Zeros

```python
np.zeros((3,4))
```

Creates:

* 3 rows
* 4 columns
* all values = 0

---

### Array of Ones

```python
np.ones((5,3))
```

Creates:

* 5 rows
* 3 columns
* all values = 1

---

### Range Array

```python
np.arange(0,10,2)
```

Syntax:

```python
np.arange(start, stop, step)
```

Output:

```python
[0 2 4 6 8]
```

---

# 3. Vectorized Operations

NumPy performs operations on all elements at once.

### Addition

```python
array1 + 10
```

Adds 10 to every element.

---

### Multiplication

```python
array2 * 3
```

Multiplies every element by 3.

---

### Element-wise Multiplication

```python
array2 * np.array([1,2,3,4,5])
```

Each element is multiplied by its corresponding element.

Important:

Shapes must be compatible for broadcasting.

---

# 4. Reshaping Arrays

```python
np.arange(12).reshape(3,4)
```

Creates:

```python
0  1  2  3
4  5  6  7
8  9 10 11
```

Important Rule:

Total elements must remain the same.

Example:

```python
12 elements → 3 × 4 = 12
```

---

# 5. Mathematical Functions

NumPy applies functions element-by-element.

### Square Root

```python
np.sqrt(arr)
```

---

### Exponential

```python
np.exp(arr)
```

Calculates:

e^x

---

### Sine

```python
np.sin(arr)
```

Input is assumed to be in radians.

---

### Logarithm

```python
np.log1p(arr)
```

Equivalent to:

```python
log(1 + x)
```

Useful because:

```python
log(0)
```

is undefined.

---

# 6. Statistical Operations

Given:

```python
arr = np.array([1,2,3,4,5,6,7,8,9,10])
```

### Mean

```python
np.mean(arr)
```

Average value.

---

### Median

```python
np.median(arr)
```

Middle value.

---

### Standard Deviation

```python
np.std(arr)
```

Measures spread of data.

---

# 7. Random Data Generation

Useful for:

* Simulations
* Machine learning
* Testing
* Geospatial analysis

---

### Uniform Distribution

```python
np.random.uniform(
    low=-90,
    high=90,
    size=(5,2)
)
```

Generates random values between -90 and 90.

---

### Normal Distribution

```python
np.random.normal(
    loc=0,
    scale=1,
    size=10
)
```

Parameters:

* loc = mean
* scale = standard deviation

---

### Random Integers

```python
np.random.randint(
    1,
    101,
    size=10
)
```

Generates integers from 1 to 100.

Note:

Upper limit is exclusive.

---

# 8. Array Indexing

### First Element

```python
arr[0]
```

---

### Last Element

```python
arr[-1]
```

Negative indexing starts from the end.

---

### 2D Indexing

```python
arr_2d[row, column]
```

Example:

```python
arr_2d[0,1]
```

First row, second column.

---

# 9. Array Slicing

### 1D Slicing

```python
arr[1:4]
```

Includes:

```python
1,2,3
```

Excludes:

```python
4
```

Rule:

```python
[start : stop]
```

Stop index is NOT included.

---

### From Specific Position

```python
arr[2:]
```

Everything from index 2 onward.

---

### 2D Slicing

First two rows:

```python
arr_2d[:2,:]
```

Last two rows, first two columns:

```python
arr_2d[1:,:2]
```

General form:

```python
array[rows, columns]
```

---

# 10. Boolean Indexing

Create condition:

```python
condition = arr > 25
```

Returns:

```python
[False False True True True]
```

Use it:

```python
arr[condition]
```

Filters elements matching the condition.

Very important for data analysis.

---

# 11. Iterating Through Arrays

### 1D Array

```python
for element in arr:
```

Loops through each value.

---

### 2D Array Rows

```python
for row in arr_2d:
```

Returns one row at a time.

---

### Every Element

```python
for row in arr_2d:
    for element in row:
```

Nested iteration.

---

# 12. Modifying Arrays

### Single Element

```python
arr[1] = 25
```

---

### Multiple Elements

```python
arr[2:4] = [35,45]
```

Updates multiple values at once.

---

# 13. Geospatial Coordinate Processing

Coordinates:

```python
[
 [35.6895, 139.6917],
 [34.0522,-118.2437],
 [51.5074,-0.1278]
]
```

Represent:

```python
[latitude, longitude]
```

---

### Degrees to Radians

```python
np.radians(coords)
```

Important because:

Many GIS and geospatial calculations use radians.

Examples:

* Haversine Distance
* Great Circle Distance
* Satellite calculations
* Remote Sensing algorithms

---

