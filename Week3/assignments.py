'''
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
'''

'''
number = abs(int(input()))

sum = 0

for i in range(1, number+1):
    sum = sum + (((number + 1) - i) * i)

print(sum)
'''

'''
number = abs(int(input()))

for i in range(2, number+1):
    if(number % i == 0):
        print(i)
        number = number // i
        i = 2
'''

'''
originalStr = str(input())

lowerStr = originalStr.lower()
lowerStrList = []
n = len(lowerStr)

for i in range(n):
    if(lowerStr[i].isalpha()):
        lowerStrList.append(lowerStr[i])

n = len(lowerStrList)
for i in range(n):
    for j in range(n - i - 1):
        if(lowerStrList[j] > lowerStrList[j + 1]):
            lowerStrList[j], lowerStrList[j + 1] = lowerStrList[j + 1], lowerStrList[j]

sortedStr = ""
for i in range(n):
    sortedStr += lowerStrList[i]

print(sortedStr)
'''

'''
from math import sqrt

inputStr = str(input())
num = len(inputStr)
listOfPrimes = []

for i in range(2, num):
    j = 2
    prime = True
    while(j <= sqrt(i)):
        if((i % j) == 0):
            prime = False
            break
        j += 1
    if(prime):
        listOfPrimes.append(i)
        prime = True

primePos = len(listOfPrimes)
for i in range(primePos):
    print(inputStr[listOfPrimes[i]])
'''

'''
inputPhoneNum = str(input())

invalidNum = False

for i in inputPhoneNum:
    if(not i.isdigit()):
        invalidNum = True

if(not invalidNum and len(inputPhoneNum) != 10):
    invalidNum = True

if(not invalidNum and (inputPhoneNum[0] not in ['6', '7', '8', '9'])):
    invalidNum = True

if(not invalidNum):
    digitCountMax = 7
    for i in range(10):
        digitCount = inputPhoneNum.count(inputPhoneNum[i])
        if(digitCount > digitCountMax):
            invalidNum = True
            break

if(not invalidNum):
    for i in range(10):
        inputPhoneNumSubStr = inputPhoneNum[i:i+5]
        if(inputPhoneNumSubStr.count(inputPhoneNumSubStr[0]) == 5):
            invalidNum = True

if(not invalidNum):
    print("valid")
else:
    print("invalid")
'''