import random

numList = []

for i in range(10):
    numList.append(random.randint(1, 10))

sortedList = []
minElement = numList[0]

while(len(numList) != 0):
    minElement = numList[0]
    for i in range(len(numList)):
        if(minElement > numList[i]):
            minElement = numList[i]

    sortedList.append(minElement)
    numList.remove(minElement)

print(sortedList)