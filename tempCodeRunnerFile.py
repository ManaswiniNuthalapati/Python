# Print elements from index 2 to 5 in a tuple.
a=(1,2,3,4,5)
for i in range(2,5):
  print(a[i])

# Print all elements except the first and last one.
a=(1,2,3,4,5)
for i in range(1,len(a)-1):
  print(a[i])
  
# Print every alternate element from a tuple.
a=(1,2,3,4,5)
for i in range(len(a)):
  if i%2==0:
    print(a[i])
    
# Print the tuple in reverse order using slicing.
a=(1,2,3,4,5)
print(a[::-1])

# Access the third element from the end of a tuple.
a=(1,2,3,4,5)
print(a[-3])