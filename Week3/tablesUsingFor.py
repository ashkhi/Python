num = abs(int(input("Enter a number: ")))

for i in range(num):
    print("\n\nTable of", (i + 1))
    for j in range(10):
        print((i + 1) * (j + 1), end=" ")