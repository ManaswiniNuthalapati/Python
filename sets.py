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


