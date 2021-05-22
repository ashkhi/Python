# arithmetic operators +, -, *, /
a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = [10, 20, 30]
b = [30, 40, 50]
print(a+b)
# -, * and / do not work on lists
# print(a-b)
# print(a*b)
# print(a/b)

# operator precedence
a = 10
b = 20
c = a + a * b
print(c)
c = ((a + a) * b)
print(c)

# floor division //, modulo % and expo **
print(7 // 3)
print(7 % 3)
print(7 ** 3)

# relational operators <, >, <=, >=, ==, !=
print(5 < 10)
print(5 > 10)
print(5 <= 5)
print(5 >= 5)
print(5 == 5)
print(5 != 5)

# logical operators and, or, not
print(True and False)
print(True or False)
print(not True)
print(not False)