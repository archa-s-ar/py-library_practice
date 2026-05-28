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

