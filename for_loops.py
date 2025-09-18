# Print numbers from 1 to 10.
for i in range(1,11):
  print(i)
  
# Print numbers from 1 to 10.
x=int(input())
for i in range(x):
  print(i+1)
  
# print first even numbers
for i in range(20,0,-2):
  print(i)
  
# print multipplication of a number
n=int(input())
for i in range(n):
  print(i*n)
  
# print sum of numbers from 1 to 50
n=int(input())
total=0
for i in range(n+1):
  total=total+i
print(total)

# print hello n times
n=int(input())
for i in range(n):
  print("Hello")

# program that takes a number n and an integer m as input and prints n, m times (each on a new line) using a for loop.
n=input()
m=int(input())
for i in range(m):
  print(n)

#  multiplication table of n up to 10 in one line using a for loop.
n = int(input())
for i in range(1,11):
    print(n*i,end=" ")
        
#print divisors of a num
n=int(input())
for i in range(1,n+1):
  if (n%i==0):
    print(i)
    
# Check prime or not
n=int(input())
i=2
prime=True
if n<=1:
  prime=False
else:
  while i<n:
    if n%i==0:
      prime=False
    i+=1
if prime:
  print(True)
else:    
  print(False)
  
# fibonacci numbers-continous numbers
n=int(input())
if n==0:
    fib=0
elif n==1:
    fib=1
else:
    a,b=0,1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    fib=b
print(fib)


