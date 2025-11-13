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