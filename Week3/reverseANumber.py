number = int(input("Enter a number: "))

neg = False
if(number < 0):
    neg = True
    number = abs(number)

reversedNumber = 0

while(number >= 10):
    rem = number % 10
    number = number // 10
    reversedNumber = (10 * reversedNumber) + rem

reversedNumber = (10 * reversedNumber) + number

if(neg):
    reversedNumber *= -1

print("Reversed number: ", reversedNumber)