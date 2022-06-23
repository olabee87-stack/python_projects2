import numpy as np

# We can use numpy to convert a list to an array in python
# It offers flexibility and versatility
# Note though: Arrays in python does not support values of different data types
# If you for example add a string to it, it will convert all types to a string, incl the numbers there


my_list = [2, 67, 98, 43, 97]

new_list = np.array(my_list)

print(new_list.mean())

print(new_list)