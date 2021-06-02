'''
string = "this is old python course"
print(string.count("is"))
print(string.replace("old", "new"))
print(string.index("python"))
print(string.startswith("this"))
print(string.isalnum())
print(string.title())
print(string.strip("this is old"))
'''

'''
a = 22
b = 2
c = -2
d = 2
for num in range(a, b, c):
    num = num+d
    print(num)
'''

'''
x = ["python",]
for num in x:
    print(num, end="")
'''

'''
list_1 = ["I play", "You play"]
list_2 = ["Badminton", "Cricket"]
print("{a} {b}".format(a = list_1[0], b = list_2[0]))

print(list_1[0] + " " + list_2[0])

for x in list_1[:-1]:
    for y in list_2[:-1]:
        print(x, y)
'''

'''
L = [1,2,3,4,5]
s = 0
for x in L:
    s += x

flag = False
y = -1
for x in L:
    if x * len(L) == s:
        flag = True
        y = x
        break
'''

'''
x = [1,2,3]

dp1 = 0
for e in x:
    dp1 += e * e
print(dp1)

dp2 = 0
for i in range(len(x)):
    dp2 += x[i] ** 2
print(dp2)

dp3 = 0
for i in range(x):
    dp3 += x[i] * x[i]
print(dp3)

i, dp4 = 0, 0
while i <= len(x):
    dp4 += x[i] ** 2
    i += 1
print(dp4)

i, dp5 = 0, 0
while i < len(x):
    dp5 += x[i] ** 2
    i += 1
print(dp5)
'''

'''
import math

ip = str(input())
inputNum = 0
sum = 0
count = 0
numbers = []

while(ip != "END"):
    inputNum = float(ip)
    numbers.append(inputNum)
    sum += inputNum
    count += 1
    ip = str(input())

mean = sum / count
sqSum = 0
for i in range(count):
    sqSum += ((numbers[i] - mean) ** 2)

standardDev = math.sqrt(sqSum / (count - 1))
print("{0:.2f}".format(standardDev))
'''

'''
inputStr = str(input())

openCount = 0
count = 0
i = 0
inputLen = len(inputStr)
incorectBrackets = False

while(count > -1 and i < inputLen):
    ch = inputStr[i]
    i += 1
    if(ch == '('):
        if(openCount != count):
            openCount = count
        count += 1
    if(ch == ')'):
        if(count == 0):
            print("Not matched")
            incorectBrackets = True
            break
        else:
            count -= 1

if((not incorectBrackets) and count == 0):
    print(openCount+1)
if((not incorectBrackets) and count != 0):
    print("Not matched")
'''