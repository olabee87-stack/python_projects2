import pandas as pd

dataset = {
    'animal': ['dog', 'tiger', 'lion', 'zebra'],
    'sounds': ['woof', 'snarl', 'roar', 'whine']
}

new_list = pd.DataFrame(dataset)

print(new_list)

