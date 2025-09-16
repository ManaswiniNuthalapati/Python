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
