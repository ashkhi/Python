# having print and input under same statement
# input accepts only one argument
name = str(input("Hello, what is your name? : "))

# you can add strings and send them as one argument for input
place = str(input("Hi " + name + ", where are you from? : "))

print("Great!", name, "hope all is well in", place, "..")

age = int(input("Could you please share your age? : "))

print("Thanks", name, "good to know that you are", age, "years old")

# here the radius and area are variables as they can change the value
# however 3.14 is a literal as that never changes the value
radius = int(input("Enter radius of the circle : "))
area = 3.14 * radius * radius
print("Area of the circle is : ", area)