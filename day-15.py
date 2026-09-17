'''
when is called
--> a function start with def keyword and th line is called as definition line,
where we can define a function name and parameters, and the body of the function is indented below the definition line.
--> and if we want to execute the program in the function,
we need to call the function by using the function name and passing the required arguments in parentheses.



syntax
------
def fun_name(parameters):
    pass
    fun_name(arguments)

ex:
---
def add(a,b):
print(a+b)
add(10,20)

Arguments
---------
Positional arguments:
---------------------
--> the areguments should be same at def line and function call line, 
incase they are not same then it will give an error. 


ex:
---
def fibanocci(num , num1 , num2):
    print(num, num1, end = ' ')
    for i in range(1,10):
        num2=num+num1
        num=num1
        num1=num2
        print(num2, end = ' ')
fibanocci(0, 1, 0)





ex:
---
def feb(num=0, num1=1):
    print(num+num1)

feb([1,3],[5,6])

default arguments:
------------------
--> the default arguments where the function will only consider the data at calling eventhough data fresent at def ine                        
#(function call lo ey values icchina sare, function lo default values ki priority istundi)

Ex:
---
def data(a=8, b=10):
    print(a+b)
data(1,2)

Ex for prime number:
--------------------
def prime(a=7):
    for i in range(2, a):
        if a % i == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number ")
print("Enter a number: ")    
n = int(input())
prime(n)

keyword arguments:
------------------
-->  Keyword arguments are sending arguments in a pair

Ex:
---
def data(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data(22,"sai",6,"Vizag")


def all(*names):
    print(names)
all('sai','kumar','reddy')

def details(**data):
    print(data.keys())
details(name='sai', age=22, batch=6, location='Vizag')

return statement:
------------------
-->  The return statement is used to exit a function and go back to the place where it was called. This statement can contain an expression which gets evaluated and the value is returned to the caller



'''

    