def print_num():
    num = 0
    while num < 5:
        print(num)
        if num == 3:
            break
        num += 1


def print_num2():
    num = 0
    while num < 5:
        if num == 3:
            break
        num += 1
        print(f"""Numbers: {num}""")


# Print all fruits before agbalumo
# Use continue instead of break if you want to print fruits from agbalumo to the end


def print_list():
    fruit_list = ['mango', 'cherry', 'agbalumo', 'soup sop', 'oronbo']

    for fruit in fruit_list:
        if fruit == 'agbalumo':
            break
        print(fruit)


# print_num()
# print_num()
print_list()
