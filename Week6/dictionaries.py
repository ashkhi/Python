# initizlize a dictionary
d1 = {}
print(type(d1))

d1["A"] = 1
d1["B"] = 2
d1["c"] = 3

print(d1)

# dictionary access
# one can access the dictionary using a key to get the respective value
print(d1["A"])

# one can modify the values of dictionary using the respective keys
d1["A"] += 1
print(d1["A"])

# the dictionary can have a list as its value
d1["D"] = [1,2,3]
print(d1["D"])

# how to create a dictionary using lists
l1 = ["A", "B", "C", "D", "E", "A", "D", "C", "B", "B"]
s1 = set(l1)
print(s1)

d1 = {}

for i in s1:
    d1[i] = 0

for i in l1:
    d1[i] += 1

print(d1)