myList = [10,2,340,40]
print(myList + myList)
print(myList * 2)

import numpy as np
myArray = np.array(myList)
print(type(myArray))
print(myArray)
print(myArray + myArray)
print(myArray * myArray)
print(myArray ** myArray)
print(myArray * 4)
print(myArray)

myArray = np.append(myArray, 100)

print(myArray)

print(np.insert(myArray, 0, 1))
print(np.delete(myArray, 0))


myArray2 = np.array([10,20,2,3,4,56])
print(np.sum(myArray2))
print(np.max(myArray2))
print(np.min(myArray2))
print(-np.sort(-myArray2))

nd = np.array([[1,3,8],[5,7,1],[9,3,7]])
print(nd)
print(np.sum(nd))
print(np.sum(nd, axis=1))
print(nd.T)