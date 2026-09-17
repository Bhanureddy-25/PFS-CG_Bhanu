'''
nested if
---------
--> if condition inside an if statement is called nested if 

Ex:
---
app_details = {'pin':8520}
import random
user_pass = int(input('enter ur app password: '))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input('enter four digit otp: '))

    if user_otp == otp:
        print('welcome to app')
    else:
        print('otp is incorrect')

else: 
    print('Password is wrong')








'''
marks = int(input('enter your marks: '))
if marks >= 90:
    print('A+ grade')
elif marks >= 80:
    print('A grade')
elif marks >= 70:
    print('B+ grade')
elif marks >= 60:
    print('B grade')
elif marks >= 50:
    print('C+ grade')
elif marks >= 40:
    print('C grade')
else:
    print('fail')
