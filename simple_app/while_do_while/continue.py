# This program continues until the condition is fulfilled.
# The program will do nothing until it gets to the condition. In this case, 5
# When it gets to 5, it will print all the numbers from 5 to the end of the number stipulated: 10

def print_num():
    num = 0
    while num < 10:
        num += 1
        if num < 5:
            continue
        print(num)


# Print all fruits except 'agbalumo'


def print_list():
    fruit_list = ['mango', 'agbalumo', 'agbon', 'sour sop', 'breadfruit']
    for fruit in fruit_list:
        if fruit == 'agbalumo':
            continue
        print(fruit)


print_num()
print_list()
