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
  
# print multiplication of a number
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
  

# Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.    
n1=int(input())
n2=int(input())
for i in range(1,11):
    a=n1*i
    b=n2*i
    print(a-b,end=" ")
    
# print odd numbers
def main():
    N = int(input())
    for i in range(N):
        if i%2==1:
            print(i)
    return 0
if __name__ == '__main__':
    main()
    
# Write a Python program to print all numbers from 1 to 20, but skip the multiples of 3.
for i in range(1,21):
  if i%3==0:
    continue
  print(i)
 
# Write a Python program to print numbers from 1 to 50, but stop printing if you reach a number greater than 30. 
n=int(input())
for i in range(1,n+1):
  if i>30:
    break
  print(i)
  
'''
You have numbers from 1 to 50. Write a program that:
Skips all multiples of 4 (use continue).
Stops completely if the number is greater than 40 (use break).
Prints all other numbers.
'''
n=int(input())
for i in range(1,n+1):
  if i%4==0:
    continue
  if i>=40:
    break
  print(i)

# From a given string, print only the consonants (skip vowels).
text = "python is fun"
vowels = "aeiouAEIOU"
for ch in text:
    if ch in vowels:
        continue  
    print(ch, end="")
    






