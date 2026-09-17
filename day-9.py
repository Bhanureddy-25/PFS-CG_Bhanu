'''

Union()
----------

→ the union() will combine two set into a sinngle set
syntax → set1_.union(set_2) or set_1 | set_2


eg
--
data = {1,2,3,4,}
nums = {4,5,6}
print(data.union(nums))
print(data | nums)


intersection()
-----------------


ex:
---
data = {1,2,3,4,}
nums = {4,5,6}
print(data.intersection(nums))
print(data & nums)

difference()
-----------------

--> it will display the different elements from set_1 but not in set_2
Syntax → set_1.difference(set_2) or set_1 - set_2

ex:
---
data = {1,2,3,4,}
nums = {4,5,6}
print(data.difference(nums))
print(data - nums)

Symmetric_difference()
----------------------
--> it will display the different elements from both sets
Syntax → set_1.symmetric_difference(set_2) or set_1 ^ set_2

Ex:
---
data = {1,2,3,4,}
nums = {4,5,6}
print(data.difference(nums))
print(data ^ nums)

add()
-----
--> it will add the element to the set | it adds only one element at a time
Syntax → set_1.add(element)
ex:
---
data = {1,2,3,4,}
print(data.add(7))
print(data)


update()
-------
--> it will add the multiple elements to the set | it adds only one element at a time
Syntax → set_1.update([element1, element2, element3])
ex:
---
data = {1,2,3,4,}
nums = {4,5,6}
data.update([7,8,9])
print(data)
data.update(nums)
print(data)

remove()
-------
--> it will remove the element from the set | if the element is not present it will throw an error
Syntax → set_1.remove(element)
ex:
---
data = {1,2,3,4,}
data.remove(3)
print(data)

discard()
-------
--> it will remove the element from the set | if the element is not present it will not throw an error
Syntax → set_1.discard(element)
ex:
---
data = {1,2,3,4,}
data.discard(7)
print(data)
data.discard(3)
print(data)

clear()
-------
--> it will remove all the elements from the set
syntax → set_1.clear()
ex:
---
data = {1,2,3,4,}
data.clear()
print(data)


'''







