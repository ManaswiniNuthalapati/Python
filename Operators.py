#1
# Given two variables x and y and perform Arithmetic Operations
x=int(input())
y=int(input())
p = x+y
q = x-y
r = x*y
s = x//y
t = x%y
print(p, q, r, s, t)

#2
# Given four inputs that are stored in variables a, b, c, and d. Write an expression to evaluate and The expression should be a single statement.
class Solution:
    def calculate(self, a: int, b: int, c: int, d: int) -> int:
        return (a+b)//c+d

#3
# Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.  Calculate the nth term of A.P. 
class Solution:
    def nthTerm(self, a, d, n):
        return a+(n-1)*d
    
#4
# Sum od N Natural Numbers
class Solution:
    def sumoffirstn(self, n: int) -> int:
        return n*(n+1)//2
    
#5
# Last Digit of a number
class Solution:
    def lastDigit(self, n: int) -> int:
        return abs(n)%10
    
#6
# Day Before N Days
class Solution:
    def findAnswer(self, d, n):
        return (d-n)%7
    
#7
# Swap Two variables without using third variable
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)

# Swap Two variables without using third variable
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#8
#  Remove Last Digit of a Number
a=int(input())
print(a//10)


# Sum of Digits (eg:57--5+7=12)
a=int(input())
b=a//10
c=a%10
print(b+c)


# Find absolute difference between two numbers
a=int(input())
b=int(input())
c=abs(a-b)
print(c)

# Take a 3-digit number and print its reverse using only operators
a=int(input())
b=str(a%10)
c=str(a//10)
d=b+c
print(d)

# Store your age in a variable and print the year you were born
birth_year=int(input())
curr_year=2025
print(curr_year-birth_year)


# Input a number and print whether it is even
a=int(input())
print("Even:" ,a%2==0)


# Take two integers and print the bitwise AND, OR, XOR results.
a=int(input())
b=int(input())
print(a&b)
print(a|b)
print(a^b)

'''
# Assign two numbers and print their average without using division '''
a=int(input())
b=int(input())
c=(a+b)*0.5
print(c)


