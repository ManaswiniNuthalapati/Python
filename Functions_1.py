
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