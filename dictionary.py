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

