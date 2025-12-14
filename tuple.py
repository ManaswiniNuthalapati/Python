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