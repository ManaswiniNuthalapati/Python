# Swap two numbers without using 3rd variable
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)

#7
# Take a 3-digit number and print its reverse using only operators
a=int(input())
b=str(a%10)
c=str(a//10)
d=b+c
print(d)

#8
# Store your age in a variable and print the year you were born
birth_year=int(input())
curr_year=2025
print(curr_year-birth_year)
