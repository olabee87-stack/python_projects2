my_son = {
    "name": "Araoluwa",
    "age": 9,
    "hobbies": ['running', 'eating turkey']
}


def print_son():
    for key in my_son:
        print(key)


def print_key_val():
    for key in my_son:
        print(f"""Key: {key} -- Value: {my_son[key]}""")


def print_key_val2():
    for key, value in my_son.items():
        print(f"""Keymi: {key} ---- Value mi: {value} """)



print(print_son())
print_key_val()
print_key_val2()



