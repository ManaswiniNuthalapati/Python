# Sets
'''
A set is an unordered collection of unique elements
Written using { }
Duplicates are automatically removed
Unindexed (no positions like 0,1,2…)
Mutable (you can add/remove items)
'''
# Important Set Methods
'''
add()       # Add element
remove()    # Remove element (error if not exist)
discard()   # Remove element (no error)
union()     # Combine sets
intersection() # Common elements
difference()   # Elements in A not in B
'''
# Create a set
s={1,2,3,4}
print(s)

# Create a set and remove duplicates
a=[1,2,2,3,4,4,5]
b=set(a)
print(b)

# Add and Remove elements
s={1,2,3}
s.add(4)
s.remove(2)
print(s)

# Find common elements between two sets
A={1,2,3,4}
B={3,4,5,6}
print(A.intersection(B))

# Find elements present in Set A but not in Set B
A={10,20,30,40}
B={30,40,50}
print(A.difference(B))

# Check if Set is Subset
A={1,2,3}
B={1,2,3,4,5}
print(A.issubset(B))

# Check if value exists
s={5,10,15,20}
print(10 in s)

# Add an element
a={1,2,3,4,5}
b=a.add(6)
print(a)

# Remove an element
a={1,2,3,4,5}
b=a.remove(3)
print(a)

'''
Find union of:
A={1,2,3}
B={3,4,5}
'''
A ={1,2,3}
B ={3,4,5}
print(A.union(B))

'''
Find intersection of:
A = {1,2,3,4}
B = {3,4,5,6}
'''
A={1,2,3,4}
B={3,4,5,6}
print(A.intersection(B))

'''
find difference A - B
A = {10,20,30,40}
B = {30,40,50}
'''
A={10,20,30,40}
B={30,40,50}
print(A.difference(B))

'''
Check whether these sets are disjoint:
A = {1,5,9}
B = {2,4,6}
'''
A={1,5,9}
B={2,4,6}
if not A.intersection(B):
  print("Yes Disjoint")
else:
  print("No")
                  #OR
A={1,5,9}
B={2,4,6}
if A.disjoint(B):
    print("Yes Disjoint")
else:
    print("No")

# Convert string "banana" to a set.
a=set("banana")
print(a)

'''
Check if A is a subset of B
A = {1,2}
B = {1,2,3,4}
'''
A = {1,2}
B = {1,2,3,4}
print(A.issubset(B))

'''
Find symmetric difference
A = {1,2,3}
B = {3,4,5}
'''
A = {1,2,3}
B = {3,4,5}
print(A.symmetric_difference(B))

'''
Remove an element safely (without error) from:
s = {1,2,3}
remove 5'''
s={1,2,3}
a=s.discard(5)
print(s)

'''
Find common items between 3 sets:
A = {1,2,3,4}
B = {2,3,5}
C = {2,3,6}'''
A = {1,2,3,4}
B = {2,3,5}
C = {2,3,6}
print(A.intersection(B).intersection(C))

'''
Given a list:
nums = [1,1,2,3,4,4,5,6,6]
Find number of unique elements using set.'''
nums = [1,1,2,3,4,4,5,6,6]
s=set(nums)
count=0
for i in s:
  count+=1
print("Set is: ",s,"\n""Count is: ",count)

# Write logic to check if two lists contain same elements ignoring order.
# Example: [1,2,3] and [3,2,1]
a=[1,2,3]
b=[4,2,1]
a.sort()
b.sort()
if len(a)==len(b):
  if a==b:
    print("same")
  else:
    print("No")
  
# Given a sentence "hello world hello python world", print only unique words.
a="hello world hello python world"
b=a.split()
print(set(b))

# Check if two sentences are made with the same set of words (order can differ
S1="I love coding"
S2="coding I love"
s1=S1.lower().split()
s2=S2.lower().split()
if set(s1)==set(s2):
  print("True")
else:
  print("False")
  
'''
A = {1,2,3,4,5}
B = {3,4,5,6,7}
Find:
✔ elements only in A
✔ elements only in B
✔ elements in both
✔ elements in none if universal = {1..7}'''
A = {1,2,3,4,5}
B = {3,4,5,6,7}
U = {1,2,3,4,5,6,7}
print(A-B)
print(B-A)
print(A.intersection(B))
print(U-(A.union(B)))

# Convert list → set and check if length reduced (means duplicates existed or not).
a=[1,2,3,4,4]
b=set(a)
if len(b)==len(a):
  print("Duplicates not exist")
else:
  print("Exists")
  
# check whether set A is a proper subset of B
a={1,2}
b={1,2,3}
print(a<b)

# Remove duplicates from a list
a=[1,2,2,3,4,4,5]
result=set(a)
print(result)

# Check if a set is empty
s = set()
if not s:
    print("Set is empty")
else:
    print("Set is not empty")