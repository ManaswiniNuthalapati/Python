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