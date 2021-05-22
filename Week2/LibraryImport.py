import random

heads = tails = 0

for i in range(1000):
    num = random.random()

    if(num < 0.5):
        heads += 1
    else:
        tails += 1

print("Heads count : ", heads)
print("Tails count : ", tails)

# there are different ways one can import a library
import calendar # builds and imports
import calendar as c # builds and imports into var c
from calendar import * # imports everything from lib
from calendar import month # imports certain functions
from calendar import month, calendar # imports multiple functions needed
from calendar import month as m # imports needed function as var