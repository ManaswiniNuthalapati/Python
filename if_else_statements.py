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
    

#5
# Given n apples, you and your friend take turns picking one apple each starting with you; print "You" if you take the last apple, otherwise print "Friend".
n=int(input())
if n%2==0:
    print("Friend")
else:
    print("You")
    

#6
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
    
#7
# Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" 
year=int(input())
if year%4==0:
    print("True")
else:
    print("False")
    '''
#8
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
    print("none")  