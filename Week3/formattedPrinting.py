for i in range(10):
    print(i, end=' ')
print("\n")

d = 16
m = 12
y = 1987

print("My DOB is :",end = ' ')
print(d, m, y, sep = '-')
print("\n")

# default print statement
# cominiation of variables and strings
for i in range(1, 11):
    print(d, "X", i, "=", (d * i))
print("\n")

# using format specifier f"string"
# all the variables go inside {}
for i in range(1, 11):
    print(f"{d} X {i} = {d * i}")
print("\n")

# using "string".format specifier
# all the variables go in .format()
# numbers are used to indicate the variable position
for i in range(1, 11):
    print("{0} X {1} = {2}".format(d, i, (d * i)))
print("\n")

# using "string" % () specifier
# the variables go inside ()
for i in range(1, 11):
    print("%d X %d = %d" % (d, i, (d * i)))
print("\n")

# using format specifier
for i in range(1, 11):
    print(f"{d} / {i:2d} = {(d / i):.3f}")
print("\n")

for i in range(1, 11):
    print("{0} / {1:2d} = {2:.3f}".format(d, i, (d / i)))
print("\n")

for i in range(1, 11):
    print("%d / %2d = %.3f" % (d, i, (d / i)))
print("\n")