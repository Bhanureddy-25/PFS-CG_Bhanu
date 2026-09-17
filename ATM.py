'''
Python project ATM machine


Technology used:
================
1) Basic Python

Steps:
======
-->withdraw
-->depsoit
-->pin change
-->check balance
*****************************************************
*    objectives to complete by wednesday            *
*    1)pin change                                   *       
*    2)transaction history                          *=======> complete as soon as possible
*    3)do not modify or change the existing code    *
*                                                   *
*****************************************************



Exception Handling:
===================
--> this is the process of handling the errors
--> we can write any number exception for one code written at try block

try:
----
--> the try block, where we can write a code which may contain errors
Syntax -->
try:
    code that is required to use
    



1)except
2)else
-------
--> the else block will only execute, if no error at try block
ex:
---
try:
    print(5/8)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No error')

3)finally
----------
--> executes regaurdless the error
eg:
---
try:
    print(5/8)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No error')




sample code:
============



'''
Bank_details = {
    "name": 'bhanu',
    'Addr': 'Vizag',
    'PAN': '9491355377',
    'ATMPIN': '8520',
    'Balance': 100000,
    'mini_statement' :[] 
}
all_attempts = 3
while all_attempts > 0:
    user_pin = input('Enter ATM Pin: ')
    if user_pin in Bank_details['ATMPIN'] and len(user_pin)==4:
        print("Welcome To Bank")
        choice=int(input('Enter \n1.Withdraw \n2.Deposit \n3.Check balance \n:'))
        if choice == 1:
            Withdraw_amount = int(input('Enter amount to Withdraw: '))
            if Withdraw_amount <= Bank_details['Balance'] and Withdraw_amount % 100 == 0:
                Bank_details['Balance'] -= Withdraw_amount
                print(f'take your cash and your balance is {Bank_details["Balance"]}')
                Bank_details['mini_statement'].append(f'Withdraw: {Withdraw_amount}')
                print(f'{Bank_details["mini_statement"]}')
                user_opt = int(input('1.Home Page \n2.Exit \nEnter: '))
                if user_opt == 1:
                    print('Taking to Home Page')
                elif user_opt == 2:
                    print('Thanks for Visiting')
                    break
            else:
                print('Insufficient Balance or this atm cannot provide cash at the momment')
                break
        elif choice == 2:
            Deposit_amount = int(input('Enter Amount to Deposit: '))
            if Deposit_amount % 100 ==0:
                Bank_details['Balance'] += Deposit_amount
                print(f'amount to depsoit and total amount in account:{Bank_details["Balance"]}')
                Bank_details['mini_statement'].append(f'Deposit: {Deposit_amount}')
                print(f'{Bank_details["mini_statement"]}')
                user_opt = int(input('1.Home Page \n2.Exit \nEnter: '))
                if user_opt == 1:
                    print('Taking to Home Page')
                elif user_opt == 2:
                    print('Thanks for Visiting')
                    break
            else:
                print('This ATM Does not Accept Change')
        elif choice == 3:
            print(f'Your Account balance is {Bank_details["Balance"]}')
            user_opt = int(input('1.Home Page \n2.Exit \nEnter: '))
            if user_opt == 1:
                print('Taking to Home Page')
            elif user_opt == 2:
                print('Thanks for Visiting')
                break
        break

    else:
        all_attempts -=1
        if all_attempts > 0:
            print(f'Incorrect Pin Entered and you have {all_attempts}')
        else:
            print('Your Card is Blocked')
