def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

# print(list(squared))


def return_dates(my_date):
    return my_date


dates = ['2022', '888', '87533']

result = map(return_dates, dates)

print(list(result))