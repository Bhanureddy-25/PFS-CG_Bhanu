'''
scope of variables
==================
1.local variable: variable defined inside a function
2.global variable: variable defined outside a function

Ex:
---
def display():
    name = "John" # local variable

    
--> global is keyword used to declare a variable as global
--> a variable that is defined outside a function is called global variable

it can be accessed trough any where in the program

Ex:
---
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)








'''




def fac(a):
    if a == 0 or a == 1:
        return 1
    return a * fac(a - 1)
a=int(input("Enter a number: "))
print(fac(a))










