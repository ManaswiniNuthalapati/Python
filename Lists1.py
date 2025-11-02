# Find all even numbers from a given list
num=[10, 21, 4, 45, 66, 93, 11]
even=[]
for i in num:
    if i%2==0:
        num.append(i)
print(even)

# Find all odd numbers and print them in a single line
num=[10, 21, 4, 45, 66, 93, 11]
print("Odd numbers:", end=" ")
for i in num:
    if i%2!=0:
        print(i,end=" ")