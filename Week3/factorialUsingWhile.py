print("Enter a number:")
number = int(input())

factorial = 1

while(number >= 1):
    factorial *= number
    number -= 1

if(number < 0):
    print("Factorial is not defined")
else:
    print("Factorial of number :", factorial)