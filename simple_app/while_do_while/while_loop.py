def print_me():
    max_num = 0
    while max_num < 5:
        print(max_num)
        max_num += 1

    else:
        f"""End of while loopsy!!!"""


def print_num():
    num = 0
    while num < 5:
        print(num)
        if num == 3:
            break
        num += 1


def print_names():
    names = ['Bisi', 'Ara', 'Mum', 'Bayo']

    while len(names) == names:
        print(names)


print_names()
# print_me()
# print_num()
