person = {
    "name": 'Ola',
    "age": 34,
    "height": 164
}

# Print the keys in the dictionary


def print_keys():
    return person.keys()


# Print the keys in the dictionary
def print_values():
    return person.keys()


# Print the values in the dictionary
def print_keys():
    return person.values()


# Print specific value of the key in the parentheses
def print_val_or_key():
    return person.get('name')


# Print specific value of the key index
def print_val_of_index():
    return person['height']


print(print_keys())
print(print_values())
print(print_val_or_key())
print(print_val_of_index())
