num = abs(int(input("Enter dim of matrix :")))

print("All the matrix positions :")

for i in range(num):
    for j in range(num):
        print("(",i, ",", j, ")", end='\t')
    print("\n")