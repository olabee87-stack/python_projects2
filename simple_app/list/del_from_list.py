# Remove first num on the list

def remove_first_num(num):
    num.remove(21)
    return num


# Remove last num on the list

def remove_last_num(num):
    num.pop()
    return num


# Remove num from a specific position

def remove_num(num):
    del num[4]
    return num


# Remove from multiple positions - This ex will remove all numbers before the 6th index
def remove_many(num):
    del num[1:6]
    return num


print(remove_first_num([21, 15, 98, 50]))
print(remove_last_num([71, 25, 88, 60]))
print(remove_num([91, 15, 35, 78, 70]))
print(remove_many([91, 15, 35, 78, 70, 100, 500, 534, 894]))
