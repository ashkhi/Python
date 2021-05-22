# if statement is a conditional block
# indentation plays important role
# the block can have multiple statements

a = int(input("Enter an integer : "))
print("The following code would tell you if the next number is even-odd")
if a % 2 == 0:
    a += 1
    print("Number", a, "is odd.")
else:
    a += 1
    print("Number", a, "is even.")

print("This is from common part of the code.")

# else-if part
# the following code would help segragate the numbers based on units place
# ends in 0
# ends in 5
# ends in anything else
a = int(input("Enter an integer : "))
unitsPlace = a % 10

if(unitsPlace == 0):
    print("Number", a, "ends in 0")
elif(unitsPlace == 5):
    print("Number", a, "ends in 5")
else:
    print("Number", a, "ends in anything else")