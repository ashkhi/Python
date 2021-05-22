for i in 'we are in question one':
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    print(i, end="")

print("\n--------------------")
str = "Hello Python!\n"
print(str * 10)

print("--------------------\n")
x = int(input())
i = 0
while x % 10 ** i != x:
    i = i + 1
print(i)

print("--------------------\n")
a = 0
for i in range(10):
    for j in range(10):
        a += 1
        break
    a += 1
    break

print(a)

print("--------------------\n")
for i in range(10, 0, 1):
    print(i)

print("--------------------\n")
a = 0
for i in range(1231, -12420, -7):
    a += 1
    print(i, a)

print("--------------------\n")
a = 0
b = 1
for i in range(10):
    a, b = b, a + b
print(a)

a = 0
b = 1
for i in range(10):
    a = b
    b = a + b
print(a)