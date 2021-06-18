import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print('Original array is:')
print(a)
print('\n')

print('Transpose of the original is:')
b = a.T #Transpose
print(b)