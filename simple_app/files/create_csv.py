# Create a file in my present directory
# w- writing, a- appending to file, r- reading from file, r+, reading and writing from file

# I am doing a conversion on line 9... So converting the object I passed in into a string


def create_file(uuid, name, email):
    file = open('./data.csv', 'a')
    return file.write(str({uuid, name, email}))


create_file("id", "name", "email")
create_file("1", "Bisi", "bisi@gmail.com")
create_file("2", "Dayo", "dayo@gmail.com")
