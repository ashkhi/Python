number = abs(int(input("Enter a number: ")))
numOfDigits = 1

while(number >= 10):
    number /= 10
    numOfDigits += 1

print("Number of digits: ", numOfDigits)