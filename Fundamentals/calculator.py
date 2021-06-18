def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("select operation")
print("1.add")
print("2.substration")
print("3.multiply")
print("4.divide")
while True:
    choice = int(input("enter the choice"))
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
if choice == 1:
        print(add(num1, num2))
elif choice == 2:
            print(substract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
elif choice == 4:
    print(division(num1, num2))
else :
   print("cant find")




