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
'''

#Indexing --> index starts with 0 and ends at len(obj)-1 

#print(batch[4])
#print(batch[34])#Index error --> length is only 7 we are accessing extra




#slicing[] --> group of values [start:end];
#when nothing is given in the start value it takes 0 by default;
#same for the end also if end is not specified it prints to upto last element
#print(batch[2:4])
#Striding[]-->[start:end:step]
#print(batch[:7:4])
#print(batch[1::5])
#print(batch[7::4])
#print(batch[1:7:-2])
#print(batch[-1:-4:-1])

batch.insert(2,("vizag","hyd","vjy"))
print(batch)
print(len(batch))
#as we have tuple inside a list
print(batch[2])
#print(len(batch[2]))
print(batch[2] [1]) #this returns 'Hyd' -->string datatype.
print(batch[2][::2])#returns vizag and vjy (striding)
print(batch[2].index("hyd"))
#index --> gives first occureance
#count --> gives the count of the objects

print(batch[2].count("codegnan"))#returns count as 0
#index will raise error,where as count will return 0
batch.insert(3,['pfs','da','jfs'])
print(batch)
print(batch[3])
print(batch[3][1])
batch[3][2] = batch[3][2].upper()#batch[3] is a list and does not have upper attribute
print(batch[3][2])#so we are converting directly batch[3][2] which is a string data type into upper
#now we want to add a new course to batch 3. 
batch[3].append('AAA')
print(batch[3])
print(len(batch[3]))
#remove lo word ivaali------
batch.remove('Bhanu')   #  |
print(batch)            #  | both pop and remove functions only with list
#pop lo index ivvali--------
batch.pop()
print(batch)

batch.clear()
print(batch)

#dictionaries
#dictionary is a collection of key value pairs.
details = {}
#print(len(details))
details['Batch'] = ['PFS-6']
#print(details)
details['Course'] = ['Python']
#print(len(details))
#print(details)
details['Students'] = ['Sai','Hema']
#print(details)
details.update({'branch':('Hyd','Vizag'),
                'Subjects':{'Python','Soft-skills','Aptitude'}})
print(details)
details['Batch'].extend(['JFS','DA'])
details['Students'].extend(['Manu','Chinnu'])
print(details)
details['Subjects'].add('DSA')
print(details)


#Task --> Details --> List,set,Dictionary(Use Codegnan Portal as Example)
#Exams,Mock Interviews,Project Demos

#push to github --> Share your link in whatsapp group


#input from user --> input()
name = list(map(int,input("Enter Names:").split(',')))#by default split will be space seperated 
#split(',') --> is comma seperated 
print(name)
print(type(name))
print(len(name))


pressure,temperature = map(float,input("enter the values:").split(','))
print("temperature is" ,temperature)
print("pressure is" , pressure)



a,b = 13,4.5
print(a,b,end=' ')
print("Codegnan is in Vizag",end = '\t')
print('PFS6 & DA6')
print()

#use print() and build  a simple calculator application
#ask input from user and perform these operations--> add,subtract,multiply,divide

a,b = map(int,input("Enter the Values: ").split(','))

print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("multiplication: ",a*b)
print("Division: ",a/b)




#usage of %d,%f,%s --> from c language
#print("usage of %" %(arguments))
price = 45.3 ; grade = 'A';stock = 15
#print("%d"%price)
#print('%s'%grade)#--> type error,type of grade is string
print("price is: %f"%price)
print("price is: %.1f"%price)
print("Grade is: %s"%grade)
print("price is: %d"%stock)



#find the area of circle when the radius is 3.5cm, round off area o 2 decimal value

r = 3.5
pi = 3.1416
area = pi*(r**2)
print("Area of circle:%.2f"%area)


name = 'alphabets'
letter = 'a'
print(f"{letter} is in {name}")

'''
#control block statements --> they control the flow of the program
#conditional statements-->(if,else,elif)
#repetation statements--> (loops)-->(for,while)
#jumping statements--> (break,continue,pass)


#----> bmi converter(wight,height)


#now lets divide into categeories
'''
<18.5 --> underweight
>=18.5-24.9 --> healthy
>=25-29.9 --> overweight
>30 --> obese

for i in range(5):
    name = input("Enter your name:")
    weight = int(input("Enter weight in Kg's: "))
    height = float(input("Enter height: "))
    if weight>0 and height>0:
        bmi = weight/((height)**2)
        if bmi<18.5:
            print(f'bmi of {name} is {bmi} and you are underweight --> Eat well')
        elif bmi>=18.5 and bmi<=24.9:
            print(f'bmi of {name} is {bmi} and you are healthy --> maintain consistancy')
        elif bmi>=25 and bmi<=29.9:
            print(f'bmi of {name} is {bmi} and you are overweight --> Workout')
        elif bmi>30:
            print(f'bmi of {name} is {bmi} and you are Obese --> consult doctor ')
    else:
        print("Enter only values grreater than 0")

    #task --> User can enter height in centimeters,feets --> meters
    #cal BMI
    #make all User validations for height
    
#1cm = 0.01 meter
#1feet = 0.3048



members = {}

for i in range(5):
    name = input("Enter your name: ")
    weight = int(input("Enter weight in Kg's: "))
    height = float(input("Enter height: "))
    if weight > 0 and height > 0:
        members[name] = (height, weight)
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            print(f"BMI of {name} is {bmi:.2f} and you are underweight --> Eat well")
        elif bmi >= 18.5 and bmi <= 24.9:
            print(f"BMI of {name} is {bmi:.2f} and you are healthy --> Maintain consistency")
        elif bmi >= 25 and bmi <= 29.9:
            print(f"BMI of {name} is {bmi:.2f} and you are overweight --> Workout")
        elif bmi > 30:
            print(f"BMI of {name} is {bmi:.2f} and you are Obese --> Consult doctor")
    else:
        print("Enter only values greater than 0")

print("\n--- Stored Members ---")
for name, (height, weight) in members.items():
    print(f"{name}: Height={height}m, Weight={weight}kg")   


members = {}
for i in range(5):
    name = input("Enter your name: ")
    weight = int(input("Enter weight in Kg's: "))
    height = float(input("Enter height: "))
    if weight > 0 and height > 0:
        members[name] = (height, weight)
    else:
        print("Enter only values greater than 0")
print("\n---> Stored Members <---")
for name, (height, weight) in members.items():
    print(f"{name}: Height={height}m, Weight={weight}kg")
print("\n--- BMI Results ---")
for name, (height, weight) in members.items():
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"BMI of {name} is {bmi:.2f} and you are underweight --> Eat well")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"BMI of {name} is {bmi:.2f} and you are healthy --> Maintain consistency")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"BMI of {name} is {bmi:.2f} and you are overweight --> Workout")
    elif bmi > 30:
        print(f"BMI of {name} is {bmi:.2f} and you are Obese --> Consult doctor")   


details = {'names':[],
           'weights':[],
           'heights':[]}
n = int(input("Enter how many times you want to repeat:"))
for i in range(n):
    weight = int(input("Enter the weight in kgs: "))
    details['weights'].append(weight)
    height = float(input("Enter the height in meters: "))
    details['heights'].append(height)
    name = input("Enter Name: ")
    details['names'].append(name)
    if weight > 0 and height > 0:
#            details[name] = (height, weight)
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                print(f"BMI of {name} is {bmi:.2f} and you are underweight --> Eat well")
            elif bmi >= 18.5 and bmi <= 24.9:
                print(f"BMI of {name} is {bmi:.2f} and you are healthy --> Maintain consistency")
            elif bmi >= 25 and bmi <= 29.9:
                print(f"BMI of {name} is {bmi:.2f} and you are overweight --> Workout")
            elif bmi > 30:
                print(f"BMI of {name} is {bmi:.2f} and you are Obese --> Consult doctor")
    else:
        print("Enter only values greater than 0")


a,b = map(int,input("Enter the values:").split(','))
try:
    result = a/b
    print(result)
except Exception as e:
    print("Find it")
    print(e)

#lets accpet inputs in try block in the same above case:
try:
    a,b = map(int,input("Enter the values:").split(','))

    result = a/b
    print(result)
except ValueError:
    print("chusi enter chey ra puka")
except ZeroDivisionError:
    print("Make sure to give denominator grater than zero")
except NameError:
    print("Spellings Nerchuko Gandu")

'''

try:
    a = [12,3,4,5]
    print(a[0],a[3])
    a.append(['codegnan','Nani'])
    print(a)
except(IndexError,NameError,AttributeError) as e:
    print(e)
finally:
    print("Done")