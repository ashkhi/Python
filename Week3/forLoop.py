# for loop is a condition based looping structure
# if for condition evealuates to true the loop would run
# when the conition evaluates to false, the loop would break
# we can have multiple statements inside the for loop

# for loop should be used whne we have idea about 
# how many times the loop needs to executed
# the for loop is range based loop

# if we want to do a same task N times, we should use for loop
# for loop counter starts from 0

for i in range(10):
    print("Hello")

print("------------------")

num = int(input("Enter a number : "))
for i in range(num):
    if(i % 2):
        print(i, "-> Odd")
    else:
        print(i, "-> Even")

print("------------------")

# variations of for statement with start and end of range
# efault start value for range is 0
for i in range(1, 10):
    if(i % 2):
        print(i, "-> Odd")
    else:
        print(i, "-> Even")

print("------------------")

# variations of for statement with step
# default step is always 1
for i in range(1, 10, 3):
    if(i % 2):
        print(i, "-> Odd")
    else:
        print(i, "-> Even")

print("------------------")

# variations of for statement with decreasing counter
for i in range(10, -1, -1):
    if(i % 2):
        print(i, "-> Odd")
    else:
        print(i, "-> Even")

print("------------------")

# variations of for statement without range
for i in "India":
    print(i)

print("------------------")

for i in ["India", "US", "China", "UK"]:
    print(i)