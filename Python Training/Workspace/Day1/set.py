myset = {10, 20, 450, 10, 23, 20}
print(myset)
print(type(myset))

myset.add(244)
print(myset)


print(30 in myset)

# for val in myset : 
#     print(val)
    

print(myset.remove(10))
print(myset)

set1 = {1,2,3,4,5}

set2 = {3,4,5,6,7}


print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))


