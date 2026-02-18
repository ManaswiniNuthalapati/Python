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

'''
What Are Arguments in Python?

Arguments are values you pass into a function when you call it.
They are placed inside the parentheses after the function name.
Arguments allow you to send data into functions so that the function can use that data.

Example
def greet(name):
    print("Hello " + name)
greet("Alice")  

Here:
name inside the function is called a parameter.
"Alice" is the argument passed to the function.

Types of Arguments in Python
Python supports several ways of passing arguments — each has a specific purpose:
Argument Type	                Description
Positional	                    Passed in order
Keyword	                        Passed with name=value
Default	                        Has a default value if not provided
*args	                        Accepts any number of positional values
**kwargs	                    Accepts any number of keyword values
'''
'''
Write a function add(a, b) that
prints the sum of two numbers. Call it with 5 and 7.'''
def add(a,b):
  return a+b
add(5,7)

'''Write a function greet(name) that prints:
Hello, <name>
Call it with your name.'''
def greet(name):
  result="hello" + name
greet("Manu")
