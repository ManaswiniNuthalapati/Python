'''
#1
# Swap two numbers using 3rd variable
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a)
print(b)


#2
# A double value d = 10.23 is given. Print the integer value of d.
d = 10.23
print(int(d))


#3
# given a number as string. so typecast into an integer and double it.
num = input()
a= int(num)
print(a * 2)


#4
# Sum of n Natural Numbers
class Solution:
    def sumOfNumbers(self, n):
        total=n*(n+1)//2
        return total
        '''
        

#5
'''Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.

Examples:

Input: a = 6, b = 4, c = &
Output: 666666&4444
Explanation: 6 printed 6 times and 4 printed 4 times seperated by c = &.

a = int(input())
b = int(input())
c = input()
d=str(a)*a
e=str(b)*b
print(d+c+e)

#6
# Area of Rectangle
length=int(input())
breadth=int(input())
area=length*breadth
print(area)


#7
# conversion of celsius to fahrenheit
a = float(input())
b = (a*9/5)+32
print(b)


#8
# Assign a variable and convert it into integer and multiply by 2
a=input()
b=int(a)
print(b)
print(b*2)

x=int(input())

#9
# Swap two numbers without using 3rd variable
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)
'''

#10
# Calculate SImple Interest
p=int(input())
r=int(input())
t=int(input())
SI=(p*r*t)/100
print(SI)






