# import numpy as np
# a = np.arange(9, dtype =float).reshape(3,3)
#
# print('first array:')
# print(a)
# print('\n')
#
# print('second array:')
# b = np.array([10,10,10])
# print(b)
# print('\n')
#
# print('add the two arrays:')
# print(np.add(a,b))
# print('\n')
#
# print('substract the two arrays:')
# print(np.subtract(a,b))
# print('\n')
#
# print('multiply the two arrays:')
# print(np.multiply(a,b))
# print('\n')

#tangent values

# import numpy as np
# a = np.array([0,30,45,60,90])
# print(a)
#
# print('sine of different angles:')
# print(np.sin(a*np.pi/180))
# print('\n')
#
# print('cosine values for angles in array:')
# print(np.cos(a*np.pi/180))
# print('\n')
#
# print('tangent values for  given angles:')
# print(np.tan(a*np.pi/180))


import numpy as np
a = np.array([0,30,45,60,90])

print('array containing sine values:')
sin = np.sin(a*np.pi/180)
print(sin)
print('\n')

print('compute sine inverse of angles, return values are in radians:')
inv = np.arcsin(sin)
print(inv)
print('\n')

print('check result by converting to degrees:')
print(np.degree(inv))
print('\n')

print('across and arctan functions behave similarly:')
cos = np.cos(a*np.pi/180)
print(cos)
print('\n')

print('inverse of cos:')
inv = np.across(cos)
print(inv)
print('\n')

print('in degrees:')
print(np.degree(inv))
print('\n')

print('tan function:')
tan = np.tan(a*np.pi/180)
print(tan)
print('\n')

print('inverse of tan:')
inv = np.arctan(tan)
print(inv)
print('\n')

print('in degrees:')
print(np.degrees(inv))




