def is_adult(age):
    if age >= 18:
        return f"""Your age is {age}: and you're an adult!"""
    else:
        return f"""Sorry, you are {age} years old! Apply when you are 18!"""


print(is_adult(20))