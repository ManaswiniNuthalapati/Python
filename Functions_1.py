'''
A function is a block of code that runs only when it is called.
You can pass data into a function, and it can return data as a result.

Functions help you:
Reuse code
Make programs cleaner
Avoid writing the same code again and again

Summary 
Use def to create a function
Call a function using ()
Functions can take parameters
Use return to send back a value
You can set default values for parameters
'''
# Create and Call a Function
def my_function():
    print("Hello, Python!")
my_function()

# Write a function greet(name) that prints "Hello" and the given name.
def greet(name):
    print("Hello", name)
greet("Manaswini")

# Write a function add(a, b) that prints the sum of two numbers.
def add(a, b):
    print(a + b)
add(10, 5)

# Write a function square(n) that returns the square of a number and print the result.
def square(n):
    return n * n
result = square(4)
print(result)

# Write a function greet(name="User") that prints "Hello" and the name. Call it with and without an argument.
def greet(name="User"):
    print("Hello", name)
greet("Vinaya")
greet()

# Write a function print_list(items) that prints each item in a list.
def print_list(items):
    for i in items:
        print(i)
numbers = [1, 2, 3, 4, 5]
print_list(numbers)