import numpy as np

#1 Slice the 3x3 matrix to get first two rows and all columns
# Given 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Slicing to get the first two rows and all columns
result = matrix[:2]  # This slices the first two rows
for row in result:
    print(row)

#2 Create a new array using arange and Reshape it to 5x5 matrics

import numpy as np

# Creating a new array using arange
original_array = np.arange(25)

# Reshaping the array to a 5x5 matrix
reshaped_matrix = original_array.reshape(5, 5)

print("Original Array:")
print(original_array)
print("\nReshaped Matrix:")
print(reshaped_matrix)

#3 Split concatenated array into three parts vertically
import numpy as np

# Create a concatenated array
concatenated_array = np.concatenate((np.arange(10), np.arange(10, 20), np.arange(20, 30)))

# Split the concatenated array into three parts vertically
split_arrays = np.vsplit(concatenated_array, 3)

# Display the split arrays
for idx, split_array in enumerate(split_arrays):
    print(f"Split Array {idx+1}:")
    print(split_array)
    print()


#4 Use boolean indexing to replace the elements of the diagonal array with the corresponding random values array.
import numpy as np

# Create a concatenated array
concatenated_array = np.concatenate((np.arange(10), np.arange(10, 20), np.arange(20, 30)))

# Split the concatenated array into three parts vertically
split_arrays = np.vsplit(concatenated_array, 3)

# Display the split arrays
for idx, split_array in enumerate(split_arrays):
    print(f"Split Array {idx+1}:")
    print(split_array)
    print()

#5 Filter array to extract elements greater than 10
import numpy as np

# Create a diagonal array
diagonal_array = np.diag(np.arange(1, 6))

# Create a random values array
random_values_array = np.random.rand(5, 5)

# Replace diagonal elements with corresponding random values
diagonal_array[np.diag_indices_from(diagonal_array)] = random_values_array[np.diag_indices_from(diagonal_array)]

# Display the modified diagonal array
print("Diagonal Array with Random Values:")
print(diagonal_array)


#6 Concatenate the sliced matrix and new array vertically
import numpy as np

# Original matrix
original_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# New array
new_array = np.array([7, 8, 9])

# Slicing the matrix to get the first row
sliced_matrix = original_matrix[0:1]

# Concatenating the sliced matrix and new array vertically
result = np.concatenate((sliced_matrix, np.expand_dims(new_array, axis=0)))

print("Result:")
print(result)

#7 Find maximum value in sliced matrix
import numpy as np

# Original matrix
original_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Slicing the matrix to get a sub-matrix
sliced_matrix = original_matrix[1:, :2]  # Slicing rows 1 and 2, and columns 0 and 1

# Finding the maximum value in the sliced matrix
max_value = sliced_matrix.max()

print("Sliced Matrix:")
print(sliced_matrix)
print("Maximum Value in Sliced Matrix:", max_value)


#8 Reshape the 1D array into a 10x10 matrix
import numpy as np

# Create a 1D array with 100 elements
one_dimensional_array = np.arange(100)

# Reshape the 1D array into a 10x10 matrix
reshaped_matrix = one_dimensional_array.reshape(10, 10)

print("Reshaped Matrix:")
print(reshaped_matrix)

#9 Create a new 2D array with the numbers from 1 to 25 in a 5x5 matrix
import numpy as np

# Create a 2D array with numbers from 1 to 25 in a 5x5 matrix
new_2d_array = np.arange(1, 26).reshape(5, 5)

print("New 2D Array:")
print(new_2d_array)


#10 Find the sum of each row in the 5x5 matrix and store the result in a 1D array

import numpy as np

# Create a 5x5 matrix
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Find the sum of each row and store the results in a 1D array
row_sums = matrix.sum(axis=1)

print("Row Sums:")
print(row_sums)
