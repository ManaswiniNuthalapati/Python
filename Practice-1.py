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

'''
Write a program that computes the value of
a + aa + aaa + aaaa
with a given digit as input.
'''
a=input().strip()
res=int(a)+int(a*2)+int(a*3)+int(a*4)
print(res)

'''
Write a program that accepts a comma-separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.
'''
n="without,hello,bag,world"
words=n.split(',')
words.sort()
res=",".join(words)
print(res)

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then 
check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''
n=input().split(",")
res=[]
for i in n:
  dec=int(a,2)
  if dec%5==0:
    res.append(i)
print(res)

'''
Write a program which accepts a sequence of comma separated integers as input
and prints the numbers that are divisible by 2 in a comma separated sequence.
'''
n=input().split()
res=[]
for i in n:
  if int(i)%2==0:
    res.append(i)
print(",".join(res))

'''
Write a program which can map() to make a list whose elements are square of elements in
[1,2,3,4,5,6,7,8,9,10]
'''
n=list(map(int,input().split()))
total=[]
for i in n:
  total.append(i*i)
print(total)

'''
Write a program which can use filter() to make a list 
whose elements are even numbers between 1 and 20 (both included).
'''
def is_even(x):
    return x % 2 == 0
nums = list(range(1, 21))
even_nums = list(filter(is_even, nums))
print(even_nums)

'''
Write a program which can compute the factorial of a number using recursion.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number: "))
print(factorial(n))

# Generate list of squares from 1 to 20
squares = []
for i in range(1, 21):
    squares.append(i * i)
print(squares)

'''
Write a program which can generate a tuple where the values are square of numbers
between 1 and 20 (both included).
Then print the first half values in the tuple.
'''
t = tuple(i*i for i in range(1, 21))
mid = len(t) // 2
print(t[:mid])

'''
Write a program which can generate a tuple where the values are square of numbers 
between 1 and 20 (both included).
Then print the last 5 elements in the tuple.
'''
t = tuple(i*i for i in range(1, 21))
print(t[-5:])

# Check if two strings are anagrams
s1="listen"
s2="silent"
s1=s1.replace(" ", "").lower()
s2=s2.replace(" ", "").lower()
if len(s1)!=len(s2):
    print("Not Anagrams")
else:
    if sorted(s1)==sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagrams")
        
# Find first non-repeating character (without def)
s="aabbcde"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
found=False
for ch in s:
    if freq[ch]==1:
        print("First non-repeating character:", ch)
        found=True
        break
if not found:
    print("No non-repeating character found")
    
# Find sum of all values in a dictionary
d = {"a": 10, "b": 20, "c": 30, "d": 40}
total = 0
for value in d.values():
    total += value
print(total)
    
# Invert a dictionary (swap keys and values)
d = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in d.items():
    inverted[value] = key
print("Original dictionary:", d)
print("Inverted dictionary:", inverted)

# Find First Non-Repeating Character in a String
s=input("Enter string: ")
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for ch in s:
    if freq[ch]==1:
        print("First non-repeating:",ch)
        break
      
# Find Second Largest Element in a List
lst=list(map(int, input().split()))
first=second=-10**18
for x in lst:
    if x>first:
        second=first
        first=x
    elif x!=first and x>second:
        second=x
print("Second largest:", second)

# Reverse Words in a Sentence
s=input("Enter sentence: ")
words=s.split()
words.reverse()
result=" ".join(words)
print(result)

# Find Duplicate Elements in a List
lst=list(map(int, input().split()))
seen=set()
duplicates=set()
for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print(list(duplicates))

# Check if Array is Sorted
arr=list(map(int, input().split()))
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")
    
Move All Zeros to End (Maintain Order)
arr = list(map(int, input().split()))
result = []
zero_count = 0
for x in arr:
    if x != 0:
        result.append(x)
    else:
        zero_count += 1
result.extend([0] * zero_count)
print(result)