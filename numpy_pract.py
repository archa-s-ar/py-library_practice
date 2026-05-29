import numpy as np

#Creating 1D array
array1=np.array([1,2,3,4,5])
print("1D Array: ", array1)
print(f"1D Array: {array1}")

print(type(array1)) #<class 'numpy.ndarray'> n dimensional array

# Creating 2D array
array2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2D Array: ", array2)
print(f"2D Array: {array2}")

print(array2.shape) # Shape of the array: (2, 5) means 2 rows and 5 columns

# Create an array of zeros
zer= np.zeros((3,4))
print("Array of zeros: ", zer)

# Create an array of ones
one=np.ones((5,3))
print("Array of ones:\n", one)

# Creating an array with a range of values
range_arr= np.arange(0,10,2) # start, stop, step
print("Range Array: ",range_arr)

# Basic Array Operations

nums=[1, 2, 3, 4, 5]
for num in nums:
    print(num+10)

#addition
arr_Sum= array1+10
print("Array after addition: ", arr_Sum) #each no: in array1 is added by 10

#array multiplication
arr_Mul=array2*3
print("Array after multiplication: ", arr_Mul) #each no: in array2 is multiplied by 3

#element-wise multiplication of two arrays
arr_mul2=array2*np.array([1,2,3,4,5]) #each element of array2 is multiplied by corresponding element of the second array
print("Element-wise multiplication: ", arr_mul2)

#Reshaping an array: Reshaping arrays can be particularly useful when you need to restructure data for specific computations or visualizations.

arr_reshaped= np.arange(12).reshape(3,4) # Reshape a 1D array of 12 elements into a 2D array with 3 rows and 4 columns. No: from 0 to 11.
print("Reshaped Array:\n", arr_reshaped)

#*********Mathematical functions******** on arrays: NumPy provides a wide range of mathematical functions that can be applied to arrays, allowing for efficient computations.

#Square root of each element in the array
sqrt_art=np.sqrt(arr_reshaped)
print("Square root of each element:\n", sqrt_art)

#Exponential of each element in the array
exp_arr=np.exp(arr_reshaped)
print("Exponential of each element:\n", exp_arr)

#Sine of each element in the array
sin_arr=np.sin(arr_reshaped)   
print("Sine of each element:\n", sin_arr)

#logarithm of each element in the array
log_arr=np.log1p(arr_reshaped) # add 1 to avoid log(0) which is undefined
print("Logarithm of each element:\n", log_arr)

#******STATISTICAL OPERATIONS ON ARRAYS*******: NumPy provides various functions to perform statistical operations on arrays, such as mean, median, standard deviation, etc.

arr=np.array([1,2,3,4,5,6,7,8,9,10])
mean_arr= np.mean(arr) #Mean of the array
median_arr=np.median(arr) #Median of the array
std_arr= np.std(arr) #Standard deviation of the array

print("Mean of the array: ", mean_arr,"Median of the array: ", median_arr, "Standard deviation of the array: ", std_arr)

#*********RANDOM DATA GENERATION FOR SIMULATIONS********: NumPy's random module allows you to generate random numbers and arrays, which can be useful for simulations, testing algorithms, or creating synthetic datasets.
#Random data generation is useful for simulations, such as generating random geospatial coordinates or sampling from distributions.

#Generate an array of random latitudes and longitudes
random_cords= np.random.uniform(low = -90, high = 90, size = (5, 2)) # Generate 5 random pairs of latitudes and longitudes. Latitudes range from -90 to 90, and longitudes range from -180 to 180.
print("Random Latitudes and Longitudes:\n", random_cords)

#Generate random samples from a normal distribution
normal_samples= np.random.normal(loc=0, scale=1, size=10) # Generate 10 random samples from a normal distribution with mean 0 and standard deviation 1.
print("Random samples from a normal distribution:\n", normal_samples)

#Generate random integers between 1 and 100
random_ints= np.random.randint(1, 101, size=10) # Generate 10 random integers between 1 and 100 (inclusive).
print("Random integers between 1 and 100:\n", random_ints)

#*********ARRAY INDEXING AND SLICING********: NumPy allows you to access and manipulate specific elements or subsets of an array using indexing and slicing techniques.

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Accessing the first element
first_element = arr[0]
print(f"First element: {first_element}")

# Accessing the last element
last_element = arr[-1]
print(f"Last element: {last_element}")

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr_2d)

# Accessing the element in the first row and second column
element = arr_2d[0, 1]
print(f"Element at row 1, column 2: {element}")

# Accessing the element in the last row and last column
element_last = arr_2d[-1, -1]
print(f"Element at last row, last column: {element_last}")

# Slicing in NumPy

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Slice elements from index 1 to 3 (exclusive)
slice_1d = arr[1:4]
print(f"Slice from index 1 to 3: {slice_1d}")

# Slice all elements from index 2 onwards
slice_2d = arr[2:]
print(f"Slice from index 2 onwards: {slice_2d}")

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_2d

# Slice the first two rows and all columns
slice_2d = arr_2d[:2, :]
print(f"Sliced 2D array (first two rows):\n{slice_2d}")

# Slice the last two rows and the first two columns
slice_2d_partial = arr_2d[1:, :2]
print(f"Sliced 2D array (last two rows, first two columns):\n{slice_2d_partial}")

#Boolean Indexing
# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Boolean condition to select elements greater than 25
condition = arr > 25
print(f"Boolean condition: {condition}")

# Use the condition to filter the array
filtered_arr = arr[condition]
print(f"Filtered array (elements > 25): {filtered_arr}")

#Iterating over arrays

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Iterating through the array
for element in arr:
    print(f"Element: {element}")

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Iterating through rows of the 2D array
print("Iterating over rows:")
for row in arr_2d:
    print(row)

# Iterating through each element of the 2D array
print("\nIterating over each element:")
for row in arr_2d:
    for element in row:
        print(element, end=" ")

#Modifying array elements
# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Modify the element at index 1
arr[1] = 25
print(f"Modified array: {arr}")

# Modify multiple elements using slicing
arr[2:4] = [35, 45]
print(f"Modified array with slicing: {arr}")

#Working with Geospatial Coordinates
# Array of latitudes and longitudes
coords = np.array([[35.6895, 139.6917], [34.0522, -118.2437], [51.5074, -0.1278]])

# Convert degrees to radians
coords_radians = np.radians(coords)
print(f"Coordinates in radians:\n{coords_radians}")