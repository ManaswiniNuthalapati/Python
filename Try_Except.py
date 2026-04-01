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
#  1. Handle Division by Zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b 
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

#  2. Handle Invalid Input
try:
    num = int(input("Enter a number: "))  
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer")

#  3. Multiple Exceptions
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))  
    print("Result:", a / b)
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")

#  4. Using else Block
try:
    x = int(input("Enter number: "))
    y = int(input("Enter divisor: "))  
    result = x / y
except Exception:
    print("Error occurred")
else:
    print("Division successful:", result)  # runs if no error

#  5. Using finally Block
try:
    num = int(input("Enter a number: "))
    print("Number is:", num)
except ValueError:
    print("Invalid input")
finally:
    print("This block always runs")  # always executes

#  6. Index Error Handling
try:
    my_list = [10, 20, 30]
    index = int(input("Enter index: ")) 
    print("Element:", my_list[index])  
except IndexError:
    print("Error: Index out of range")
except ValueError:
    print("Error: Enter valid index number")

