''' 
Strings ---> A sequence of Characters used 
to store text data --->Letters, Numbers, special Characters,etc..

Characters represented by integer values --->ASCII Values
A to Z ---> 65 to 90
a to z ---> 97 to 122

ord()--> takes a character and returns integer as output
chr()--> reverse

Strings-- Immutable 

Accessing characters in a string ---> through indexing
'''

# Print the string
str1="Hello"
print(str1)

# Print Each Character on a new line
str="Code"
print(str[0])
print(str[1])
print(str[2])
print(str[3])

# Print Length of String
str2="Hello"
print(len(str2))

# Print First and Last Character
str="Hello"
print(str[0],end=" ")
print(str[-1],end=" ")

# Print Middle Character (if length is odd)
str="Apple"
length=len(str)//2
print(str[length])

# Check if String is Empty
s=input()
if s:
  print("Not empty")
else:
  print("Empty")
  
# Count Spaces in a Sentence
str="I am FIme"
count=0
for ch in str:
  if ch==' ':
    count+=1
print(count)
  
# Type of a String
s="Chatgpt"
print(type(s))

# print a string for 5 times
s=input()
print((s+"\n")*5)

# Print a string with quotes inside
n='"Hello"'
print("She said, {}".format(n))

# Use Escape Sequence for a New Line
n="Hello \nWorld"
print(n)

# Use Escape Sequence for a Tab
n="Hello \tWorld"
print(n)

# Print String with Single and Double Quotes
n="It's a" ' "sunny" day' 
print(n)

# Display Floating-Point Value with Two Decimals
price=45.6789
print(format(price,".2f"))
