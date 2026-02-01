'''
Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
res=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        res.append(str(i))
print(",".join(res))

'''
Question: Write a program which can compute the factorial of a given numbers. The results 
should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
'''
n=8
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

'''
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included).and then the program should print the dictionary. 
Suppose the following input is supplied to the 
program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
n=8
res={}
for key in range(1,n+1):
  res[key]=key*key
print(res)
  
'''
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number. Suppose the following input is supplied to the
program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
'''
n="34,67,55,33,12,98"
n_1=n.split(",")
print(list(n_1))
print(tuple(n_1))

'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters
in the sentence capitalized. Suppose the following input is supplied to the 
program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
'''
s="Hello world Practice makes perfect"
s=s.upper()
print(s)

'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
'''
s="Hello World"
upper=0
lower=0
for i in s:
  if i.isupper():
    upper+=1
  if i.islower():
    lower+=1
print(upper)
print(lower)

'''
Square Pattern
****
****
****
****
'''
n=4
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

'''
*
*
*
*
*
'''
n=5
for i in range(1,n+1):
  print("*")
  
'''
* * * * *
'''
n=5
for i in range(1,n+1):
  print("*",end=" ")

'''
Right angle triangle
*
* *
* * *
* * * *
'''
n=5
for i in range(1,n+1):
  for j in range(i):
    print("*",end=" ")
  print()
  
'''
Inverted Right Triangle
* * * *
* * *
* *
*
'''
n=5
for i in range(n,-1,-1):
  for j in range(i):
    print("*",end=" ")
  print()
  

'''
Number Square
1 1 1
1 1 1
1 1 1
'''
n=5
for i in range(n):
  for j in range(n):
    print(1,end=" ")
  print()
  
'''
Increasing Number Triangle
1
1 2
1 2 3
'''
n=3
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()
  
'''
Repeated Number Triangle
1
2 2
3 3 3
'''
n=3
for i in range(1,n+1):
  for j in range(1,i+1):
    print(i,end=" ")
  print()
  
'''
Star Pyramid
   *
  ***
 *****
*******
'''
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
  
'''
Inverted Pyramid
*******
 *****
  ***
   *
'''
n=5
for i in range(n,-1,-1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()

'''
Hollow Square
* * * *
*     *
*     *
* * * *
'''
n=5
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  

'''
Floyd’s Triangle
1
2 3
4 5 6
7 8 9 10
'''
n=5
num=1
for i in range(1,n+1):
  for j in range(1,i+1):
    print(num,end=" ")
    num+=1
  print()
  
'''
Diamond Pattern
   *
  ***
 *****
*******
 *****
  ***
   *
'''
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
for i in range(n-1,0,-1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
  
  '''
  Hollow Triangle
    *
   * *
  *   *
 *     *
*********
'''
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==1:
      print("*")
    elif i==n:
      print("*"*(2*n-1))
    else:
      print("*"+" "*(2*i-3)+"*")
'''
Butterfly Pattern
*       *
**     **
***   ***
**** ****
***   ***
**     **
*       *
'''
n=int(input())
for i in range(1,n+1):
  print("*"*i,end="")
  print(" "*(2*(n-i)),end="")
  print("*"*i)

for i in range(n,0,-1):
  print("*"*i,end="")
  print(" "*(2*(n-i)),end="")
  print("*"*i)
  
# Write a program that accepts a sentence and calculate the number of letters and digits.
n="hello world! 123"
alpha=0
num=0
for i in n:
  if i.isalpha():
    alpha+=1
  elif i.isdigit():
    num+=1
print("Letters:",alpha)
print("Digits:",num)

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
N='''Hello world
Python is easy
I love coding
'''
print(N.upper())