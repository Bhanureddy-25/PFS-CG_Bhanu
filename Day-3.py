'''
print('b=',b)


DataTypes & TypeConversions
-----------------------------
1.Numeric data types
---------------------

----> Float and integer is called as numeric datatypes.

2.Float data type
-----------------
A float is a number that has a decimal values, we call it float data type.
EX: 
num1 = 3.14
Price = 56.89

3.Integer data type
-------------------
An integer is a whole number without any decimal values, we call it integer data type.
EX:
num2 = 5
num1 = 89

4.String data type
------------------
A string is a sequence of characters enclosed in single or double quotes, we call it string data type.
String is immutable, which means we cannot change the value of a string once it is created.
Ex:
name = 'python'
all_ = 'Ab,.&[)-+'

5.List data type
----------------
A list is a collection of items which is ordered and changeable, we call it list data type.
it is represented by [] and the items are separated by commas.
the items in a list can be of any data type and can be duplicated.
Ex:
fruits = ['apple', 'banana', 'orange']
any_ = [1, 'python', 3.14, True, [1,2,3], {'name':'python', 'age':5}]
print(type(any_))

6.Tuple data type
-----------------
A tuple is a collection of items which is ordered and unchangeable, we call it tuple data type.
it is represented by () and the items are separated by commas.
the items in a tuple can be of any data type and can be duplicated.
Ex:
nums = (1,89.67,'python',[3,4],(8,9))
print(type(nums))

7.Dictionary data type
----------------------
A dictionary is a collection of items which is unordered, changeable and indexed, we call it dictionary data type.
it is represented by {} and the items are separated by commas.
the items in a dictionary can be of any data type and can be duplicated.
Ex:
person = {'name': 'python', 'age': 5}
print(type(person))


6.Set data type
----------------------
A set is a colletion of unique elements and set can't allow any duplicate values inside it
set is represented by {} and the items are separated by commas.
Ex:
an={1,2,3,4,5,6,7,8,9}
print(an)



-------------------------- 
|   TYPE CONVERSIONS     |      
--------------------------

float() --> can convert into integer and string data type into float data type
price = 56.89
con = int(price)
print (type(con))

int() --> can convert into float and string data type into integer data type
price = 56.89
con = float(price)
print (type(con))

str() --> can convert into float and integer data type into string data type but only numeric string can be converted into integer and float data type.
price = 56.89
con = str(price)
print (type(con))

List() --> can convert into tuple and set data type into list data type
Ex:
nums = [1,2,3,4]
print(tuple(nums))

set() --> can convert into list and tuple data type into set data type
Ex:
all_ = {5,6,7}
print(tuple(all_))

Dictionary() --> can convert into list and tuple data type into dictionary data type
Ex:
details = [('name', 'python'),('age', 5)]
person = dict(details)

'''
details = [('name', 'python'),('age', 5)]
person = dict(details)