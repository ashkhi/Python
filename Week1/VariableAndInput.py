# some mixing of variables and how to use them in print statements
print("Hello,", "what is your name?")
name = str(input())

print("Hi", name, "Where are you from?")
place = str(input())

# try to find out how to avoid a space between last word and ..
# hint : escape character
print("Great!", name, "hope all is well in", place, "..")

print("Could you please share your age?")
age = int(input())
print("Thanks", name, "good to know that you are", age, "years old")