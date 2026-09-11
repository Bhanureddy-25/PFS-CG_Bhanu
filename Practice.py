'''
cost = 2000
discount = 0.05
gst = 0.05
final_price = cost-(cost*discount)
final = final_price+(final_price*gst)
print (final)

cost = int(input('Enter CP: '))
selling = int(input('Enter SP: '))
profit = cost-selling
profit_percentage = (selling-cost)/cost*100
print('Profit Percentage =',profit_percentage) 

=======================================================
price = int(input('Enter Amount: '))
discount = float(input('Enter Discount in between 0.1-0.2: '))
gst = float(input('Enter GST: '))

final_prize = price - (price*discount)
final_prize = final_prize + (final_prize*gst)
print('Final pice = ',final_prize)
=======================================================================

operators --> Arithemetic,assignment,comparision,Membership,logical
           |
            --> Bitwise,identity.
           
membership --> in , not in --> checks for the values in a collection

marks = []
for mark in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
print(marks.pop())
print("final List is",marks)
print("Length of the list is",len(marks))

numbers = [20,10,30,20,40,20]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

number = int(input("Enter a Number: "))
if number in numbers:
    print("Count is",numbers.count(number))
    print("first index is",numbers.index(number))
else:
    print("Number is not in the list")

print("smallest Value is ",min(numbers))
print("largest value is ",max(numbers))
print("sum of values in list is",sum(numbers))



#1: Create two empty lists named even and odd.
#2: Use a loop to examine every number in the original list.
#for number in numbers:
   # if number % 2 ==0:
    #   print(f"{number} is even")
    #else:
     #   print(f"{number} is odd")
#3: Use a condition with the remainder operator (%) to identify even and odd numbers. 
#4: Add each number to the correct list using append(). 
#5: Use slicing to display the first three and last three values. 
#6: Create a backup of the original list using copy().  
#7: Empty the original list using clear(), then display both the original and backup lists. 
numbers = [10, 15, 20, 25, 30, 35]
Even = []
odd = []
for i in numbers:
    if i % 2 ==0:
        Even.append(i)
    else:
        odd.append(i)

print(Even)
print(odd)
print("first three:",numbers[:3])
print("last three:",numbers[3:])
f = numbers.copy()
print(f)
numbers.clear()
print(numbers)

a=15
b=25
print(a+b)
'''
batch = ['PFS-6','DA-6']
#print(batch)
#print(type(batch))
#python follows both procedure oriented programming
#and object oriented programming

#len()-->it is a funcion used that returns the number of items in a collection
#print(len(batch))

#Add 3 more student names into it
batch.append('sai')
#print(batch)
batch.extend(['Bhanu','Nani'])
#print(batch)
batch.insert(0,'Reddy')
#print(batch)
batch.insert(-1,'Python')
#print(batch)
#print(len(batch))


#Indexing --> index starts with 0 and ends at len(obj)-1 

#print(batch[4])
#print(batch[34])#Index error --> length is only 7 we are accessing extra




#slicing[] --> group of values [start:end];
#when nothing is given in the start value it takes 0 by default;
#same for the end also if end is not specified it prints to upto last element
#print(batch[2:4])
#Striding[]-->[start:end:step]
print(batch[:7:4])
print(batch[1::5])
print(batch[7::4])
print(batch[1:7:-2])
print(batch[-1:-4:-1])