'''
def f(a=1, b=2, c, d):
    return a + b + c + d
print(f(0, 0, 3, 4))
SyntaxError: non-default argument follows default argument
'''

'''
def f(a, b, c=10, d=19):
    return a + b + c + d
print(f(1, 2))
'''

'''
def f(a, b, c=10, d=19):
    return a + b + c + d
print(f(c=1, d=2, 1, 2))
SyntaxError: positional argument follows keyword argument
'''

'''
def assert(x):
    return x == int(str(x))
assert(1)
SyntaxError: invalid syntax
'''

'''
def f():
    return x
x = 10
print(f())
'''

'''
def f(x):
    print("F", x)
    if x == 0:
        return x
    elif  x > 5:
        return g(x - 2)
    else:
        return f(x - 1)

def g(x):
    print("G", x)
    if x == 0:
        return x
    elif  x > 5:
        return f(x - 1)
    else:
        return g(x - 2)

x = 8
print(g(x))
'''

'''
import random
x = random.random()
for i in range(4):
    print(x)
'''

'''
import math
print(math.hypot(-4, -3))
'''

'''
def f():
    for i in range (n):
        print(i)

n = 5    
f()
'''

'''
import math
s = math.sqrt
print(s(64))
'''

'''
def perfect_number(num):
    sum = 0
    
    for i in range (1, num):
        if(num % i == 0):
            sum += i

    if(sum == num):
        return True
    else:
        return False

print(perfect_number(28))
'''

'''
def user_score(read_count=0, reply_count=0, new_post_count=0):
    if(read_count < 0):
        read_count = 0
    if(reply_count < 0):
        reply_count = 0
    if(new_post_count < 0):
        new_post_count = 0

    score = (read_count * 1) + (reply_count * 3) + (new_post_count * 5)
    if (score > 50):
        return "Leader"
    else:
        return "Basic"

print(user_score(10))
'''

'''
def check_leap_year(year):
    if(year < 1600 or year > 9999):
        return False
    else:
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            if(year % 4 == 0):
                return True
            else:
                return False

print(check_leap_year(2020))
'''

'''
def is_magic(mat):
    dim = len(mat)

    sum = 0
    for i in range(dim):
        sum += mat[0][i]
    
    for i in range(dim):
        rowSum = 0
        for j in range(dim):
            rowSum += mat[i][j]
        if(rowSum != sum):
            return "NO"
    
    for i in range(dim):
        colSum = 0
        for j in range(dim):
            colSum += mat[j][i]
        if(colSum != sum):
            return "NO"
    
    d1Sum = 0
    d2Sum = 0
    for i in range(dim):
        d1Sum += mat[i][i]
        d2Sum += mat[i][(dim - 1) - i]
    
    if(d1Sum == sum and d2Sum == sum):
        return "YES"
    else:
        return "NO"

print(is_magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
'''

'''
def process():
    firstMin = 0
    secondMin = 0
    while(True):
        firstMin = board_min()
        secondMin = board_min()
        board_erase(firstMin)
        if(board_isEmpty()):
            break
        else:
            secondMin = board_min()
            board_erase(secondMin)
    
        absoluteDiff = abs(secondMin - firstMin)
        board_write(absoluteDiff)
    return firstMin
'''