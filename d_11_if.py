'''
# find The leap Year
year = 2025
if (year%4==0 and year!=100) or (year%400==0):
    print("Leap Year")
else:
    print("Not Leap year")
    

#Grading System
marks=int(input())
if (marks>=90):
    print("A")
elif (marks>=80 and marks<=89):
    print("B")
elif (marks>=70 and marks<=79):
    print("C")
elif (marks>=60 and marks<=69):
    print("C")
else:
    print("Fail")
    '''

#Check Triangle Type
side1=int(input())
side2=int(input())
side3=int(input())
if(side1==side2==side3):
    print("Equilateral")
elif(side1==side2!=side3):
    print("Isosceles")
elif(side1!=side2!=side3):
    print("Scalene")
else:
    print("Invalid")


    
    