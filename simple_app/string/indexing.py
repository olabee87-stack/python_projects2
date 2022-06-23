# Indexing - Grabbing a singe character
# Slicing - Grabbing a subsection of that character
# Step size - Jumping indexes

def print_wrd():
    my_str = 'abcdefghijk'

    # start from index 1 and keep printing every third letter (step size)
   # return my_str[1::3]

    # start from index 2 and print to the end
    #return my_str[2:]

    # grab the first 4 letters - won't indlude the 4th index
    # return my_str[0:4]

    # grab the first 3 letters and stop at the 4th (won't grab the 4th index)
    # return my_str[:3]

    # grab the first 'def' letters
    return my_str[3:6]


print(print_wrd())