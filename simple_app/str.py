comment = """
This is how
to split your words
into different lines in Python!
"""
print(comment)

# NOTE: You could also do print(email.format(name)) to print but preceding with f is cleaner

name = 'Araoluwa'
email = f"""
Hello {name}
How are you doing today?
Did you sleep well ?
"""


def print_name():
    return print(email)


print_name()

