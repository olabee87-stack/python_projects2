import pandas as pd

dataset = {
    'family': ['Dupe', 'Ara', 'Bayo', 'Ade', 'Bola'],
    'listings': [33, 9, 30, 37, 39]
}

my_list = pd.DataFrame(dataset)

print(my_list)