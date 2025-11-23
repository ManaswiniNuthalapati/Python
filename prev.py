# Sum of Digits Until Single Digit
num=int(input())
while num>=10:
    total=0
    while num>0:
        total+=num%10
        num//=10
    num=total
print(num)

# Reverse a String (No slicing)
string=input()
rev=""
for char in string:
    rev=char+rev
print(rev)

# Frequency Counter
lst=[2,2,3,1,3,3]
freq={}
for i in lst:
    freq[i]=freq.get(i,0)+1
print(freq)

# Split List in Half
lst=[1,2,3,4,5,6]
mid=len(lst) // 2
first_half=lst[:mid]
second_half=lst[mid:]
print(first_half)
print(second_half)

# List Difference
list1=[1,2,3,4,5]
list2=[3,4,6]
diff=[x for x in list1 if x not in list2]
print(diff)

# Cumulative Sum
lst=[1,2,3,4]
cum=[]
total=0
for x in lst:
    total += x
    cum.append(total)
print(cum)

# Count Divisors
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of divisors:", count)

# Sum of List Except Current Index
lst = [1, 2, 3]
result = []
total = sum(lst)
for x in lst:
    result.append(total - x)
print("Output:", result)

# Interchange First and Last Elements
lst = [10, 20, 30, 40]
lst[0], lst[-1] = lst[-1], lst[0]
print("After swapping:", lst)

#  Sort Without Using sort()
lst = [5, 2, 9, 1, 3]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)

# Count Prime Numbers in List
lst = [2, 3, 4, 5, 10, 11]
count = 0
for num in lst:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
print("Number of primes:", count)

# Hollow Square Pattern
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    
# Merge and Sort Lists
a = [3, 1, 4]
b = [2, 5, 0]
merged = a + b
for i in range(len(merged)):
    for j in range(i+1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Sorted merged list:", merged)

# Merge and Sort Lists
a = [3, 1, 4]
b = [2, 5, 0]
merged = a + b
for i in range(len(merged)):
    for j in range(i+1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Sorted merged list:", merged)

# Perfect Number
num = int(input("Enter a number: "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
if sum_div == num:
    print(num, "is a Perfect Number ✅")
else:
    print(num, "is not a Perfect Number ❌")
    
# Palindrome Number
num = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if rev == num:
    print("Palindrome ✅")
else:
    print("Not Palindrome ❌")

# Count Divisors
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of divisors:", count)

# Count Divisors
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of divisors:", count)

# Average of 4 numbers
a = float(input())
b = float(input())
c = float(input())
d = float(input())

avg = (a + b + c + d) / 4
print("Average:", avg)

# Print name, age, height formatted
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height in cm: "))

print(f"My name is {name}, I am {age} years old and {height} cm tall.")

# Convert minutes → hours + minutes
mins = int(input("Enter minutes: "))
hours = mins // 60
rem = mins % 60
print(f"{hours} hour(s) {rem} minute(s)")

# Full operator task
a = int(input())
b = int(input())
print("Add:", a+b)
print("Sub:", a-b)
print("Mul:", a*b)
print("Div:", a/b)
print("Mod:", a%b)
print("Floor div:", a//b)
print("Power:", a**b)

# Compare decimal parts of two floats
x = float(input())
y = float(input())
d1 = x - int(x)
d2 = y - int(y)
if d1 > d2:
    print("First has greater decimal part")
else:
    print("Second has greater decimal part")
    
# KM to meters, cms, mms
km = float(input("Enter km: "))
print("Meters :", km * 1000)
print("CM     :", km * 100000)
print("MM     :", km * 1000000)

# Percentage + rounded percentage
marks = int(input("Enter marks out of 600: "))
percentage = (marks / 600) * 100

print("Percentage:", percentage)
print("Rounded:", round(percentage))

# Absolute difference > 10
a = int(input())
b = int(input())
if abs(a - b) > 10:
    print("Difference > 10")
else:
    print("Difference <= 10")
    
# Using split() and join()
s = "hi how are you"
s = "".join(s.split())
print(s)

# Using Loop
s = "hi how are you"
result = ""
for i in s:
    if i != " ":
        result += i
print(result)

# reverse a number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10        
    rev = rev * 10 + digit  
    num = num // 10         
print("Reversed number:", rev)

# Count vowels in a string
s = "education"
vowels = "aeiouAEIOU"
count = 0
for i in s:
    if i in vowels:
        count += 1
print(count)

# Find the largest number in a list (without max())
lst = [10, 5, 22, 9, 31]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)

# Count words in a sentence
s = "hi how are you"
words = s.split()
print(len(words))

# Print Fibonacci series
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
    
# Remove duplicates from a list
lst = [1,2,3,2,1,4,5,4]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

# Check if two strings are anagrams
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
    
# Find factorial using a loop
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# Print pattern
'''
*
**
***
****
'''
for i in range(1, 5):
    print("*" * i)
    
# Print even and odd numbers separately from a list
lst = [10, 3, 5, 8, 2, 7]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)

# Swap two numbers WITHOUT a third variable
a = 5
b = 10
a, b = b, a
print(a, b)

# Check if a number is prime
num = 29
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not Prime")
    
# Print sum of digits of a number
num = 123
s = 0
while num > 0:
    s += num % 10
    num //= 10
print(s)

# Find common elements between two lists
a = [1,2,3,4]
b = [3,4,5,6]
common = []
for i in a:
    if i in b:
        common.append(i)
print(common)

# Take two numbers and print their sum
a = int(input())
b = int(input())
print(a + b)

Find area of a circle
r = float(input())
area = 3.14159 * r * r
print(area)