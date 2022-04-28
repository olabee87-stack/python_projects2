# Import a package to check the path, verify that your path is correct,
# print it, handle non-existent file


import os.path

filename = './data.csv'

if os.path.isfile(filename):
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f""" The filename: "{filename}" does not exist! """)






