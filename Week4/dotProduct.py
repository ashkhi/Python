import random

dimOfVect = abs(int(input("Enter the dim of the vectors : ")))

vect1 = []
vect2 = []

for i in range(dimOfVect):
    vect1.append(random.randint(1, 10))

for i in range(dimOfVect):
    vect2.append(random.randint(1, 10))

dotProduct = 0
for i in range(dimOfVect):
    dotProduct += (vect1[i] * vect2[i])

print("Dot product of vect1 ", vect1, " and ", vect2, " is : ")
print(dotProduct)