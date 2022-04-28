lettersA = {'A', 'B', 'C', 'D'}
lettersB = {'E', 'F', 'G'}
lettersC = {'E', 'F'}

union = lettersA | lettersB
intersection = lettersB & lettersC
difference = lettersB - lettersA


# Union - Will print the union of both sets

def print_set_union():
    return f"""Union result is: {union}"""


# Intersection - Will print common occurrence of both sets

def print_set_intersection():
    return f"""Intersection result: {intersection}"""


# Difference will return what is in the first set but not in the other set. NOTE: The order of the set matters
def print_difference():
    return f"""Difference: {difference}"""


print(print_set_union())
print(print_set_intersection())
print(print_difference())
