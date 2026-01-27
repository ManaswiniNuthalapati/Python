# Check whether a number is positive or negative
a=20
if a>0:
  print("Positive")
elif a==0:
    print("Zero")
else:
  print("Negative")
  
# Check whether a number is Even or Odd
n=10
if n%2==0:
  print("Even")
else:
  print("Odd")
  
# Find Largest of Two Numbers
n1=10
n2=20
if n1>n2:
  print("Largest:",n1)
else:
  print("Largest:",n2)

# Find Smallest of Two Numbers
n1=10
n2=20
if n1>n2:
  print("Smallest:",n2)
else:
  print("Smallest:",n1)

# Find Largest of 3\three Numbers
n1=10
n2=20
n3=30
if n1>n2 and n1>n3:
  print("Largest:",n1)
elif n2>n1 and n2>n3:
  print("Largest:",n2)
else:
  print("Largest:",n3)
  
# Check whether a year is Leap Year or not
n=1900
if (n%4==0 and n%100!=0) or n%400==0:
  print("Leap Year")
else:
  print("Not leap Year")
  
# Check Eligibility for Voting
n=22
if n>=18:
  print("Eligible to vote")
else:
  print("Not Eligible")
  
# Check whether character is Vowel or Consonant
n="a"
if n in "aeiouAEIOU":
  print("vowel")
else:
  print("consonant")
  
# Check whether number is Divisible by 5 and 11
n=55
if n%5==0 and n%11==0:
  print("Divisible")
else:
  print("Not Divisible")
  
# Check whether all Three numbers are equal or not
n1=10
n2=10
n3=10
if n1==n2==n3:
  print("Equal")
else:
  print("Not Equal")

# Check whether a number lies between two given numbers or not
n=18
a=10
b=20
if a<n<b:
  print("Exists")
else:
  print("Not Exists")

# Find greatest and smallest among three numbers
n1=10
n2=20
n3=30
large=n1
small=n1
if n2>large:
  large=n2
if n3>large:
  large=n3
if n2<small:
  small=n2
if n3<small:
  small=n3
print(large)
print(small)

# Check whether a number is multiple of another number
num=0
n=5
if num%n==0:
   print(True)
else:
  print(False)

# Grade calculation system using marks
marks=84
if marks>=90:
  print("A")
elif 80<marks<89:
  print("B")
elif 70<marks<79:
  print("C")
elif 60<marks<69:
  print("D")
else:
  print("E")