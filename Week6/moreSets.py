# set do not allow dupliates
# set is an unordered entity, we can not have index for set
# sets are not subscriptables
# sets are mutables and the values have to be immutable and hashable

s1 = {1, 2, 3, 4, 5, 1, 2, 3}
print(s1, type(s1))
#s2 = {[1,2,3], 2, 3} # not allowed as the element of the set is a list and it is mutable

# iterate over set
for i in s1:
    print(i)

# sets in python are based on mathematical sets
# so all the mathematical operations can be performed on python sets
s2 = {1, 2, 3}

print(s2.issubset(s1))
print(s2.issuperset(s1))

print(s1 | s2)
print(s1.union(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1 - s2)
print(s1.difference(s2))