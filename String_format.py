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
#  1. Print name and age using f-string
name = "Sai"
age = 20
print(f"My name is {name} and I am {age} years old")

#  2. Print price with 2 decimal places
price = 123.4567
print(f"Price: {price:.2f}")

#  3. Print total cost (price + tax)
price = 100
tax = 0.18
print(f"Total cost: {price + price * tax}")

#  4. Convert name to uppercase
name = "vinaya"
print(f"Hello {name.upper()}")

#  5. Print even or odd
num = 7
print(f"The number is {'Even' if num % 2 == 0 else 'Odd'}")

#  6. Print name and marks
name = "Sai"
marks = 85
print("Name: {}, Marks: {}".format(name, marks))

#  7. Swap values
name = "Sai"
age = 20
print("Age: {1}, Name: {0}".format(name, age))

#  8. Use named placeholders
print("Name: {n}, Age: {a}".format(n="Sai", a=20))

#  9. Format number with commas
num = 1000000
print(f"Number: {num:,}")

#  10. Align text
name = "Sai"
print(f"{name:<10}")
print(f"{name:>10}")
print(f"{name:^10}")

#  11. Convert to percentage
value = 0.85
print(f"Success rate: {value:.2%}")

# Print number with leading zeros (5 digits)
num = 42
print(f"Number: {num:05}")