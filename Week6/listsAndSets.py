import sys

# initializing a list
l1 = [1,2,3,4,5]
print(l1)
print(type(l1))
l2 = list(range(100))
print (l2)
print(type(l2))

# to search in list we can use 'in' operator
# searching in the list is slow compared to set, using 'in'
# size of list is very small compared to set
bigList = list(range(1000000))
print(-1 in bigList)
print(sys.getsizeof(bigList))

# initializing a set
s1 = {1,2,3,4,5}
print(s1)
print(type(s1))
s2 = set(range(100))
print(s2)
print(type(s2))

# to search in set we can use 'in' operator
# searching in the set is fast compared to list, using 'in'
# size of set is very big compared to list
bigSet = set(range(1000000))
print(-1 in bigSet)
print(sys.getsizeof(bigSet))

# there is a size and search efficiency trade off between list and set

# both list and set are heterogeneous structures
l1.append("Hi")
s1.add("Hi")

print(l1)
print(s1)