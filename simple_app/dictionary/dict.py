# This is object in javaScript
countries = {'Nigeria', 'Austria', 'Denmark'}
countriess = ['Nigeria', 'Austria', 'Denmark']


def get_countries():
    for cou in countries:
        return cou


# print(get_countries())


def create_dict():
    """ Function to return dict """
    your_dict = {}
    for i in range(10):
        your_dict[i] = str(i)
    return your_dict


def create_list():
    new_list = []
    for cou in countriess:
        new_list.append(cou)
    return new_list



# print(create_dict())


print(create_list())






