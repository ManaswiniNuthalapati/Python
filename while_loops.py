# print hello 5 times
i=int(input())
n=int(input())
while i<=n:
  print("Hello")
  i+=1
    
# print numbers from 1 to N
n=int(input())
i=0
while i<=n:
    print(i)
    i=i+1 

# Sum of first N natural numbers
n=int(input())
i=1
total=0
while i<=n:
  total=total+i
  i=i+1
print(total)

#print even numbers till numbers
n=int(input())
i=2
while i<=n:
  print(i)
  i=i+2

#print odd numbers till numbers
n=int(input())
i=1
while i<=n:
  print(i)
  i=i+2
  
# print product on numbers
n=int(input())
i=1
total=1
while i<=n:
  total=total*i
  i=i+1
print(total)


# Reverse Counting
n=int(input())
i=n
while i>=1:
  print(i)
  i=i-1

# Multiplication of a number
n=int(input())
a=int(input())
i=1
while i<=a:
  print(i*n)
  i+=1

# Program to print the integers from M to N
m=int(input())
n=int(input())
while m<=n:
  print(m)
  m=m+1
  
# program to print cubes of a number
n=int(input())
i=1
while i<=n:
  print(i**3)
  i+=1
  
# print numbers divisible by 3
n=int(input())
i=3
while i<=n:
  print(i)
  i+=3

# program to print the numbers divisible by 3 and 5
n=int(input())
i=1
while i<=n:
  if i%3==0 and i%5==0:
    print(i)
  i+=1
  
  # count the no of digit separatelly
n=int(input())
count=0
if n==0:
  count=1
else:
  while n>0:
    n=n//10
    count+=1
print(count)

# Find the sum of digits of a number
n=int(input())
total=0
while n>0:
    digit=n%10        
    total=total+digit 
    n=n//10           
print(total)

# Reverse a number
n=int(input())
reverse=0
while n>0:
  digit=n%10
  reverse=reverse*10+digit
  n=n//10
print(reverse)

#palindrome or  not
n=int(input())
temp=n
reverse=0
while n>0:
  digit=n%10
  reverse=reverse*10+digit
  n=n//10
if temp==reverse:
  print("Palindrome")
else:
  print("Not palindrome")
  
  # factorial of a nummber
n=int(input())
i=1
count=0
while i<=n:
    if i%2!=0:
        count+=1
    i+=1          
print(count)

# program that takes a number n and an integer m as input and prints n, m times (each on a new line) using a for loop.
n=input()
m=int(input())
i=1
while i<=m:
  print(n)
  i+=1
  
# print divisors of a num
n=int(input())
i=1
while i<=n:
  if (n%i==0):
    print(i)
  i+=1
  
# Given an integer n, print the squares of all non-negative integers less than n, each on a new line.
n = int(input())
i=0
while i<n:
        print(i**2)
        i=i+1
   
# Find the Largest digit in a number
n=int(input())
largest=0 
while n>0:
  digit=n%10
  if digit>largest:
    largest=digit
  n=n//10
print(largest)

# Find the GCD Numbers
a=int(input())
b=int(input())
if a<b:
    smaller=a
else:
    smaller=b
gcd=1
i=1
while i<smaller:
    if a%i==0 and b%i==0:
        gcd=i  
    i+=1
print(gcd)
  
  





    

    

