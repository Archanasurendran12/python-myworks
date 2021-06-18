# dict = {'name':'anju', 'age' :6}
# print(dict)
# print(type(dict))
#
# print("dict['name']: ", dict['name'])
# print("dict['age']: ", dict['age'])
#
# dic={}
# print(dic)
# print(type(dic))

#mutable,kepp order,hetrogenous
#update
# dict = {'name':'anju', 'age' :6, 'class': 'first'}
# dict['age'] = 8
# dict['school'] = "dps school"
# dict.update({'location':'kochi'})
# print(dict)

#deleting dectonry
# dict = {'name':'anju', 'age' :6, 'class': 'first'}
# del dict['name'] #remove entry with a keyname
# dict.clear()    #remove all entries in dict
# del dict        #deleate entire dictinory
# print(dict)

#word count

count={}
data=input("enter")
words=data.split(" ")
# print(words)
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)

