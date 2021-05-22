# rules for naming variables
# variables can have A-Z, a-z, 0-9 and _
# variables can start with alphabet or _
# variable names are case sensetive
a = 10
a1 = 20
a_1 = 30
# 1a = 40 -> not allowd as starts with 1
_1a = 40

hi = 50
HI = 60
Hi = 70

print(a, a1, a_1, _1a, hi, HI, Hi)

# multiple assignments
# sequence is important
x = y = 10
print(x, y)

x, y = 1, 2
print(x, y)

y, x = x, y
print(x, y)

#deleting a variable
x = 10
print(x)
del x
# print(x) -> will give an error, 'x is not defiled' as that is deleted

# shorthand operators
# we can write prefix notation
x = 0
x += 1
x *= 2
x -= 1
x /= 2
print(x)

# 'in' operator
print('A' in "A beatiful day")
a = print('B' in "A beatiful day")
print(a)
print(type(a))

# chaining operator
# when multiple relational operators are in chain with one another
x = 5
print(1 < x < 10)
print(10 < x < 20)
print(5 <= x > 10)