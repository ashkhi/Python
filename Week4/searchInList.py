import random

numList = []

for i in range(10000):
    numList.append(random.randint(1, 10000))

inputNum = 0
inputNum = int(input("Enter a number to search, -1 to exit :"))

while(inputNum != -1):
    searchFlag = False
    for i in range(len(numList)):
        if(numList[i] == inputNum):
            searchFlag = True
            print("Number found at position : ", i)
            break
    
    if(not searchFlag):
        print("Number not in the list")

    inputNum = int(input("Enter a number to search, -1 to exit :"))