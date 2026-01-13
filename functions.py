'''
What is a Function?
A function is a block of code that performs a specific task.
It helps reuse code, avoid repetition, and make programs organized and modular.

🔹 Defining a Function
Use the def keyword.
EX:
def fun():
    print("Welcome")

🔹 Calling a Function
Use the function name with parentheses.
EX: fun()

🔹 Function Arguments
Arguments are values passed to a function.
A function can take zero or more parameters.

🔹 Types of Function Arguments
1️⃣ Default Arguments
Use default values if no argument is given.
EX: def myFun(x, y=50):

2️⃣ Keyword Arguments
Pass values using parameter names (order doesn’t matter).
EX: student(fname="Geeks", lname="Practice")

3️⃣ Positional Arguments
Values assigned based on position.
EX: nameAge("Suraj", 27)

4️⃣ Arbitrary Arguments
*args → variable number of non-keyword arguments
**kwargs → variable number of keyword arguments
EX: def myFun(*args, **kwargs):

🔹 Function Within Function (Nested Function)
A function defined inside another function.
Can access variables of the outer function.

🔹 Anonymous Functions (Lambda)
Functions without a name.
Created using lambda.
lambda x: x*x*x

🔹 Return Statement
return sends a value back to the caller.
Ends the function execution.
return value

🔹 Pass by Reference vs Pass by Value
Python uses pass-by-object-reference.
Mutable objects (list, dict): changes affect original.
Immutable objects (int, string, tuple): original value unchanged.

🔹 Recursive Functions
A function that calls itself.
Must have a base case to stop recursion.
 EX: def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    '''
# Function to Print a Message
def greet():
    print("Hello, World!")
greet()

# Add Two Numbers
def add(a, b):
    print(a+b)
add(3,5)

# Return the Square of a Number
def square(n):
    return n*n
print(square(4))

# Print a Name
def print_name():
    print("My name is Manaswini")
print_name()


def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(10)
