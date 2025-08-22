#1
# Given a,b variables and printing these variables with space, with separator and without separator
a=input()
b=input()
c=input()
# with space
print(a,b)
# with separator
print(a,b,a+c+b)
# without space
print(a+b)

#2
# Declare two integer variables and print their sum.
a = 10
b = 20
print(a + b)

#3
# Store an integer in a variable, then change its value to a float and print both.
x = 25
print(x)      
x = float(x)
print(x)


#4
# Assign the same value to three variables in one line and print them.
a = b = c = 100
print(a, b, c) 


#5
# Assign multiple values to multiple variables in one line and print them.
a, b, c = 1, 2, 3
print(a, b, c)

#6
# Store your age in a variable and print "I am X years old" using that variable.
age = 19
print("I am", age, "years old") 

#7
# Concatenate two string variables and print the result.
first = "Hello"
second = "World"
print(first + " " + second) 

#8
# Assign a decimal number to a variable and convert it into an integer.
x = 12.9
print(int(x)) 

#9
# Assign a value to a variable and check its type using type().
x = 100
print(type(x))

#10
# Store a string "100" in a variable, convert it into an integer, and add 50.
s = "100"
n = int(s)
print(n + 50)

#11
# Demonstrate variable reassignment by assigning different data types.
x = 10
print(x)        
x = "Hello"
print(x)        
x = 3.14
print(x) 