# import numpy as np
# a = np.arange(10)
# print(a)
# print(a[slice(2,7,2)])

#slising multi dimensional array
# import numpy as np
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a)
# print('now we will slice the array from the index a[1:]')
# print(a[1:])

#indexing
# import numpy as np
# x = np.array([[1, 2],[3, 4],[5, 6]])
# print(x)
# print("................")
# y = x[[0,1,2],[0,1,0]]
# print(y)

#corner elements
import numpy as np
x = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9, 10, 11]])
print('our array is')
print(x)

rows = np.array([[0, 0],[3, 3]])
cols = np.array([[0, 2],[0, 2]])
y = x[rows, cols]

print('the corner elements of this array are:')
print(y)