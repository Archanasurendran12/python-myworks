# set

# a=(4,4,5,6)
# print(a)

#empty set

# s=set()
# print(s)
# s.add("hello")
# s.add(5)
# s.add(True)
# s.add(9.7)
# print(s)

# s={1,3,"hello",4,5}
# print(s)
# for i in s:
#     print(i)

#squre of string
# a={1,2,3,4,5}
# b=set()
# for i in a:
#     b.add(i**2)
# print(b)

# s={9,7,5,4,3,2,1}
# s.remove(7)
# print(s)
# s.clear()-complete delete
#del s- remove set

#find common elements

# s1={1,2,3,4,5}
# s2={6,5,8,7,2}
# for i in s1:
#     if i in s2:
#         print(i)

#odd or even
s1={1,2,5,6,90,25,50,60,}
odd=set()
even=set()
for i in s1:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(odd)
print(even)


#union,intersection,diffrends
#a={1,3,5}
#b={1,2,7}
#print(a.union(b))
#print(a.intersection(b))
#print(a.difference(b))

#set is mutable that is it can update.
#unmute means canot be update

