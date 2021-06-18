punctuations = '' ""!()-{};:/<>

my_str=input("enter a string")

no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

 print(no_punct)


