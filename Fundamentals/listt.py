# a=[]
# a.append("hello")
# a.append(24)
# a.append(4.08)
# print(a)

#lst=[2,4,6,7,8,]
#print(lst)

# lst=[2,3,4,5,6,7,8,9]
# a=[]
# for i in lst:
#     a.append(i*5)
# print(a)
# lst=[2,3,5,6,4]
# prime=[]
# nonprime=[]
# for i in lst:
#     if i > 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 nonprime.append(i)
#                 break
#         else:
#             prime.append(i)
# print(prime)
# print(nonprime)

#index value varing
# lst=[1,2,3,4,5,6,7,8,9,0]
# print(lst[2:5])
# print(lst[3:])
# print(lst[:5])
#
# print(lst[0])
# print(lst[3])
# print(lst[-1])
# print(lst[-4])


# lst=[5,6,7,8,9,67,89,55,43,32]
# print(lst)
#
# def linsearch(lst):
#      ele = int(input("enter a number"))
#      fla = 0
#      for i in lst:
#         if i == ele:
#             fla = 1
#             break
#      if fla == 0:
#        print("not present")
#      else:
#        print("present")
#
# linsearch(lst)

# lis=[2,4,5,6,7,4]
# s=0
# for i in lis:
#     s+=i
# print(s)

# numbers = [1,2,3,4]
# squres = [n**2 for n in numbers]
# print(squres)



number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)