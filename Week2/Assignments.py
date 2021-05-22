'''
a, b, c, d = input()
print(a)
print(b)
print(c)
print(d)
'''

'''
x = bool(False)
print(x)
print(type(x))
'''

'''
x = bool(input())
print(x)
'''

'''
a = int(input())
# a = int(input())
b = int(input())
if a > 0:
    if b < 0:
        print('ok')

if int(input()) > 0 and int(input()) < 0:
    print('ok')
'''

'''
a = False
b = False
c = True

if a:
    if b:
        print('okb')
    if c:
        print('okc')

if a and b or c:
    print('ok2')
'''

'''
x = int(input())
y = int(input())
z = int(input())

if x > 0 or y > 0 or z > 0:
    if(x > 0 and y > 0) or (y > 0 and z > 0) or (z > 0 and x > 0):
        if x > 0 and y > 0 and z > 0:
            print('p3')
        else:
            print('p2')
    else:
        print('p1')

if x < 0 or y < 0 or z < 0:
    if(x < 0 and y < 0) or (y < 0 and z < 0) or (z < 0 and x < 0):
        if x < 0 and y < 0 and z < 0:
            print('n3')
        else:
            print('n2')
    else:
        print('n1')
'''

'''
import math as ma
print(ma.sqrt(16))
'''

'''
dept = input()
course = input()
prefix = input()
name = input()
roll = input()
name = prefix + " " + name
libid = dept[0] + course[0] + roll
print("student record : ")
indent = '    '
print(indent + "dept:", dept)
print(indent + "name:", name)
print(indent + "roll:", roll)
print(indent + "libid:", libid)
'''

'''
s = "abcd(efgh(ijkl}{{}))"
match = False
if s.count('(') == s.count(')'):
    if s.count('[') == s.count(']'):
        if s.count('{') == s.count('}'):
            match = True

print(match)
'''

'''
s1 = int(float(input()))
s2 = int(float(input()))
s3 = int(float(input()))

if((s1 <= 0 or s2 <= 0 or s3 <= 0) or (s1 == s2 and s2 == s3)):
    print("NO")
elif(s1 > s2):
    if(s1 > s3):
        if((s1 * s1) == ((s2 * s2) + (s3 * s3))):
            print("YES")
        else:
            print("NO")
    else:
        if(s1 == s3):
            print("NO")
        elif((s3 * s3) == ((s2 * s2) + (s1 * s1))):
            print("YES")
        else:
            print("NO")
else:
    if(s2 > s3):
        if(s1 == s2):
            print("NO")
        elif((s2 * s2) == ((s1 * s1) + (s3 * s3))):
            print("YES")
        else:
            print("NO")
    else:
        if(s2 == s3):
            print("NO")
        elif((s3 * s3) == ((s2 * s2) + (s1 * s1))):
            print("YES")
        else:
            print("NO")
'''

'''
t = int(float(input()))

if(t < 0 or t > 23):
    print("INVALID")
elif(t >= 0 and t <= 5):
    print("NIGHT")
elif(t >= 6 and t <= 11):
    print("MORNING")
elif(t >= 12 and t <= 17):
    print("AFTERNOON")
else:
    print("EVENING")
'''

'''
evenCount = 0
oddCount = 0

e1_ID = int(input())
if(e1_ID % 2 == 0):
    evenCount += 1
else:
    oddCount += 1

e2_ID = int(input())
if(e2_ID % 2 == 0):
    evenCount += 1
else:
    oddCount += 1

e3_ID = int(input())
if(e3_ID % 2 == 0):
    evenCount += 1
else:
    oddCount += 1

e4_ID = int(input())
if(e4_ID % 2 == 0):
    evenCount += 1
else:
    oddCount += 1

e5_ID = int(input())
if(e5_ID % 2 == 0):
    evenCount += 1
else:
    oddCount += 1

if(e1_ID <= 0 or e2_ID <= 0 or e3_ID <= 0 or e4_ID <= 0 or e5_ID <=0):
    print("NO")
elif((e1_ID == e2_ID or e1_ID == e3_ID or e1_ID == e4_ID or e1_ID == e5_ID) or
    (e2_ID == e3_ID or e2_ID == e4_ID or e2_ID == e5_ID) or
    (e3_ID == e4_ID or e3_ID == e5_ID) or
    (e4_ID == e5_ID)):
    print("NO")
elif(evenCount == 5 or oddCount == 5):
    print("YES")
else:
    print("NO")
'''

'''
inputStr = str(input())
outputStr = ""

if(inputStr.count('a') > 0 or inputStr.count('A') > 0):
    outputStr += "a"
if(inputStr.count('e') > 0 or inputStr.count('E') > 0):
    outputStr += "e"
if(inputStr.count('i') > 0 or inputStr.count('I') > 0):
    outputStr += "i"
if(inputStr.count('o') > 0 or inputStr.count('O') > 0):
    outputStr += "o"
if(inputStr.count('u') > 0 or inputStr.count('U') > 0):
    outputStr += "u"

print(outputStr)
'''

'''
p1_name = str(input())
p1_dob = str(input())
p2_name = str(input())
p2_dob = str(input())

p1_year = p1_dob[6:10]
p2_year = p2_dob[6:10]

if(p1_year != p2_year):
    if(p1_year < p2_year):
        print(p2_name)
    else:
        print(p1_name)
else:
    p1_mon = p1_dob[3:5]
    p2_mon = p2_dob[3:5]

    if(p1_mon != p2_mon):
        if(p1_mon < p2_mon):
            print(p2_name)
        else:
            print(p1_name)
    else:
        p1_day = p1_dob[0:2]
        p2_day = p2_dob[0:2]

        if(p1_day != p2_day):
            if(p1_day < p2_day):
                print(p2_name)
            else:
                print(p1_name)
        else:
            if(p1_name < p2_name):
                print(p1_name)
            else:
                print(p2_name)
'''

'''
pwd = str(input())
pwd = pwd.lower()

if(len(pwd) < 8 or len(pwd) > 32):
    print("False")
elif(not(pwd[0].isalpha())):
    print("False")
elif(('/' in pwd) or ('\\' in pwd) or ('=' in pwd) or ('\'' in pwd) or ('\"' in pwd) or (' ' in pwd)):
    print("False")
else:
    excCount = pwd.count('!')
    atCount = pwd.count('@')
    hashCount = pwd.count('#')
    dolCount = pwd.count('$')
    modCount = pwd.count('%')
    capCount = pwd.count('^')
    andCount = pwd.count('&')
    usCount = pwd.count('_')
    starCount = pwd.count('*')
    dotCount = pwd.count('.')

    oneCount = pwd.count('1')
    twoCount = pwd.count('2')
    threeCount = pwd.count('3')
    fourCount = pwd.count('4')
    fiveCount = pwd.count('5')
    sixCount = pwd.count('6')
    sevenCount = pwd.count('7')
    eightCount = pwd.count('8')
    nineCount = pwd.count('9')
    zeroCount = pwd.count('0')

    aCount = pwd.count('a')
    bCount = pwd.count('b')
    cCount = pwd.count('c')
    dCount = pwd.count('d')
    eCount = pwd.count('e')
    fCount = pwd.count('f')
    gCount = pwd.count('g')
    hCount = pwd.count('h')
    iCount = pwd.count('i')
    jCount = pwd.count('j')
    kCount = pwd.count('k')
    lCount = pwd.count('l')
    mCount = pwd.count('m')
    nCount = pwd.count('n')
    oCount = pwd.count('o')
    pCount = pwd.count('p')
    qCount = pwd.count('q')
    rCount = pwd.count('r')
    sCount = pwd.count('s')
    tCount = pwd.count('t')
    uCount = pwd.count('u')
    vCount = pwd.count('v')
    wCount = pwd.count('w')
    xCount = pwd.count('x')
    yCount = pwd.count('y')
    zCount = pwd.count('z')

    specialCount = 0
    specialCount = specialCount + excCount + atCount + hashCount + dolCount + modCount + capCount + andCount + usCount + starCount + dotCount

    numCount = 0
    numCount = numCount + oneCount + twoCount + threeCount + fourCount + fiveCount + sixCount + sevenCount + eightCount + nineCount + zeroCount

    alphaCount = 0
    alphaCount = alphaCount + aCount + bCount + cCount + dCount + eCount + fCount + gCount + hCount + iCount + jCount + kCount + lCount + mCount + nCount + oCount + pCount + qCount + rCount + sCount + tCount + uCount + vCount + wCount + xCount + yCount + zCount

    totalCount = specialCount + numCount + alphaCount
    pwdlength = len(pwd)

    if(pwdlength == totalCount):
        print("True")
    else:
        print("False")
'''