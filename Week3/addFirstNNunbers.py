num = abs(int(input("Enter a number: ")))
sum = 0

for i in range(num):
    sum += i

print("Sum of first", num, "natural numbers starting at 0 is :", sum)

sum = 0

for i in range(num):
    sum += (i + 1)

print("Sum of first", num, "natural numbers starting at 1 is :", sum)