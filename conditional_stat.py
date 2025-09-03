#1
#  Given a number n, print "Big" if n > 100. Always print "Number" at the end.

'''n=int(input())
num=100
if n>num:
    print("Big")
print("Number")

#2
# If a > 100 → print "Big" Else → print "Number"
n=int(input())
if n>100:
    print("Big")
else:
    print("Number")
    
#3
# If `a > 100` print "Big", elif `a < 10` print "Small", else print "Number". 
a=int(input())
if (a>100):
    print("Big")
elif (a<10):
    print("Small")
else:
    
    print("Number")
    

    
#4
# Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" 
year=int(input())
if year%4==0:
    print("True")
else:
    print("False")
    
#5
# Given two numbers a and b, use the value of operator: if it is 1 print their sum, if 2 print their difference (a - b), if 3 print their product, otherwise print "Invalid Input".
a=int(input())
b=int(input())
operator=int(input())
if operator==1:
    print(a+b) 
elif operator==2:
    print(a-b)
elif operator==3:
    print(a*b)
else:
    print("Invalid")
    '''
    #1
''' Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if ((a > 0 and b < 0) or (a < 0 and b > 0)) and flag == False:
            return True
        elif ((a<0 and b<0) and flag==True):
            return True
        else:
            return False'''
        

#2 
'''You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.
def cat_hat(str):
    count_cat = str.count("cat")
    count_hat = str.count("hat")
    if count_cat == count_hat:
        return True
    else:
        return False

#1
# Print **"Fizz"** if the number is divisible by 3, **"Buzz"** if divisible by 5, **"FizzBuzz"** if divisible by both, otherwise print the number. 
num=int(input())
if (num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
elif (num % 5 == 0):
    print("Buzz")
elif (num % 3 == 0):
    print("Fizz")
else:
    print("None")
    

#2
# Given n apples, you and your friend take turns picking one apple each starting with you; print "You" if you take the last apple, otherwise print "Friend".
n=int(input())
if n%2==0:
    print("Friend")
else:
    print("You")
    

#3
# Given three numbers a, b, and c. You need to find which is the greatest of them all.
a=int(input())  
b=int(input())
c=int(input())
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    
    
# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:] 
    


# Salary Bonus Calculator
year=int(input())
salary=int(input())
if year>10:
     print("10%",salary*0.1)
elif (year>=6) and (year<=10):
    print("8%",salary*0.8)
elif year<6:
    print("5%",salary*0.5)
else:
    print("Invalid")
    
#Electricity Bill Calculator. calculate total bill amount
units=int(input())
if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+((units-100)*7)
else:
    bill=(100*5)+(100*7)+((units-200)*10)
print(bill)

# Character Type Check
ch=input('Enter a char: ')
#if ('a'>=ch) and ('z'<=ch) and ('A'>=ch) and ('Z'>=ch):
if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")
    
# checking whether a number is 3 digit or not
num=input('Enter a number:')
n=len(num)
if n==3:
    print("True")
else:
    print("False")
    
# Cab Fare Calculaor
km=int(input())

if km<=5:
    Fare=50
elif km<=15:
    Fare=50+(km-5)*10
else:
    Fare=50+(10*10)+(km-15)*15
print(Fare)'''

# Insurance Premium Calculator
age=int(input())
v_age=int(input())
if age<25 and v_age<5:
    Premium="High"
elif (age>25) and (age<60) and v_age<10:
    Premium="Medium"
else:
    Premium="Low"
print(Premium)
    