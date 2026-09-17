'''
Armstrong number
---------------
--> it is a number that is equal to the sum of its own digits raised to the power of the number of digits.
    for example, 153 is an Armstrong number because it has 3 digits, and 1^3 + 5^3 + 3^3 = 153.

Ex:
---
num = int(input("Enter a number: "))
length = len(str(num))
armstrong_number = 0
for i in str(num):
    armstrong_number = armstrong_number + int(i)**length
    print(armstrong_number)
if armstrong_number == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


    perfect number
    ---------------
    --> A perfect number is a positive integer that is equal to the sum of its proper positive
Ex:
---
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
        print(f"Divisor: {i}")

if sum_of_divisors == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")


fibonacci series:
-----------------
--> The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, 
starting from 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
Ex:
---
num = 0
num1 = 1
print(num, num1, end = ' ')
for i in range(1,10):
    num2=num+num1
    num=num1
    num1=num2
    print(num2, end = ' ')

'''
num = 0
num1 = 1
n = int(input("Enter the number of terms in the Fibonacci series: "))
print(num, num1, end = ' ')
for i in range(1, n):
    num2=num+num1
    num=num1
    num1=num2
    print(num2, end = ' ')