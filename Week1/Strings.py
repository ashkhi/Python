s = "coffee"
t = "bread"
print(s + t)

# access and slice
# print(s[10]) index out of range
print(s[1:3])
print(s[1:7])

# multiplication on strings
a = "Hello"
print(5 * a)
print(5 * a[1])

print("India" == "india")
print("apple" > "one")
print("four" < "one")
print("a1" > "a2")
print("a11" > "a1")

# negative indices
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
# print(a[-6]) string index is out of range

#length of string
print(len(s + t))
print(s[len(s) - 1])