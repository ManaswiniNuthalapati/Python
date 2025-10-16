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

# Print Two Strings Using One Print Statement
a="Hello"
b="World"
c=({},{}).format(a,b)
print(c)

# Check if the word "data" exists in "dataanalytics".
s1="dataanalytics"
s2="data"
print(s2 in s1)

# Join "machine" and "learning" to form "machinelearning"
s1="machine"
s2="learning"
print(s1+ " "+s2)

# Print "Welcome to AI course" using concatenation of multiple strings.
s1="Welcome"
s2="to"
s3="AI Course"
s4=s1+" "+s2+" "+s3
print(s4)

# Find the position of "learn" in "learnpythonlearn".
s1="learnpythonlearn"
s2="learn"
print(s1.index(s2))

# Find the last occurrence of "learn" using index() with a start parameter.
s1="learnpythonlearn"
s2="learn"
print(s1.rindex(s2))

# Find all the occurrences of "on" in "pythonpythonpython"
s1="pythonpythonpython"
s2="on"
first=s1.find(s2)
second=s1.find(s2,first+1)
last=s1.rindex(s2)
print("1st Occurance:",first)
print("2nd Occurance:",second)
print("3rd Occurance:",last)

# Verify if "Coding in Python" starts with "Coding" and ends with "Python"
s1="Coding with Python"
print(s1.startswith("Coding"))
print(s1.endswith("Python"))

# Split the string "AI ML DS" into words.
s1="AI ML DS"
s2=s1.split()
print(s2)

# Split "apple,banana,cherry" using , as separator.
s1="apple,banana,cherry"
s2=s1.split(",")
print(s2)

#Join the list ["I", "love", "coding"] into one sentence separated by spaces.
s1=["I", "love", "coding"]
s2=" ".join(s1)
print(s2)

# Remove "#" characters from both ends,right and left of "###Geeks###" using strip()
s1="###Geeks###"
print(s1.strip("#"))
print(s1.rstrip("#"))
print(s1.lstrip("#"))

# Search for "python" and "java" in "python programming" using find() and print their index values.
s1="python programming"
s2=s1.find("python")
print(s2)
s3=s1.find("java")
print(s3)

# Given a list of names, sort them in ascending order using string comparison.
s1=["Manu","Ashritha","Vinaya","Taruni"]
for i in range(len(s1)):
  for j in range(len(s1)):
    if s1[i]<s1[j]:
      s1[i],s1[j]=s1[j],s1[i]
print(s1)

