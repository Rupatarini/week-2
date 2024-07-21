import numpy as np

array_from_list = np.array([1, 2, 3, 4])
array_linspace = np.linspace(0, 10, 5)
array_zeros = np.zeros((2, 3))
array_ones = np.ones((2, 3))
array_arange = np.arange(0, 10, 2)

print("Array from list:", array_from_list)
print("Array with linspace:", array_linspace)
print("Array of zeros:\n", array_zeros)
print("Array of ones:\n", array_ones)
print("Array with arange:", array_arange)

reshaped_array = np.reshape(array_from_list, (2, 2))
print("Reshaped array:\n", reshaped_array)

mean_value = np.mean(array_from_list)
median_value = np.median(array_from_list)
std_dev = np.std(array_from_list)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)

sum_value = np.sum(array_from_list)
prod_value = np.prod(array_from_list)
dot_product = np.dot(array_from_list, [1, 1, 1, 1])

print("Sum:", sum_value)
print("Product:", prod_value)
print("Dot Product:", dot_product)

transposed_array = np.transpose(array_zeros)
print("Transposed array:\n", transposed_array)

min_value = np.min(array_from_list)
max_value = np.max(array_from_list)

print("Minimum value:", min_value)
print("Maximum value:", max_value)

concatenated_array = np.concatenate((array_zeros, array_ones), axis=0)
print("Concatenated array:\n", concatenated_array)

