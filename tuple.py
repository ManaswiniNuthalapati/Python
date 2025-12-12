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