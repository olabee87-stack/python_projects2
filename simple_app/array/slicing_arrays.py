import numpy as np

my_list = [2, 67, 98, 43, 97]

changed_list = np.array(my_list)

# Created a copy or my original array, so as not to mutate it
copy_list = changed_list.copy()


range_example = (list(range(0, 6)))
range_with_step_example = (list(range(0, 10, 2)))

print(copy_list[:2])
print(range_example)
print(range_with_step_example)