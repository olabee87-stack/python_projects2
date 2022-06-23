import numpy as np

a_list = [1, 2, 3]
b_list = [1, 2, 3]

# This can be done because it is numpy. Cannot be done with lists
a_numpy = np.array([1, 2, 3])
b_numpy = np.array([1, 2, 3])

# Multidimensional arrays
c_numpy = np.array([[1, 2, 3], [4, 5, 5]])

# Get the shape of the array
print(f"""Shape: {c_numpy.shape}""")

# Get the dimension of the array
print(f"""Dimension: {c_numpy.ndim}""")

# Get type
print(f"""Type: {c_numpy.dtype}""")

# Get size
print(f"""Size: {c_numpy.itemsize}""")

# Get total size
print(f"""Total size: {c_numpy.nbytes}""")





print(a_numpy * b_numpy)
