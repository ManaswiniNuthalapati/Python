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

'''
Write a function square(n) that returns 
the square of a number. Print the result for 4.
'''
def square(n):
  return n*n
print(square(4))

'''
Write a function country(name, c="India") that prints:
My name is <name> and I am from <c>
Call it once with only name
Call it once with name and country
'''
def country(name, c="India"):
  print("My name is ",name,"I am from",c)
country("Manu")
country("Manu","India")

'''
Write a function multiply(a, b, c=1) 
that multiplies three numbers, where c has a default value.'''
def multiply(a,b,c=1):
  return a*b*c
print(multiply(2,3))
print(multiply(2,3,4))

'''
Write a function student(name, age, branch)
and call it using keyword arguments in any order.'''
def student(name,age,branch):
  print(name,age,branch)
student("Manu",19,"DS")

'''
Write a function book(title, author, price) and call it like this:
book(price=300, title="Python", author="Guido")
'''
def book(title,author,price):
  print(title,author,price)
book(price=300,title="Python",author="Guido")

'''
Write a function total(*numbers) that 
prints the sum of all numbers passed.'''
def total(*numbers):
  print(sum(numbers))
total(1,2,3)

# Sum of all numbers
def total(*numbers):
    print(sum(numbers))
total(1, 2, 3, 4) 

# Print each item on new line
def print_items(*items):
    for item in items:
        print(item)
print_items("apple", "banana", "cherry")

# Return largest number
def max_number(*nums):
    return max(nums)
print(max_number(10, 5, 20, 3))

# Count how many arguments
def count_args(*args):
    print(len(args))
count_args(1, 2, 3, 4, 5)

'''
*args — Arbitrary Positional Arguments
Use a single asterisk (*) before a parameter to let the function accept multiple positional arguments.
Inside the function, these arguments are received as a tuple.
'''
def my_function(*numbers):
    for num in numbers:
        print(num)
my_function(1, 2, 3, 4)
'''
**kwargs — Arbitrary Keyword Arguments
Use double asterisks (**) before a parameter to accept multiple named arguments.
Inside the function, these are stored in a dictionary, where keys are argument names and values are their values.
'''
def person_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
person_info(name="Tobias", age=30, city="Bergen")

# Sum of numbers
def sum_all(*nums):
    total = 0
    for n in nums:
        total=total + n
    return total
print(sum_all(1, 2, 3, 4))

# Find maximum number
def find_max(*nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val
print(find_max(3, 7, 2, 9, 1)) 

'''Scope in Python means where in your code a variable can be seen and used.
It tells Python where a variable “lives” and where it can be accessed.
1. Global Scope

🔹 A global variable is one that is created outside any function — at the top level of your code.
✔ You can use a global variable anywhere in your program — inside functions and outside functions.

2. Local Scope
🔹 A local variable is created inside a function — and it only exists inside that function.

Why Scope Matters

✔ Scope helps prevent variables from conflicting with each other.
✔ It tells Python where it’s allowed to read or change a variable.
✔ It helps organize your code better.
'''
# Global Variable Access
x = 10
def func():
    print(x)
func()
print(x)

# Local Variable Outside Function
def func():
    y = 5
    print(y)
func()

# Local vs Global with Same Name
a = 100
def test():
    a = 50
    print(a)
test()
print(a)

# Changing Local Does Not Change Global
x = 20
def change():
    x = 10
    print(x)
change()
print(x)

'''
Given dictionary:
dic = {'ram': 20, 'krish': 23, 'shyam': 21, 'radha': 25, 'chandu': 22}
a) Print all names and ages
'''
dic = {'ram': 20, 'krish': 23, 'shyam': 21, 'radha': 25, 'chandu': 22}
for name, age in dic.items():
    print(name, age)

# Print only names whose age > 22
for name, age in dic.items():
    if age > 22:
        print(name)
        
'''
Given list:
lst = [10, 20, 16, 23, 12, 25, 16, 16, 10, 20]
# print the number which comes 3 times
'''
lst=[10, 20, 16, 23, 12, 25, 16, 16, 10, 20]
freq={}
for n in lst:
    if n in freq:
        freq[n]+=1
    else:
        freq[n]=1
for key, value in freq.items():
    if value==3:
        print(key)
        
# Check even or odd for each number in a list
def check_even_odd(nums):
    result={}
    for n in nums:
        if n%2==0:
            result[n]="Even"
        else:
            result[n]="Odd"
    return result
numbers=[1,2,3,4,5,6]
print(check_even_odd(numbers))

# Return True if string contains vowels
def contains_vowel(s):
    vowels="aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            return True
    return False
print(contains_vowel("sky"))     
print(contains_vowel("hello"))   