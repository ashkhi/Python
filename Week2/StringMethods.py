# there are multiple methods those can be applied to strings to manipulate the strings
a = "pytHoN sTriNg MethODs"
b = a.lower()
print(b)
c = a.upper()
print(c)
d = a.capitalize() # only the first char of the statement is in upper case
print(d)
e = a.title() # first cahr of every word is converted to upper case
print(e)
f = a.swapcase()
print(f)

print(b.islower())
print(c.isupper())
print(e.istitle())

x = '123'
y = 'abc'
z = 'abc123'
print(x.isdigit())
print(y.isalpha())
print(z.isalnum())
z += '!@#$'
print(z)
print(z.isalnum())

# strip methods remove the chars only from the ends of the strings
# if teh char appears in the middle of the string, it would not be removed
a = "-----python-programming-----"
print(a.strip("-"))
print(a.lstrip("-"))
print(a.rstrip("-"))

print(b.startswith("P"))
print(b.startswith("p"))
print(b.endswith("S"))
print(b.endswith("s"))

print(b.count("s"))
print(b.index("s"))
print(b.replace("p", "P"))

