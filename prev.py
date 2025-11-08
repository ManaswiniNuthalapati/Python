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