
#sorting without using sort function
# my_list = [111, -15, -26, 15, 1, 0, 8, 876, 100,54,23]
# new_list = []
#
# while my_list:
#     min = my_list[0]
#     for i in my_list:
#         if i < min:
#             min = i
#     new_list.append(min)
#     my_list.remove(min)
# print(new_list)
# print(my_list)

#min and maximum elements in list
# my_list = [111, -15, -26, 15, 1, 0, 8, 876, 100,54,23]
# maximum = max(my_list)
# print(maximum)
# minimum = min(my_list)
# print(minimum)

#or  without using min and maximum
# my_list = [111, -15, -26, 15, 1, 0, 8, 876, 100,54,23]
#  new_list = []
#
#  while my_list:
#      min = my_list[0]
#      for i in my_list:
#          if i < min:
#              min = i
#      new_list.append(min)
#      my_list.remove(min)
# print(new_list)
# print(my_list)

# print("minimum element",new_list[0])
# print("maximum element",new_list[-1])

#find duplicate elements in a list
s=[1,2,3,4,1,2,3]
a=[]
for i in s:
    if i not in a:
        a.append(i)
    else:
        print(i)
