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
        