import random

birthdayList = []
for i in range(40):
    birthdayList.append(random.randint(1, 366))

birthdayList.sort()
print(birthdayList)

repFlag = False
for i in range(len(birthdayList)-2):
    if(birthdayList[i] == birthdayList[i+1]):
        repFlag = True
        print("Repetition of ", birthdayList[i], birthdayList[i+1])
        print("Birthday paradox holds")
        break

if(not repFlag):
    print("No repetition : Birthday paadox fails")