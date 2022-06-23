example = '2022-03-31T07:40:45.000Z'

# step-size[start, stop, step size]

# print start to end
print(example[::])
print(example[::4])

print(example[0:8])
print(example[:19:])

# reverse
print(example[::-1])

# String concatecation - use for my time
subset_a = example[:10]
subset_b = example[11:19]
subset_c = subset_a + ' ' + subset_b

print(subset_a)
print(subset_b)
print(subset_c)


