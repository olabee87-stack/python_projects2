import chalky

my_style = chalky.sty.bold & chalky.fg.magenta

def calculator():
    num1 = input ('Enter first number: ')
    num2 = input('Enter another number: ')
    result = float(num1) + float(num2)

    return f"""Your result is: {result} """


print(calculator())
print(my_style(calculator()))

