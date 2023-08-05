a = 1
b = 2
sum = a + b
print(sum)

import numpy as np  # numpy is python library imported to use array, do liner algebra,fourier transform and matrices

# numpy is open source project and defined as Numerical Python(numpy)
# array of objet is called 'ndarray'
# arrays are stored in one continuous place in memory unlike List
# this is why numpy is 50X faster than list

arr = np.array([1, 2, 3, 4])


two_dimension_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
three_dimension_arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[1, 2, 3, 4], [5, 6, 7, 8]]])
print('three_dimension_arr',three_dimension_arr.reshape(2,8))
reshape_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("numpy arr", type(arr))
print("find dimension", arr.ndim)
print("find shape", arr.shape)
print("reshape", reshape_arr.reshape(5, 2))