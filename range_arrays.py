'''
Python range() Function
1. Definition
The range() function returns a sequence of numbers, starting from 0 by default, 
incrementing by 1, and stopping before the specified number.
It is commonly used with for loops to iterate a specific number of times.

Syntax
range(start, stop, step)
Parameters
Parameter	         Description
start	             Starting number of the sequence. Default = 0
stop	             The sequence stops before this value
step	             Increment value between numbers. Default = 1
'''

'''
Python Arrays (According to W3Schools)
1. What is an Array?
An array is a special variable that can store multiple values in a single variable.
Instead of creating many variables like:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

You can store them together in one array:
cars = ["Ford", "Volvo", "BMW"]
This makes it easier to manage large collections of data.

Python does not have built-in arrays like some other languages.
Instead, Python uses lists as arrays.

Array Methods (Important)
Python arrays (lists) have many built-in methods.

Method	    Description
append()	Adds element at end
insert()	Adds element at specific position
remove()	Removes element by value
pop()	    Removes element by index
sort()	    Sorts array
reverse()	Reverses array
count()	    Counts occurrences
index()	    Returns index of element
clear()	    Removes all elements
copy()	    Returns copy of array
'''

# Print numbers from 1 to n
n=int(input())
for i in range(1,n+1):
    print(i)
    
# Print even numbers from 1 to n
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)
        
# Print numbers from n to 1
n=int(input())
for i in range(n,0,-1):
    print(i) 
 
# Find sum of numbers from 1 to n
n=int(input())
total=0
for i in range(1,n+1):
    total+=i
print(total)

#  Print multiplication table of a number
n=int(input())
for i in range(1,11):
    print(n*i)

# Print all elements of an array
arr=[4,7,2,9]
for i in range(len(arr)):
    print(arr[i])

# Find sum of array elements
arr=[2,5,7,1]
total=0
for i in range(len(arr)):
    total+=arr[i]
print(total)

# Find maximum element in array
arr=[3,9,1,6,4]
max_val=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
print(max_val)

# Count even numbers in array
arr = [1,2,3,4,5,6]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print(count)

# Remove all zeros from array
n=[1,0,2,0,3,0,4]
new=[]
for i in n:
  if i!=0:
    new.append(i)
print(new)

# Find the smallest element in an array.
n=[8,3,6,2,7]
min=n[0]
for i in n:
  if i<min:
    min=i
print(min)

# Find the second largest element in an array.
arr=[5,9,3,8,7]
large=arr[0]
sec=arr[0]
for i in arr:
    if i>large:
        sec=large
        large=i
    elif i>sec and i!=large:
        sec=i
print(sec)

# Reverse an array. 
arr=[1,2,3,4,5]
l=0
r=len(arr)-1
while l<r:
 arr[l],arr[r]=arr[r],arr[l]
 l+=1
 r-=1
print(arr)

# Count Occurrences of a Number
arr=[1,2,2,3,2,5]
target=2
count=0
for i in arr:
 if i==target:
  count+=1
print(count)