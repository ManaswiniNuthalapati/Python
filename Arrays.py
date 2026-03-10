# Write a program to print all elements of an array.
n=[5, 3, 8, 2]
for i in range(len(n)):
    print(n[i],end=" ")
    
# Sum of Array Elements
n=[1,2,3,4]
sum=0
for i in range(len(n)):
    sum+=n[i]
print(sum)

#  Find Largest Element
n=[3,7,2,9,5]
large=n[0]
for i in range(len(n)):
    if n[i]>large:
        large=n[i]
print(large)