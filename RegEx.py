'''
# Python RegEx (Regular Expressions)

## 1. What is RegEx?
A Regular Expression (RegEx) is a sequence of characters used to form a search pattern.
It is Used for:
  * Searching text
  * Matching patterns
  * Replacing text
  * Data validation
---

## 2. Python RegEx Module
* Python has a built-in module called `re`.
```python
import re
```
* It is used to:
  * Search
  * Match
  * Split
  * Replace strings using patterns 
---

## 3. Basic Example
```python
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```
* Checks if string starts with `"The"` and ends with `"Spain"`
---

## 4. Important RegEx Functions
| Function    | Description         |
| ----------- | ------------------- |
| `findall()` | Returns all matches |
| `search()`  | Returns first match |
| `split()`   | Splits string       |
| `sub()`     | Replaces matches    |

 Example:
```python
re.findall("ai", txt)
```
Returns all occurrences of `"ai"`
---

##  5. Match Object
* Returned when a match is found
* If no match → returns `None`

### Useful methods:
```python
x.span()    # start & end index
x.string    # original string
x.group()   # matched text
```
---

## 6. Metacharacters (Special Symbols)

| Symbol | Meaning           |    |
| ------ | ----------------- | -- |
| `.`    | Any character     |    |
| `^`    | Starts with       |    |
| `$`    | Ends with         |    |
| `*`    | 0 or more         |    |
| `+`    | 1 or more         |    |
| `?`    | 0 or 1            |    |
| `{}`   | Exact number      |    |
| `[]`   | Set of characters |    |
| `      | `                 | OR |
---

##  7. Sets `[ ]`
Used to match a group of characters:

| Pattern  | Meaning           |
| -------- | ----------------- |
| `[abc]`  | a or b or c       |
| `[a-z]`  | lowercase letters |
| `[0-9]`  | digits            |
| `[^abc]` | NOT a, b, c       |
---

## 🔹 8. Special Sequences (`\`)

| Symbol | Meaning         |
| ------ | --------------- |
| `\d`   | digits (0–9)    |
| `\D`   | non-digits      |
| `\s`   | whitespace      |
| `\S`   | non-whitespace  |
| `\w`   | word characters |
| `\W`   | non-word        |
| `\b`   | word boundary   |

---

##  9. Example Programs
### ✔ Find all digits
```python
import re
text = "My number is 12345"
print(re.findall("\d+", text))
```

### ✔ Replace text
```python
import re
txt = "Hello World"
print(re.sub("World", "Python", txt))
```
---

##  10. Key Points
* Use **`r""` (raw string)** for regex patterns
* `search()` → anywhere in string
* `match()` → only at beginning
* `findall()` → list of matches
* `sub()` → replace text
---

## Short Summary
* RegEx = pattern matching tool
* Use `re` module
* Helps in search, validation, extraction
---
'''

## 
# 1. Check if string starts with "Hello"
import re
text="Hello world"
if re.search(r"^Hello", text):
    print("Yes")
else:
    print("No")

## 2. Find all digits in a string
import re
text="My number is 123 and 456"
result=re.findall(r"\d+", text)
print(result)

##  3. Count number of vowels
import re
text="education"
vowels=re.findall(r"[aeiou]", text)
print(len(vowels))

##  4. Replace spaces with hyphen
import re
text = "Python is easy"
print(re.sub(r"\s", "-", text))

