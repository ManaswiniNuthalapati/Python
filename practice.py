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

# Find Greatest and Smallest among Three numbers
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

# Check whether a Number is Multiple of Another Number
num=0
n=5
if num%n==0:
   print(True)
else:
  print(False)

# Grade calculation system using marks
marks=84
if marks>=90:
  print("Grade is:","A")
elif 80<marks<89:
  print("Grade is:","B")
elif 70<marks<79:
  print("Grade is:","C")
elif 60<marks<69:
  print("Grade is:","D")
else:
  print("Grade is:","E")
  
# Print numbers from 1 to N
n=10
for i in range(1,n+1):
  print(i,end=" ")

# Print numbers from N to 1
n=10
for i in range(n+1,1,-1):
  print(i,end=" ")
  
# Print even numbers from 1 to 100
n=100
for i in range(n+1):
  if i%2==0:
    print(i)
  
# Print odd numbers from 1 to 100
n=100
for i in range(n+1):
  if i%2!=0:
    print(i)


# Print multiplication table of a number
n=5
for i in range(1,10):
  print(n*i)

# Find sum of first N natural numbers
n=10
sum=0
for i in range(n+1):
  sum+=i
print(sum)

# Count total numbers from 1 to N
n=10
count=0
for i in range(n+1):
  count+=1
print(count)

# Print all numbers divisible by 5 between 1 and 100
for i in range(1,100):
  if i%5==0:
    print(i)
    
# Find factorial of a number
n=5
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)

# Print Fibonacci series
n=5
a=0
b=1
for i in range(n+1):
  print(a,end=" ")
  c=a+b
  a=b
  b=c

# Reverse a number
a=102
b=str(a)
rev=""
for i in b:
  rev=i+rev
print(int(rev))

# Count number of digits
n=1234567890
n_1=str(n)
count=0
for i in n_1:
  count+=1
print(count)

# Sum of digits of a number
n="1234567890"
n.split()
sum=0
for i in n:
  sum+=int(i)
print(sum)
  
# Check whether a number is palindrome
n=12345
n_1=str(n)
rev=""
for i in n_1:
  rev=i+rev
if n==rev:
  print("Palindrome")
else:
  print("Not Palindrome")

# Check whether a number is prime
n=13
if n<=1:
  print(False)
else:
  for i in range(2,n):
    if n%i==0:
      print(False)
      break
  else:
    print(True)
# Print all prime numbers in a range
for n in range(1,11):
  if n<=1:
    continue
  for i in range(2,n):
    if n%i==0:
      break
  else:
    print(n)

# Check whether a number is Armstrong
n=153
length=len(str(n))
sum=0
for i in str(n):
  sum+=int(i)**length
if n==sum:
  print("Armstrong")
else:
  print("Not Armstrong")