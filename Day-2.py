'''
Tokens
------
--> Tokens are the small unit in python

1.identifier
------------
--> An identifier is a name given to a
 variable -->
 
        num = 'python'
        print(type(num))
 
 function -->

    def add_(a,b):
        print (a+b)
    add_(2,3)

 class -->
    class details:
        pass
        per_1 = details()
 
2.keywords
------------
--> keywords are the reserved words in python which have a predefined meaning and cannot be used as identifiers.
Example: if, else, elif, for, while, break, continue, def, class, return, import, from, as, pass, try, except, finally, with, lambda, yield

3.literals
------------
--> literals are the values assigned to variables.
Example: 'python', 5, 3.14, True, False
 
4.operators
------------
--> operators are the symbols used to perform operations on variables and values.
Example: +, -, *, /, //, %, **, ==, !=, <, >, <=, >=, and, or, not

5.statements
------------
--> statements are the instructions that are given to the program 
Example: print('Hello World'), num = 90 ,
num=90
if num >= 50:
    print('pass')

comments
------------
--> comments are the lines in the code that are not executed by the interpreter.
Example: # this is a single line comment(#)
           MULTI LINE COMMENT (''' ''')

Variables Rules
------------
1. A variable name can only contain letters, numbers, and underscores.
2. A variable name cannot start with a number.
3. A variable name cannot contain spaces.
4. A variable name is case-sensitive.
5. A variable name cannot be a keyword.



swapping of two numbers
a,b = 45,67
print('a=',a)
print('b=',b)
a,b = b,a
print('a=',a)
print('b=',b)



'''