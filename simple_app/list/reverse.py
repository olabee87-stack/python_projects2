# Reverse a string

def rev_char(word):
    return word[::-1]

# Reverse a number


def rev_num(num):
    num.reverse()
    return num


# Append to a number

def append_num(num):
    num.append(999)
    return num


def find_length(num):
    return len(num)


def clear_list(num):
    num.clear()
    return num


print(rev_char('monkey'))
print(rev_num([3, 5, 2]))
print(append_num([54, 93, 84]))
print(find_length([64, 23, 98, 46]))
print(clear_list([45, 90, 65, 34, 21]))
