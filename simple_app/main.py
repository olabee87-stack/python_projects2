name = "Olabisi"
age = 34
height = 5.5
hasChild = True

# Single line comment

"""
This is a multiline comment
"""


def person():
    return name.upper(), age, height, hasChild


print('Basic info of Miss Odusanya --- :', person())
print(type(name))
print(type(height))
print(type(hasChild))

# Get length
print(len(name))

# Replace a string character
print(name.replace('Ol', 'El'))

# Check boolean - false bcos age is a num
print(age == str)

# Check if a word or letter is in a string - Should return true bcos la is in 'Olabisi'
print('la' in name)

# Check if word not in a string false because there's no combo of 'ba' in 'Olabisi'
print('ba' in name)






