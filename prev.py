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
