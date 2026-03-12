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

'''
Find minimum element
'''
arr=[4,6,5,1,2,7]
small=arr[0]
small_idx=0
for i in range(len(arr)):
    if arr[i]<small:
        small=arr[i]
        small_idx=i
print(small,"-",small_idx)

# Find second largest element
arr=[4,6,5,1,2,7]
large=arr[0]
sec=arr[0]
for i in range(len(arr)):
    if arr[i]>large:
        sec=large
        large=arr[i]
if i>sec and i!=large:
    sec=i
print(sec)

# Check if array is sorted
arr=[1,2,3,4,5,6]
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        res="Sorted"
    else:
        res="Not"
        break
print(res)

# Count frequency of element
n=[5,6,3,7,4,3,8,6,1,9,1]
freq={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# Find element appearing most times
n = [5,6,3,7,4,3,8,6,1,9,1]
freq={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
max_count=0
max_ele=None
for key in freq:
    if freq[key]>max_count:
        max_count=freq[key]
        max_ele=key
print(max_ele)

# Find duplicates in array
n = [5,6,3,7,4,3,8,6,1,9,1]
freq = {}
for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key in freq:
    if freq[key] > 1:
        print(key)
        
'''
Reverse an array
'''
n=[1, 2, 0, 4, 5]
n_1=[]
for i in range(len(n)-1,-1,-1):
    n_1.append(n[i])
print(n_1)

# Move zeros to end
n=[0, 1, 0, 3, 12]
n_1=[]
n_2=[]
for i in range(len(n)):
    if n[i]!=0:
        n_1.append(n[i])
    elif n[i]==0:
        n_2.append(n[i])
res=n_1+n_2
print(res)