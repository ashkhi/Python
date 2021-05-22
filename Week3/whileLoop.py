# while loop is a condition based looping structure
# while the condition evealuates to true the loop would run
# when the conition evaluates to false, the loop would break
# we can have multiple statements inside the while loop

# while loop should be used whne we do not have any idea
# how many times the loop needs to executed

# problem like password validation can be solved using
# while loop till the correct password is entered

print("Please enter your user name :")
userName = str(input())

actualPassword = userName + "123@"

print("Please enter your password :")
password = str(input())

while(actualPassword != password):
    print("Incorrect password, please renenter the same")
    password = str(input())

print("Password validation complete, you have been looged in.")