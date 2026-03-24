'''Python datetime Module

🔹 1. Introduction
Python does not have a built-in date type.
To work with date and time, we use the datetime module.
import datetime

🔹 2. Getting Current Date & Time
x = datetime.datetime.now()
print(x)
Returns current:
Year, Month, Day
Hour, Minute, Second, Microsecond

🔹 3. Accessing Date Components
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)

🔹 4. Creating a Date Object
x = datetime.datetime(2020, 5, 17)
print(x)
Format: datetime(year, month, day, hour, minute, second)
Time is optional (default = 00:00:00)

🔹 5. Important Classes in datetime
Class	Description
date	Stores only date (year, month, day)
time	Stores only time (hour, minute, second)
datetime	Stores both date and time
timedelta	Represents difference between dates

🔹 6. Using date Class
from datetime import date
d = date(2026, 3, 23)
print(d)

🔹 7. Formatting Date — strftime()
Converts date/time → string
x = datetime.datetime.now()
print(x.strftime("%A"))

🔑 Common Format Codes
Code	Meaning
%Y	     Year (2026)
%m	     Month (01–12)
%d	     Day (01–31)
%A	     Weekday (Monday)
%B	     Month name (March)
%H	     Hour (00–23)
%M	     Minute
%S	     Second

📌 Example
x = datetime.datetime.now()
print(x.strftime("%d-%m-%Y"))   # 23-03-2026
print(x.strftime("%A"))         # Monday
print(x.strftime("%B"))         # March
'''
# Print current date and time
import datetime
x=datetime.datetime.now()
print(x)

# Extract and print only year
import datetime
x=datetime.datetime.now()
print(x.year)