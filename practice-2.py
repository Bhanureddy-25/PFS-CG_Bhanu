for i in range(1,6):
    for j in range(97, 97+i):
        print(chr(j), end = ' ') 

    print()













'''
inverse pattern
---------------
-->  for i in range (start, stop, step):
    start = 5
    stop = 0
    step = -1

    
number pattern
---------------
-->  for i in range (1,6):
    for j in range (1,i+1):
        print(j, end = '')
        here 1,i+1 is the range of j, which means j will take values from 1 to i (inclusive).


        

        for i in range (1,6):
    for j in range (1,i+1):
        print(i,end = ' ')
    print()  # This print statement is used to move to the next line after each row of numbers is printed.
'''