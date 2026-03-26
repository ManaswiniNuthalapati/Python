'''
Python Math
🔹 1. Built-in Math Functions

Python already gives some math functions (no need to import anything).

✅ min() → smallest value
min(5, 10, 25)  # 5
✅ max() → largest value
max(5, 10, 25)  # 25
✅ abs() → positive value
abs(-7.25)  # 7.25
✅ pow(x, y) → power (x^y)
pow(4, 3)  # 64

👉 These functions help perform basic math directly.

🔹 2. Math Module (Important ⭐)

Python has a special module called math for advanced calculations.

👉 Import it:
import math

👉 After importing, you can use many functions.

🔹 3. Important Math Functions
✅ Square root
math.sqrt(16)  # 4
✅ Round up (ceil)
math.ceil(4.2)  # 5
✅ Round down (floor)
math.floor(4.9)  # 4
✅ Power
math.pow(2, 3)  # 8.0
✅ Factorial
math.factorial(5)  # 120

👉 These functions are part of math module.

🔹 4. Math Constants
✅ PI (π)
math.pi  # 3.14159
✅ Euler’s number (e)
math.e  # 2.718

👉 Used in formulas and calculations.

🔹 5. Trigonometry Functions

(All use radians)

math.sin(x)
math.cos(x)
math.tan(x)

Convert degrees ↔ radians:

math.degrees(x)
math.radians(x)
🔹 6. Log & Exponential
✅ Logarithm
math.log(10)
✅ Exponential
math.exp(2)

👉 Used in advanced math & data science.

🔹 7. Key Points (Very Important ⚡)
Python has built-in functions (min, max, abs, pow)
For advanced math → use math module

Must write:

import math

Functions are used as:

math.function_name()
✅ Quick Summary (Revision)
min(), max() → smallest/largest
abs() → positive value
pow() → power
math.sqrt() → square root
math.pi → constant
math.log() → logarithm
'''

# Findminandmaxofnumbersinlist
nums=[12,45,7,89,23]
print("Min:",min(nums))
print("Max:",max(nums))

# Findabsolutevaluesofgivennumbers
print(abs(-25))
print(abs(13))
print(abs(-7.5))

# Calculatepowerofnumbersusingpow
print(pow(3,4))
print(pow(5,3))

# Findsquarerootofgivennumbers
import math
print(math.sqrt(49))
print(math.sqrt(144))

#Findceilandfloorofnumber
x=6.7
print("Ceil:",math.ceil(x))
print("Floor:",math.floor(x))

#Calculateareaofcircleusingradius
r=7
area=math.pi*r*r
print("Area:",area)

# Findfactorialofnumbers
print(math.factorial(5))
print(math.factorial(7))

#Findgcdofgivennumbers
print(math.gcd(24,36))
print(math.gcd(18,48))

#Findlogarithmvalues
print(math.log(10))
print(math.log10(100))

#Checkifnumberisperfectsquare
n=49
if math.sqrt(n).is_integer():
    print("PerfectSquare")
else:
    print("NotPerfectSquare")