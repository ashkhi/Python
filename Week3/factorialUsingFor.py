number = int(input("Enter a number :"))

factorial = 1

if(number < 0):
    print("Factorial is not defined")
else:
    for i in range(number, 1, -1):
        factorial *= i
    print("Factorial of number :", factorial)