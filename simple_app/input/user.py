import chalky

my_style = chalky.sty.bold & chalky.fg.bright_yellow


def user():
    first_name = input('What is your first name?: ')
    last_name = input('What is your last name?: ')
    fullname = f"""My name is {str(first_name)} {str(last_name)}"""

    return fullname


print(my_style(user()))




