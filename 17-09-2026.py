'''
#Grade_Checker:
#=============#
marks = float(input("Enter Marks out of 100: "))
if marks >= 0 and marks <= 100:
    if marks >= 90:
        Grade = 'A'
        remarks = "Outstanding!"
    elif marks >= 80:
        Grade = 'B'
        remarks = "Excellent!"
    elif marks >= 70:
        Grade = 'C'
        remarks = "Good"
    elif marks >= 60:
        Grade = 'D'
        remarks = "Fair, needs improvement"
    elif marks >= 50:
        Grade = 'E'
        remarks = "Poor, needs serious improvement"
    else:
        Grade = 'F'
        remarks = "Failed, needs to reappear"
    print("Grade:", Grade)
    print("Marks:", marks)
    print("Remark:", remarks)

else:
    print("Invalid marks entered")





#Even_Odd Checker
#****************

Number = int(input("Enter a number: "))
if Number == 0:
    print("Zero is neither even nor odd")
elif Number < 0 and Number % 2 == 0:
    print("Negative Even Number")
elif Number < 0 and Number % 2 != 0:
    print("Negative Odd Number")
elif Number > 0 and Number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

    


'''    