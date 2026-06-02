# DICTIONARIES
'''
Written inside { }
Data stored as key : value
Keys must be unique
Keys must be immutable (string, number, tuple)
Values can be any data type
Dictionaries are mutable (you can change them)
They are unordered (Python 3.7+ maintains insertion order)
'''

# Creation Of Dictionary
'''
created by placing a sequence of elements within curly {} braces, separated by a 'comma'.
'''
d1={1:'Geeks', 2:'For', 3:'Geeks'}
print(d1)
# create dictionary using dict() constructor
d2=dict(a ="Geeks", b ="for", c ="Geeks")
print(d2)

#Accessing Dictionary Items
'''
We can access a value from a dictionary by using the key within square brackets or get() method.
'''
d={"name":"John",1:"Python",(1, 2):[1,2,4]}
# Access using key
print(d["name"])
# Access using get()
print(d.get("name"))

# Adding and Updating
d["city"] = "Hyderabad"   # add
d["name"] = "Dict"        # update

# Removing Items
d.pop("city")       # removes specific key
d.popitem()         # removes last inserted key-value pair
del d["name"]       # deletes a key using del keyword
d.clear()           # removes all items (dictionary becomes empty)
del d               # deletes the entire dictionary from memory

# Important Dictionary Methods
'''
d.keys()      # returns all keys
d.values()    # returns all values
d.items()     # returns key-value pairs
'''

# Create a dictionary & access values
a={"name":"Manaswini", "age":19, "city":"Hyderabad"}
print(a)
print(a["name"])


# Add / Update / Delete keys
a={"name":"Manaswini", "age":19, "city":"Hyderabad"}
a["Branch"]="DS"
print(a)
a["name"]="Manaswini Nuthalapati"
print(a)

# Check if key exists
a={"name":"Manaswini", "age":19, "city":"Hyderabad"}
print("name" in a)

# Count frequency of elements in a list using dictionary
a=["name","Manaswini", "age","age", "city","Hyderabad"]
count={}
for i in a:
  if i in count:
    count[i]+=1
  else:
    count[i]=1
print(count)

# Convert two lists → dictionary
a=["name","Manu","age",19]
b=["manu","name",19,"age"]
print(dict(zip(a,b)))

# Get only keys / values / items
a={"name":"Manaswini", "age":19, "city":"Hyderabad"}
print(a.keys())
print(a.values())
print(a.items())

#Find length of dictionary
a={"name":"Manaswini", "age":19, "city":"Hyderabad"}
print(len(a))

# Copy dictionary
a={"name":"Manaswini", "age":19}
b=a.copy()
print(b)


# Clear dictionary
a={"name":"Manaswini", "age":19}
a.clear()

# Find the maximum & minimum value in a dictionary
a={"id":1, "age":19, "marks":96}
print(min(a.values()))
print(max(a.values()))

# Sort dictionary
#by keys
#by values
a={"name":"Manaswini", "age":"19", "city":"Hyderabad"}
print(sorted(a.keys()))
print(sorted(a.values()))


# Merge two dictionaries
a={"name":"Manaswini", "age":"19", "city":"Hyderabad"}
b={"city":"Warangal"}
c={**a,**b}
print(c)

# Check if two dictionaries are equal
a={"name":"Manaswini", "age":"19", "city":"Hyderabad"}
b={"name":"vinaya", "age":"19", "city":"Warangal"}
print(a==b)

#Get value with get() safely
a={"name":"Manaswini", "age":"19", "city":"Hyderabad"}
print(a.get("name"))

# Create dictionary using dict comprehension
a=dict(name="Manaswini", age="19", city="Hyderabad")
print(a)

# Reverse keys & values (if unique)
a={"name":"Manaswini", "age":"19", "city":"Hyderabad"}
rev={}
for key,value in a.items():
  rev[value]=key
print(rev)

# Word Frequency Count
a="I love coding and I love Python"
freq={}
for i in a.split():
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
print(freq)

# Character Frequency Count in a String
a="banana"
freq={}
for i in a:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
print(freq)

# Remove Duplicate Values in Dictionary
d={"a":1,"b":2,"c":1,"d":3}
res={}
d_1=set()
for keys,values in d.items():
  if values not in d_1:
    res[keys]=values
    d_1.add(values)
print(res)