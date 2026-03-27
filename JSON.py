'''
Python JSON – Short Notes
🔹 What is JSON?
JSON = JavaScript Object Notation
Used for storing & exchanging data
It is text format (easy to read & write)
🔹 JSON in Python
Python has a built-in module:
👉 json
Used to convert data between JSON ↔ Python
🔹 Convert JSON → Python
Method: json.loads()
Converts JSON string → Python dictionary
import json
x='{"name":"John","age":30}'
y=json.loads(x)

✔ Output → Python dict

🔹 Convert Python → JSON
Method: json.dumps()
Converts Python object → JSON string
import json
x={"name":"John","age":30}
y=json.dumps(x)

✔ Output → JSON string

🔹 JSON Syntax Rules
Data in key : value pairs
Keys must be in double quotes
{} → objects
[] → arrays
🔹 Supported Python Types → JSON
dict → object
list/tuple → array
str → string
int/float → number
True/False → true/false
None → null
🔹 Extra (Formatting)
Use indent in json.dumps() for readability
json.dumps(x,indent=4)
'''

# Convert JSON string to Python dictionary
import json
x='{"name":"John","age":25,"city":"New York"}'
y=json.loads(x)
print(y)

# Convert Python dictionary to JSON string
import json
x={"name":"Alice","age":22,"city":"London"}
y=json.dumps(x)
print(y)

# Pretty print JSON with indentation
import json
x={"name":"Bob","age":30,"city":"Paris"}
y=json.dumps(x,indent=4)
print(y)

# Convert Python list to JSON array
import json
x=["apple","banana","cherry"]
y=json.dumps(x)
print(y)

# Access values from JSON after loading
import json
x='{"name":"Tom","age":28,"city":"Berlin"}'
y=json.loads(x)
print(y["name"],y["age"])

# Write JSON data to a file
import json
x={"name":"Sam","age":20}
with open("data.json","w") as f:
    json.dump(x,f)
    
# Read JSON data from a file
import json
with open("data.json","r") as f:
    x=json.load(f)
print(x)

# Convert Python object with different data types to JSON
import json
x={"name":"Lily","age":21,"isStudent":True,"marks":None}
y=json.dumps(x)
print(y)
