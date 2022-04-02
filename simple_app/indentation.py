name = 'Dupe'
surname = 'Odus'
age = 32
fruits = ['mango', 'banana', 'orange']


def sister():
    return f"""
    Name: {name}
    Sur: {surname}
    Age: {age}
    """


def print_fru():
    for fru in fruits:
        return f"""
        {fru}
        ******************
    """


print(sister())
print(print_fru())

# list = [] aka array
# tuple = ()
# dict = {} aka object

