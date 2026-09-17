'''


get()
-----
--> get method is also use to get the value from that key
Syntax --> dict.get()

eg:
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
         2:[3,4]}
print(data)

update()
--------
--> method is used to update a key, incase if they is not present inside the dictionary then
 it will add that key value to the dictionary
Synatax --> dict.update({key: vlaue})
ex:
---
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
        }

print(data)
data.update({'name': 'sai'})
data.update({'PIN':5656})
print(data)

Method_2:
---------
Syntax --> dict[key] = value
eg:
---
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
        }

print(data)
data['AC.NO'] = '9491355377'


values()
--------
-->Values() method is used to get all the values from the dictionary
Syntax --> dict.values()
eg:
---
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
        }

print(data)
data['AC.NO'] = '9491355377'
data.update({'name': 'sai'})
data.update({'PIN':5656})


print(data.values())

Keys()
------
--> keys() s he method used to get values of key from the dictionary
syntax --> dict.keys()

eg:
---
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
        }

print(data)
data['AC.NO'] = '9491355377'
data.update({'name': 'sai'})
data.update({'PIN':5656})


print(data.keys())

items()
-------
-->the method will get the key: value seperated from thedictionary
Syntax--> dict.items()
eg
--
data = {'name': 'Bhanu',
        'balance': 5000,
        'adr' :123456789761,
        'pan' :'INNPK56789R',
        }

print(data)
data['AC.NO'] = '9491355377'
data.update({'name': 'sai'})
data.update({'PIN':5656})


print(data.items())

clear()
-------
-->used to delete the entire values inside dictionary
Syntax--> dict.clear()
    -->del()
       ----- 
    
Statements()
------------

if()
----
--> if condition is true then it will execute the inside block of code
 |
 --> incase it becomes flase then it will not execute the inside block code

ex:
---
a = 90
b = 78
if a>b:
print(a)

if else()
---------
--> else for a if statement is a fall-back statement, it only executes when the if condition is failed. 




'''









