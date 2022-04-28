from calculator import divide


def divide_num():
    return divide(60, 5)


# I am casting it as an int, since it returns a float
print(int(divide_num()))
