#1 To Check if the character is alphabet or number or any special Character
ch=input()
if ch.isalpha():
    print("alphabet")
elif ch.isdigit():
    print("Number")
else:
    print("Special Character")
    
# TO Check if the triangle is valid or not
side1=int(input())
side2=int(input())
side3=int(input())
if (side1+side2+side3==180) and (side1,side2,side3>0):
    print("Valid")
else:
    print("Not Valid")
    
''' Electricity Bill
First 50 units → ₹2 per unit
Next 100 units (51–150) → ₹3 per unit
Next 100 units (151–250) → ₹5 per unit
Above 250 units → ₹8 per unit'''
units=int(input())
if units<=50:
    price=units*2
elif (units<150):
    price=100+(units-50)*3
elif (units<250):
    price=100+300+(units-150)*5
else:
    price=100+300+500+(units-250)*8
print(price)

'''Salary Calculation
If salary ≤ 10,000 → rent = 20%, allowance = 80%
If 10,001 – 20,000 → rent = 25%, allowance = 90%
If > 20,000 → rent = 30%, allowance = 95%'''

salary=int(input())
if salary<=10000:
    rent=salary*0.20
    allowance=salary*0.80
elif salary<=20000:
    rent=salary*0.25
    allowance=salary*0.90
else:
    rent=salary*0.30
    allowance=salary*0.95
gross=salary+rent+allowance
print(gross)

#  Input three numbers and check if they can form a Pythagorean triplet.
a=int(input())
b=int(input())
c=int(input())
hypotenuse=max(a,b,c)
if hypotenuse==a:
  side1,side2=b,c
elif hypotenuse==b:
  side1,side2=a,c
else:
  side1,side2=a,b
if hypotenuse**2==side1**2+side2**2:
  print('Valid')
else:
  print("Not valid")
  
#  Input a number and check if it is an Armstrong number 
num=int(input())
a=num//100
b=(num%100)//10
c=(num)%10
if num==a**3+b**3+c**3:
  print("Amstrong nummber")
else:
  print("Not a Amstrong Number")
  

# 06-09-2025  
'''Water Consumption Bill 💧
Input: liters of water used.

Rules:
≤ 1000 liters → ₹5 per 100 liters.
1001–5000 liters → ₹8 per 100 liters.
5000 liters → ₹12 per 100 liters.'''

liters=int(input())
if liters<=1000:
  price=(liters/100)*5
elif 1001>liters<5000:
  price=(liters/100)*8
elif liters>5000:
  price=(liters/100)*12
print(price)

'''Employee Bonus System 🏢
Input: years of experience, performance rating (1–5).
Rules:
If exp ≥ 5 and rating ≥ 4 → Bonus = 20% of salary.
If exp ≥ 3 and rating ≥ 3 → Bonus = 10% of salary.
Else → No bonus.'''

years=int(input())
rating=int(input())
salary=int(input())
if (years>=5) and (rating>=4):
  print("20% of salary is: ",salary*0.20)
elif (years>=3) and (rating>=3):
  print("10% of salary is: ",salary*0.10)
else:
  print("No bonus")
  
'''Electricity Bill Calculator 💡
Problem:
Write a program to calculate the total electricity bill based on the number of units consumed.
Billing Rules:
For the first 100 units → ₹5 per unit.
For the next 100 units (101–200) → ₹7 per unit.
For units above 200 → ₹10 per unit.'''

units=int(input())
if units<=100:
  price=units*5
elif units<=200:
  price=(100*5)+((units-100)*7)
else:
  price=(100*5)+(100*7)+((units-200)*10)
print(price)

''' Cab Fare Calculator 
For the first 5 km, the fare is ₹50 per km.
For the next 10 km (i.e., from 6 km to 15 km), the fare is ₹10 per km.
Beyond 15 km, the fare is ₹15 per km.'''

km=int(input())
if km<=5:
  fare=km*50
elif km<=15:
  fare=50*5+(km-5)*10
else:
  fare=50*5+10*10+(km-15)*15
  
'''ATM Withdrawal System
Input: amount user wants to withdraw.
Rules:
Must be multiple of 100.
ATM balance = ₹10,000.
If amount > balance → show "Insufficient Balance".
If amount ≤ balance and valid multiple → show "Transaction Successful", new balance.
Else → "Invalid Amount".'''
amount=int(input())
balance=10000
if amount>balance:
  print("Insufficient Balance")
elif (amount<=balance) and (amount%100==0):
  print("Transaction Successful")
  print("New Balance is : ",balance-amount)
else:
  print("Invalid amount")
  
'''E-Commerce Delivery Charges 📦
Input: order amount, membership status (Prime/Normal).
Rule:
Prime users → Free delivery always.
Normal users:
Order ≥ ₹1000 → Free delivery.
Else → Delivery charge ₹100.'''

amount=int(input())
status=input()
if status=="Prime":
  print("Free deilvery always")
elif status=="Normal":
  if amount>=1000:
    print("Free delivery")
  else:
    print("Delivery charge is 100 extra: ",amount+100)
    
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
    
    
# Tax Calculator with Multiple Slabs
tax=int(input())
income=int(input())
if income<=250000:
    print("no tax")
elif (income>250000) and (income<500000):
    print(tax*0.5)
elif (income>500000) and (income<1000000):
    print(tax*0.20)
else:
    print(tax*0.30)
  
  
'''
Given an integer,n , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==0) and (n>=2) and (n<=5):
        print("Not Weird")
    elif (n%2==0) and (n>=6) and (n<=20):
        print("Weird")
    elif (n%2==0) and (n>20):
        print("Not Weird")
    else:
        print("Weird")
        
'''Movie Ticket Discount
Weekday = ₹200, Weekend = ₹300
Age < 12 or Age ≥ 60 → 50% discount
If Day = “Wednesday” → extra 20% discount'''

age=int(input())
day=input()
if day=="Weekday":
    price=200
else:
    price=300
if age<12 or age>=60:
    price=price*0.50
elif day=="Wednesday":
    price=price*0.80
print(price)


'''. Flight Ticket Price System
A passenger books a flight.
Class: Economy → ₹5000, Business → ₹10,000, First → ₹20,000
If Age < 12 → 50% discount
If Age ≥ 60 → 30% discount
If Day = “Friday” → 10% surcharge (extra charge)'''

day=input()
age=int(input())
Class=input()
if Class=="Economy":
    price=5000
elif Class=="Business":
    price=10000
else:
    price=20000
if age<12:
    price=price*0.50
elif age>=60:
    price=price*0.30
if day=="Friday":
    price=price*1.10
print(price)

'''E-commerce Discount Engine
An online store applies discounts:
If cart value < ₹1000 → No discount
If cart value 1000–5000 → 10% discount
If cart value > 5000 → 20% discount
If payment mode = “Credit Card” → extra 5% discount'''

value = int(input())
mode = input()
if value<1000:
    price=value
elif 1000<=value<=5000:
    price=value*0.90  
else:
    price=value*0.80   
if mode=="Credit Card":
    price=price*0.95
print(price)


'''Electricity Bill Calculator
0–100 → ₹5/unit
101–300 → ₹8/unit
301+ → ₹10/unit + 15% surcharge if bill > ₹2000'''

units=int(input())
if units<=100:
    bill=units*5
elif units<=300:
    bill=(100*5)+(units-100)*8
else:
    bill=(100*5)+(200*8)+(units-300)*10
if bill>2000:
    bill+=bill*0.15
print(bill)

'''Password Strength Checker 
Only numbers → Weak
Only letters → Medium
Letters + numbers → Strong
Letters + numbers + special chars → Very Strong'''
password = input()
if password.isdigit():
    print("Weak")
elif password.isalpha():
    print("Medium")
elif password.isalnum():
    print("Strong")
else:
    print("Very Strong")


    





  
