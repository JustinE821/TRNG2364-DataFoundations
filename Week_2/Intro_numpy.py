# numpy is a powerful library for numerical computing
#it provides support for arrays, matricies, and a wide range of mathematical functions
#to operate on these data structures
#many libraries build on top of numpy (pandas, scipy, scikit-learn)

#numpy is written in C and Fortran, making it very fast for numerical computations

import numpy as np

#Create a 1D array
array_1d = np.array([1, 2, 5, 6, 34, 81])
print("1D array: ", array_1d)

#Create a 2D array
array_2d = np.array([[5, 9, 18],[91, 45, 16]])

print("2D Array: ", array_2d)


#Perform some basic operations
#addition
array_sum = array_1d + 10
print("Array after addition: ", array_sum)

#multiplication
array_multiplied = array_1d * 4
print("Array after multiplication:  ", array_multiplied)

#Calculate the mean
mean_value = np.mean(array_1d)
print("Mean: ", mean_value)

#Calculate standard deviation
standard_dev = np.std(array_1d)
print("Standard Deviation: ", standard_dev)

#reshape 1d array into a 2d array
reshaped_array = array_1d.reshape((6, 1))
print("Reshaped array: ", reshaped_array)

#access elements
accessed_element = array_2d[0][2] # should be 18
print("My accessed item: ", accessed_element)