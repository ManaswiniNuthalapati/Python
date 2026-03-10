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

n=[1,2,3,4]
sum=0
res=[]
for i in range(len(n)):
    sum+=n[i]
    res.append(sum)
print(res)

# Find Index of Largest Element
arr=[4,7,9,2]
large=arr[0]
l_idx=0
for i in range(len(arr)):
    if arr[i]>large:
        large=arr[i]
        l_idx=i
print(large,"-",l_idx)

# Count Elements Greater Than X
arr = [1,5,7,2,9]
x = 5
count=0
for i in range(len(arr)):
    if arr[i]>x:
        count+=1
print(count)

# Check if Element Exists
arr = [3,6,1,9]
x = 6
'''if x in arr:
    print(True)
else:
    print(False)'''
for i in range(len(arr)):
    if arr[i]==x:
        res=True
        break
    else:
        res=False
print(res)      