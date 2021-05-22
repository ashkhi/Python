email = str(input("enter email id: "))

for i in range(len(email)):
    if(email[i] == '@'):
        break
    print(email[i], end="")

print("\n")
for i in range(len(email)):
    if(email[i] == '@'):
        print("\n")
        continue
    print(email[i], end="")

# pass is a keyword for doing nothig
# it is not same as a comment
# after executing 'pass', python interpreter does nothing
print("\n")
for i in range(11):
    if(i % 3 == 0):
        print(i, end=' ')
    else:
        pass