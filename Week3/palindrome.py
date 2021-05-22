originalNumber = abs(int(input("Enter a number: ")))
number = originalNumber

reversedNumber = 0

while(number >= 10):
    rem = number % 10
    number = number // 10
    reversedNumber = (10 * reversedNumber) + rem

reversedNumber = (10 * reversedNumber) + number

if(reversedNumber == originalNumber):
    print("Its a palindrome")
else:
    print("Not a palindrome")