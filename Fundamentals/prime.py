#prime or not

# n=int(input("enter a number"))
# if n > 1:
#  for i in range(2, n):
#
#     if (n % i) == 0:
#        print("not prime")
#        break
# else:
#      print("prime number")

# range

# min=int(input("enter min range"))
# max=int(input("enter max range"))
#
# for a in range(min,max+1):
#
#     if a > 1:
#         for i in range(2,a):
#             if(a % i) == 0:
#                 break
#         else:
#                 print(a)

# sum

min=int(input("enter min range"))
max=int(input("enter max range"))

for a in range(min,max+1):

     if a > 1:
        for i in range(2,a):
             if(a % i) == 0:
                 break
        else:
             sum=sum+a
print(sum)