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