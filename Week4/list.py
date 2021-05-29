l = [1, 2, 3, 4]
print(l)

# append adds an element at the end
l.append(5)
l.append(5)
print(l)

# remove will remove the element from the list
l.remove(1)
print(l)

# if there are multiple elements matching
# remove would remove the first occurance of the element
l.remove(5)
print(l)

# remove can not remove the elemnt that is not in list
# the code would show an error message
#l.remove(100)
print(l)

# list can have another list as its member
# it is called as list of lists
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]
m = []
m.append(r1)
m.append(r2)
m.append(r3)
print(m)

# we can also access an element of list using the list index
print(m[0])
print("Diagonal elements : ", m[0][0], m[1][1], m[2][2])