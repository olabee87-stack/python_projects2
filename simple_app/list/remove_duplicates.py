data = [50, 70, 70, 80, 50, 90, 90]

def remove_duplicates(my_list):
    unique_list = []

    for el in my_list:
        if el not in unique_list:
            unique_list.append(el)
    return unique_list


print(remove_duplicates(data))