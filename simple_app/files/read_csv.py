def read_file():
    file = open('./data.csv', 'r')
    return file.read()


def read_line():
    file = open('./data.csv', 'r')
    for line in file:
        return line


def read_lines():
    file = open('./data.csv', 'r')
    return file.readlines()


# print(read_file())
# print(read_line())
print(read_lines())
