def take_input():
    name = input("What is your name?: ")
    age = input("How old are you?: ")
    if name == '' and age <= 0:
        return print('Please, enter your name and age!')
    else:
        summary = f"""This person is {name} and she is {age} years old"""
    return summary


print(take_input())
