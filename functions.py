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

# Find Maximum of Two Numbers
def maximum(a,b):
    if a>b:
        print(a)
    else:
        print(b)
maximum(8,3)

# Print Numbers from 1 to 5
def numbers():
    for i in range(1,6):
        print(i)
numbers()

# Print a Name
def print_name():
    print("My name is Manaswini")
print_name()

# Check Even or Odd
def check_even_odd(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(10)

# Find the Square Number
def square(num):
    print(num*num)
square(4)

# Print Numbers from 1 to N
def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(5)

# Check Positive or Negative
def check_number(n):
    if n>0:
        print("Positive")
    elif n<0:
        print("Negative")
    else:
        print("Zero")
check_number(-5)

# Sum of Numbers from 1 to N
def total(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print(s)
total(5)

# Sum of Two Numbers (Return Version)
def sum_two(a,b):
    return a+b
result=sum_two(10,20)
print(result)

# Multiply Two Numbers
def multiply(a,b):
    print(a*b)
multiply(4,6)

# Print Table of a number
def table(n):
    for i in range(1,11):
        print(n*i)
table(5)

# Count Digits
def count(n):
    print(len(str(n)))
count(12345)

# Check Palindrome Number
def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(121)