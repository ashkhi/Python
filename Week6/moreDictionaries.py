# dictionaries can have all the elements as keys that are immutable e.g. bool, float, int, string
# dictionaries can not have any element as key that is mutable e.g. list, tuples, dicts
# always should have a key : value format
# the type of key should always be unhashable

# dict can have keys of different types
d1 = {}
d1['A'] = 100
d1['B'] = 200
d1[1] = 300
print(d1[1])

# iterate over a dict
d2 = {'k1': 1, 'k2': 2, 'k3':3}
for key in d2:
    print(key, d2[key])

# we can use following three methods of the dict
l1 = d2.keys()
print(l1, type(l1))

l2 = d2.values()
print(l2, type(l2))

l3 = d2.items()
print(l3, type(l3))