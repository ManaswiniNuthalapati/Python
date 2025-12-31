# DICTIONARIES
'''
Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type
and can be duplicated, whereas keys can't be repeated and must be immutable.
    Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
    Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
    Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
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

