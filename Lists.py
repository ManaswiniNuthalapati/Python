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
remove() method --> removes the first occurance of a specific value
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

'''
Create an empty list named numbers.
Use a loop to append numbers 1 to 5 into it.
Print the final list.
'''
list=[]
for i in range(1,5):
  list.append(i)
print(list)
  
'''
Given fruits = ["apple", "banana", "cherry"],
insert "mango" at index 1.
append "grapes" at the end.
Print the updated list.
'''
fruits=["apple","banana","cherry"]
fruits.insert(1,"mango")
fruits.append("grapes")
print(fruits)

'''
Create a list languages = ["Python", "Java"].
Use append() to add a tuple ("C", "C++") as one element.
Print the list and observe what happens.
'''
list=["Python","java"]
list.append(("C","C++"))
print(list)

'''
Create a list nums = [1, 2, 3, 4, 3, 5].
Remove the first occurrence of 3.
Then remove the last element.
Print the updated list.
'''
num=[1,2,3,4,3,5]
num.remove(3)
num.pop()
print(num)

'''
Create a list items = ["pen", "pencil", "book", "eraser"].
Delete the item at index 2 using del.
Print the list after deletion.
'''
items=["pen","pencil","book","eraser"]
del items[2]
print(items)

# Given fruits = ["apple", "banana", "cherry", "mango"], replace "banana" with "kiwi"
fruits=["apple","banana","cherry","mango"]
fruits[1]="kiwi"
print(fruits)

'''
Create a list numbers = [3, 7, 2, 8, 5, 7, 3].
Print the length of the list.
Print how many times 7 appears.
Print the largest and smallest numbers
'''
numbers=[3, 7, 2, 8, 5, 7, 3]
print(len(numbers))
print(numbers.count(7))
print(max(numbers))
print(min(numbers))

'''
Create a list of numbers marks = [90, 67, 88, 75, 95].
Find and print the highest and lowest marks using max() and min().
Then use sort() to arrange them in ascending order.
'''
marks=[90, 67, 88, 75, 95]
print(max(marks))
print(min(marks))
marks.sort()
print(marks)

'''
Create a list fruits = ["banana", "apple", "mango", "cherry"].
Sort the list alphabetically.
Then reverse the list.
Print the final result.
'''
fruits=["banana", "apple", "mango", "cherry"]
fruits.sort()
fruits.reverse()
print(fruits)
