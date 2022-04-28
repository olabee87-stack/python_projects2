def gender_converter(gender='unknown'):
    if gender.upper() == 'M':
        return 'Male'
    elif gender.upper() == 'F':
        return 'Female'
    else:
        return f"""Gender: '{gender}' is unknown"""


print(gender_converter('f'))
