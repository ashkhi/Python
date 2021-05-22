#
a = 10
b = 20.5
c = "Hello"
d = 'A'

print("a is of type : ", type(a))
print("b is of type : ", type(b))
print("c is of type : ", type(c))
print("d is of type : ", type(d))

l = [10, 20, 30]
print("0th entry in the sequence is : ", l[0])
print("1st entry in the sequence is : ", l[1])
print("2nd entry in the sequence is : ", l[2])

print("l is of type : ", type(l))
print("0th element of list is of type : ", type(l[0]))

# True and False have to start with CAP letter 
b1 = True
b2 = False
print("b1 is of type : ", type(b1))
print("b2 is of type : ", type(b2))

# data type conversion to int
a = int(20.5)
b = int("10")
print("a is :", a, "has type : ", type(a))
print("b is :", b, "has type : ", type(b))

# data type conversion to float
a = float(20)
b = float("10.5")
print("a is :", a, "has type : ", type(a))
print("b is :", b, "has type : ", type(b))

# data type conversion to string
a = str(10)
b = str(20.5)
print("a is :", a, "has type : ", type(a))
print("b is :", b, "has type : ", type(b))

# data type conversion to bool
a = bool(10)
b = bool(20.5)
c = bool(0)
d = bool(0.000000001)
e = bool(0.0)
f = bool("Hi")
g = bool("")
print("a is :", a, "has type : ", type(a))
print("b is :", b, "has type : ", type(b))
print("c is :", c, "has type : ", type(c))
print("d is :", d, "has type : ", type(d))
print("e is :", e, "has type : ", type(e))
print("f is :", f, "has type : ", type(f))
print("g is :", g, "has type : ", type(g))