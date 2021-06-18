# import numpy as np
# a = np.array([[0.0, 0.0, 0.0],[10.0, 10.0, 10.0],[20.0, 20.0, 20.0],[30.0, 30.0, 30.0]])
# b = np.array([1.0, 2.0, 3.0])
#
# print('...........first array............')
# print(a)
#
# print('...........second array............')
# print(b)
#
# print('...........first array + second array............')
# print(a + b)

#boolean
# import numpy as np
# x = np.array([[ 10, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
#
# print('our array is:')
# print(x)
# print('\n')
#
# print('the items greater than 5 are:')
# print(x[x > 5])

#display array elements

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print('original array is:')
print(a)
for i in a:
    for j in i:
        print(j)

for x in np.nditer(a):  #n-diamensional array iteration
    print(x)



