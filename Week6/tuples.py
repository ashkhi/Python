# tuples are a light weight structures
# tuples are very similar to lists

# initializing a tuple
t1 = (1,5,3,2,4,1)
print(t1)
print(type(t1))

t2 = tuple(range(10))
print(t2)
print(type(t2))

# out of the box tuples have just two properties
# count and index
print(t1.count(1)) # tells the count of the element
print(t1.index(3)) # tells at what index the element is

# tuples can be created using lists
# this tells us why the tuples are light weight
# on the other hand tuples are very rigid
# the tuples are non mutable, one can not change the tuple
l1 = [1,2,3,4,5,1]
t3 = tuple(list(l1))
print(l1)
print(t3)
print(l1.__sizeof__())
print(t3.__sizeof__())
#t3[0] = 5 # can not change or alter