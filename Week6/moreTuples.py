# packing
t = 1, 2, 3
print(t, type(t))

# unpacking
x, y, z = t
print(x, y, z)

# packing and unpacking while swapping
x = 10
y = 20
x, y = y, x

# initializing a single element tuple
l = [10]
print(l, type(l))

t1 = (10) # without comma it would be treated as simple int
print(t1, type(t1))

t2 = (10,) # this comma is importnant
print(t2, type(t2))

# modification of the tuple elements by wrapping then in list
t3 = ([1, 2], ['A', 'B'])
print(t3, type(t3))
t3[1][0] = 10
print(t3)