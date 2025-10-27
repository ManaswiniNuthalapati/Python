# Lists
"""
Lists in Python-->dynamic arrays that store items in [ ].
separated by commas.
It is a sequence datatype used to store a collections of data.

creating a list --> []
accessing element from list through indexing
-ve indexing
size of the list --> len()
adding elements 
--> append()
--> insert() - adding ele at specific position

del keyword --> delete values by index
remove() method --> removes the first occurancce of a specific value
pop() --> removes and returns an item at specific index

max() --> returns the largest value
min() --> returns the smallest value

sort() --> sorts elements in asc,des order
reverse() --> reverses the elements


"""
'''
Create a list named colors with the elements ["red", "green", "blue", "yellow"].
Print the first and last elements using both positive and negative indexing.
'''
color=["red","green","blue","yellow"]
print(color[1])
print(color[-1])

# negative Indexing
print(color[-4])
print(color[-1])

# Create a list of 5 fruits and print the third fruit.
fruits=["apple","kiwi","orange","guava","banana"]
print(fruits[2])

# Create a 2D list called matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]].
# int the value 80 using nested indexing.
matrix=[[10,20,30],[40,50,60],[70,80,90]]
print(matrix[2][1])