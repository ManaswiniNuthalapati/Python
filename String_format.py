'''
#  Python String Formatting 

##  What is String Formatting?
* Used to **insert values into a string**.
* Helps combine **text + variables** easily.

## 1. F-Strings 
* Introduced in Python 3.6
* Preferred method now 

###  Syntax:
name = "Sai"
print(f"My name is {name}")

###  Key Points:
* Use `f` before string
* Use `{}` as placeholders

##  2. Placeholders `{}`
* Used to insert values inside string

price = 50
print(f"Price is {price}")

* Can also format values:
price = 59
print(f"Price is {price:.2f}")  # 2 decimal places

 `.2f` → fixed 2 decimal points 

##  3. Perform Operations inside {}
print(f"Result: {10 * 5}")

price = 50
tax = 0.2
print(f"Total: {price + price*tax}")

✔ You can do calculations directly inside `{}` 

##  4. Use Functions inside {}
name = "sai"
print(f"Hello {name.upper()}")

✔ Functions also work inside placeholders 

##  5. Conditional (if-else) inside {}
price = 60
print(f"It is {'Expensive' if price > 50 else 'Cheap'}")

##  6. format() Method
* Used before f-strings
###  Syntax:
txt = "My age is {}"
print(txt.format(20))

###  Multiple values:
print("I am {} and age is {}".format("Sai", 20))

###  Indexing:
print("Age: {1}, Name: {0}".format("Sai", 20))

Uses `{}` placeholders 

##  7. Named Placeholders
print("Name: {n}, Age: {a}".format(n="Sai", a=20))

##  8. Formatting Types
Common formats:
* `.2f` → float with 2 decimals
* `,` → comma separator
* `>` `<` `^` → alignment
* `%` → percentage 

## Key Points 

* **f-strings → fastest & easiest**
* `{}` → placeholders
* `.2f` → decimal formatting
* `format()` → old method
* Can use **operations, functions, conditions**

'''
