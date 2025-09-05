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