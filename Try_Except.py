'''

##  Python Try...Except

###  What is it?
* Used for **error handling (exceptions)** in Python.
* Prevents program from crashing when an error occurs.

###  Basic Structure
try:
    # code that may cause error
except:
    # code to handle error

###  Keywords 
#### 1. **try**
* Tests a block of code for errors. 
#### 2. **except**
* Executes when an error occurs.
* You can handle specific errors:

try:
    print(x)
except NameError:
    print("x not defined")

#### 3. **else**
* Runs if **no error occurs**.

try:
    print("Hello")
except:
    print("Error")
else:
    print("No error")

#### 4. **finally**
* Runs **always**, whether error occurs or not. ([W3Schools][1])
* Used for cleanup (closing files, etc.)

try:
    print(x)
except:
    print("Error")
finally:
    print("Done")

###  Multiple Exceptions
* You can handle different errors separately:
try:
    print(x)
except NameError:
    print("Name Error")
except:
    print("Other Error")

###  Raise Keyword
* Used to **manually create an exception**:

x = -1
if x < 0:
    raise Exception("No negative numbers")

##  Key Points

* `try` → check code
* `except` → handle error
* `else` → runs if no error
* `finally` → always runs
* Prevents program crash

'''
