def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def re_assign():
    num = 0
    num += 50
    return num


def re_assign2():
    num = 2
    num *= 50
    return num


print(addition(50, 50))
print(subtraction(100, 50))
print(modulus(32, 5))
print(power(5, 5))
print(re_assign())
print(re_assign2())


