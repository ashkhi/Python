# init
l1 = [1,2,3]
l2 = [10,20,30]

# addition of lists
print(l1 + l2)
print(l2 + l1)

# multiplication of lists
l3 = [0] * 10
print(l3)
l4 = [1,2,3] * 3
print(l4)

# equality operators
l5 = [1,2,3]
print(l1 == l5)
print(l2 == l5)

# other equality operators
print(l1 < l5)
print(l2 > l5)
print([2,3] > [3])
print([] < [0])

# lists are mutable. One can change the elements of the list

l6 = [2,1,4,7,3,2,6,4,6]
l6.reverse()
print(l6)
l6.sort()
print(l6)
print(l6.pop())