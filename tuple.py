# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
'''
Tuples are written with round brackets.
Ex: mytuple = ("apple", "banana", "cherry")
'''
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Create a tuple with 5 integer values and print it.
a=(1,2,3,4,5)
print(a)

# Create a tuple with mixed data types and print it.
a=(1,"python",20.5,True)
print(a)

# Write a program to print the first element of a tuple.
a=(1,2,3,4,5)
print(a[0])

# Write a program to print the last element of a tuple using negative indexing.
a=(1,2,3,4,5)
print(a[-1])

# find the length of the tuple
a=(1,2,3,4,5)
print(len(a))

# Loop through a tuple and print all elements.
a=(1,2,3,4,5)
for i in a:
    print(a)
    
# Check whether a given element exists in a tuple.
a=(1,2,3,4,5)
b=1
for i in a:
    if b in a:
        print("True")
    else:
        print("False")
      
# Count how many times a specific element appears in a tuple.
a=(1,3,2,1,4,3,2,5)  
b=1
c=a.count(b)
print(c)

# Find the index of a given element in a tuple.
a=(1,2,3,4,5)
b=2
c=a.index(b)
print(c)

# Print the middle element of a tuple.
a=(1,2,3,4,5)
b=len(a)//2
print(a[b])

# Create a tuple with one element and print its data type.
a=("apple")
print(type(a))

# Convert a list into a tuple.
li=[1,2,3,4,5]
tup=tuple(li)
print(tup)

# Convert a tuple into list
a=(1,2,3,4,5)
li=list(a)
print(li)

# Add a new element to a tuple by using conversion.
a=(1,2,3,4,5)
b=list(a)
print(b)
b.append(6)
print(b)
c=tuple(b)
print(c)

# create a tuple and find its sum of all elements
a=(1,2,3,4,5)
total=0
for i in a:
  total+=i
print(total)

# Find the maximum and minimum value in a tuple.
a=(1,2,3,4,5)
print(min(a))
print(max(a))
                 # OR
a=(1,2,3,4,5)
max,min=a[0]
for i in a:
    if max>i:
        min=i
    else:
        max=i
print(min)
print(max)

# reverse a tuple using slicing
a=(1,2,3,4,5)
rev=a[::-1]
print(rev)

# print only even numbers and odd numbers separately in a tuple
a=(1,2,3,4,5,6,7,8,9)
even=[]
odd=[]
for i in a:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print(tuple(even))
print(tuple(odd))

# Create a nested tuple and print an inner element
a=(1,2,(10,20,30),3)
print(a[2][2])

# Create a tuple of numbers and find the sum of all its elements.
t=(10,20,30,40,50)
total=0
for i in t:
    total+=i
print(total)

# Find the Maximum and Minimum Element in a Tuple
t=(45,12,89,33,6)
max=t[0]
min=t[0]
for i in t:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)

# Create a tuple and check whether it is empty or not.
t=()
if len(t)==0:
    print("Tuple is empty")
else:
    print("Tuple is not empty")
    
# create a tuple and print only first 3 names
s=("Asha","Ravi","Kiran","Megha","Sita")
print(s[:3])

# Print all elements at even index positions from a tuple.
a=(10,20,30,40,50)
for i in range(len(a)):
    if i%2==0:
        print(a[i])
        
# Print all elements at odd index positions from a tuple.
a=(1,20,30,40,50,60)
for i in range(len(a)):
  if i%2!=0:
    print(a[i])
    
# Count how many elements are greater than 50 in a tuple.
a=(23,54,6,7,87,4,3,22)
count=0
for i in a:
  if i>50:
    count+=1
print(count)

# Create a tuple of 10 numbers and print only numbers divisible by 5.
a=(23,6,10,20,60,55,98)
for i in a:
  if i%5==0:
    print(i)
    
# Find the product of all elements in a tuple.
a=(1,2,3,4,5)
prod=1
for i in a:
  prod=prod*i
print(prod)

# Check whether a tuple is a palindrome or not.
#(Example: (1, 2, 3, 2, 1))
a=(1,2,3,2,1)
rev=()
for i in a:
  rev=(i,)+rev
print(rev)
if a==rev:
  print("Palindrome")
else:
  print("Not")

# find the second largest number in atuple
a=(12,46,76,43,54)
large=a[0]
sec=a[0]
for i in a:
  if i>large:
    sec=large
    large=i
  elif i>sec and i!=large:
    sec=i
print(large)
print(sec)
  
# remove all duplictes from a tuple
a=(1,4,3,5,1,4,3,6)
t=()
for i in a:
  if i not in t:
    t+=(i,)
print(t)

# Swap first and last element in a tuple
a=(1,4,3,2,6)
lst=list(a)
lst[0],lst[-1]=lst[-1],lst[0]
a=tuple(lst)
print(a)

# Split a tuple into wo equal halves
a=(1,2,3,4,5,6)
mid=len(a)//2
fir=a[:mid]
sec=a[mid:]
print(fir)
print(sec)

# Create an empty tuple and print it.
a=()
print(a)

# Create a tuple using the tuple() constructor.
a=tuple([1,2,3])
print(a)

#Create a tuple of characters from a string.
a=tuple("Python")
print(a)

# Print the data type of an empty tuple.
a=(1,2,3)
print(type(a))

# Create a tuple of 3 numbers and unpack them into 3 variables.
a=(1,2,3)
b,c,d=a
print(b)
print(c)
print(d)

# Print elements from index 2 to 5 in a tuple.
a=(1,2,3,4,5)
for i in range(2,5):
  print(a[i])

# Print all elements except the first and last one.
a=(1,2,3,4,5)
for i in range(1,len(a)-1):
  print(a[i])
  
# Print every alternate element from a tuple.
a=(1,2,3,4,5)
for i in range(len(a)):
  if i%2==0:
    print(a[i])
    
# Print the tuple in reverse order using slicing.
a=(1,2,3,4,5)
print(a[::-1])

# Access the third element from the end of a tuple.
a=(1,2,3,4,5)
print(a[-3])

# Access Values with index
days=("mon","tue","wed","thur","fri","sat","sun")
for i in range(len(days)):
  print(i,days[i])
  
# Create a tuple and replace all negative numbers with 0
a=(2,-1,5,-3,6,-9,4-6)
b=list(a)
for i in range(len(b)):
  if b[i]<0:
    b[i]=0
print(b)

# Find the difference between the largest and smallest element in a tuple.

a=(4,3,9,5,8,6,2)
large=a[0]
small=a[0]
for i in a:
    if i>large:
        large=i
    if i<small:
        small=i
print(large)
print(small)
print("Difference:",large-small)

# Find all elements that appear more than once in a tuple.
a=(2,5,4,6,2,1,8,9,1)
b=()
for i in a:
  if a.count(i)>1 and i not in b:
    b=b+(i,)
print(b)

# Convert tuple to list and add element
a = (1, 2, 3)
b = list(a)
b.append(4)
a = tuple(b)
print(a)

# Create two tuples and check whether they are equal.
a=(1,2,3,4,5)
b=(1,2,3,4,5)
if a==b:
  print("Equal")
else:
  print("Not Equal")
  
# Find the length of a tuple without using len()
a=(1,2,3,4,5)
count=0
for i in a:
  count+=1
print(count)

# Print elements at odd index positions using slicing.
a=(1,3,4,56,76,3)
print(a[0:6:2])

# Print the first half and second half of a tuple.
a=(45,7,6,87,43,9,33)
lst=list(a)
mid=len(lst)//2
print(a[:mid])
print(a[mid:])

# count how many positive and negative numbers are present in a tuple.
a=(23,-5,43,67,-55,-87,92,-5,65)
b=list(a)
pos=0
pos_1=()
neg=0
neg_1=()
for i in a:
  if i>0:
    pos+=1
    pos_1+=(i,)
  else:
    neg+=1
    neg_1+=(i,)
print(pos)
print(neg)
print(pos_1)
print(neg_1)
  
# Count how many zeros are present in a tuple.
a=(34,6,7,0,6,0,865,0,86,0,65,0)
count=0
for i in a:
  if i==0:
    count+=1
print(count)

# Print elements which are divisible by both 3 and 5.
a=(3,45,6,55,75,97,24,65,98,33,56)
b=()
for i in a:
  if i%3==0 and i%5==0:
    b+=(i,)
print(b)

# Find the average of elements in a tuple.
a=(1,2,3,4,5)
sum=0
count=0
for i in a:
  sum+=i
  count+=1
print(sum)
print(count)
print("Avg:",sum//count)
  
# Print elements whose value is equal to their index.
a=(4,1,6,98,4,65,6)
for i in range(len(a)):
    if i==a[i]:
      print("index:",i,"value:",a[i])
  
# Accessing tuples
a=input().split()
index=int(input())
print(a[index])

# Using Slicing
a=input().split()
fir=int(input())
last=int(input())
print(tuple(a[fir:last]))

# Creating a tuple
a=input().split()
print(tuple(a))

# Concatenation of tuples
a=input().split()
b=input().split()
print(tuple(a+b))

# Remove empty strings from a tuple.
a=("hi","","yoo","hello","")
b=list(a)
while "" in b:
    b.remove("")
print(tuple(b))

# Merge a list and tuple into a single tuple
a=[1,2,3]
b=(4,5,6)
b=list(b)
print(tuple(a+b))

# Find the **second smallest** element in a tuple.
a=(5,4,3,8,7)
b=list(a)
small=b[0]
sec=b[0]
for i in b:
    if i<small:
        sec=small
        small=i
    elif i<sec and i!=small:
        sec=i
print(small)
print(sec)
        
# Left Rotate Tuple
a=(1,2,3,4)
b=1
b=b%len(a)
res=a[b:]+a[:b]
print(res) 

# Right Rotate Tuple
a=(1,2,3,4)
b=1
b=b%len(a)
res=a[-b:]+a[:b]
print(res)

# Count how many elements are present inside a nested tuple (total count).
a=(1,2,(3,4,5),6,7)
print(len(a[2]))

# Find the maximum element inside a nested tuple.
a=(1,8,6,(9,5,3,2),19,10,12)
max=a[3][0]
for i in a[3]:
    if i>max:
        max=i
print(max)

# Access the last element of the inner tuple in a nested tuple.
a=(1,2,(3,4,5),(6,7,8))
print(a[3][-1])

# Count vowels present in a tuple of characters.
a=("apple","banana","orange")
count=0
for words in a:
    for i in words:
        if i in "AEIOUaeiou":
            count+=1
print(count)

# Decrement the tuple
arr=()
for i in arr:
  print(i-1, end=" ")
                         # OR
arr=()
result = []
for i in arr:
  result.append(i - 1)
print(tuple(result))

# Unpacking Tuple
a = (10,20,30)
x,y,z = a
print(x,y,z)

# Check if element exists
