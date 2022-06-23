import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Get a specific element
 # Bcos we have two array here, the forst array is index 0 and the second array is index 1
 # To get a value in either arrays, you have to reference the index of that array first, then the value
print(a[0, 5])

# Get a specific row
print(a[0, :])

# Get a specific column from both rows (Will print the 3rd index of all rows)
print(a[:, 2])

# Skip two steps
print(f"""Steps: {a[0, 1:: 2]}""")
print(f"""Another way steps: {a[0, 1:-1:2]}""")

# Re-assign
