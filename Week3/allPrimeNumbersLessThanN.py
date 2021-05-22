from math import sqrt

num = abs(int(input("Enter a number :")))
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

print(listOfPrimes)