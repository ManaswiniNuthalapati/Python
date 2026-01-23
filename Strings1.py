# Remove duplicate characters
s = "programming"
res = ""
for i in s:
    if i not in res:
        res += i
print(res)

'''
Username Validation
Input a username and check if it only contains lowercase letters and digits.
Condition: Length must be between 5 and 15.
'''
s=input()
if 5<=len(s)<=15:
    for ch in s:
        if (ch.islower() or ch.isdigit()):
            print(True)
            break
        else:
            print(False)
else:
    print(False)
    
'''
Email Domain Extractor
Given an email like "john.doe@gmail.com", extract "gmail.com".
'''
s=input()
index=s.index("@")
s1=s[index+1:]
print(s1)

'''
Palindrome Checker
Check whether the given word or sentence is a palindrome.
'''
s=input()
rev=""
for i in s:
    rev=i+rev
if s==rev:
    print(True)
else:
    print(False)
    
'''
Character Frequency Counter
Input: "banana"
Output: {'b':1, 'a':3, 'n':2} (you can print formatted output).
'''
s="banana"
freq={}
for ch in s:
  if ch in freq:
    freq[ch]+=1
  else:
    freq[ch]=1
print(freq)

'''
Check Substring
Input two strings s1 and s2; check if s2 exists inside s1.
'''
s1="Banana"
s2="an"
if s2 in s1:
  print(True)
else:
  print(False)
  
'''Longest Word in a Sentence
Input: "Python is amazing"
Output: "amazing"
'''
n="Python is amazing"
a=n.split()
longest=""
for ch in a:
  if len(ch)>len(longest):
    longest=ch
print(longest)

'''
Count Each Character Frequency
Input: "banana"
Output: b:1, a:3, n:2
'''
n="banana"
freq=""
for ch in n:
  if ch not in freq:
    print(ch,":",n.count(ch),end=",")
    freq+=ch

'''
Remove Duplicate Characters
Input: "programming"
Output: "progamin"
'''
n="programming"
dup=""
for ch in n:
  if ch not in dup:
    print(ch,end="")
    dup+=ch
    
'''
Check if Two Strings Are Anagrams
Input: "listen", "silent"
Output: Yes, anagrams
'''
a="listen"
b="silent"
c=a.lower()
d=b.lower()
if len(c)!=len(d):
  print("Not Anagram")
else:
  for ch in c:
    if c.count(ch)!=d.count(ch):
      print("Not Anagram")
      break
  else:
    print("Anagram")
    
'''
Shift Letters by 1 (Caesar Cipher Style)
Input: "abc"
Output: "bcd"
'''
n="abc"
for ch in n:
  p=ord(ch)+1
  print(chr(p),end="")
  
'''
Extract Numbers from a String
Input: "abc123xyz45"
Output: "12345"
'''
n="abc123xyz45"
for ch in n:
  if ch.isdigit():
    print(ch,end="")
    
'''
Check if String Contains Only Unique Characters
Input: "python"
Output: Yes
Input: "programming"
Output: No
'''
n="python"
count=""
for ch in n:
  if ch not in count:
    count+=ch
    unique=True
  else:
    unique=False
print(unique)

# Print Alphabets
p="a"
q="z"
for ch in range(ord(p),ord(q)+1):
  print(chr(ch),end=" ")
  
# Find All Capital Letters
s="PyThOnIsFuN"
letters=[]
for ch in s:
    if 'A'<=ch<='Z': 
        letters.append(ch)
print(letters)

# Count the Number of Sentences in a Paragraph
s="Python is fun. I love coding! Do you?"
a=".!?"
count=0
for ch in s:
    if ch in a:
        count+=1
print(count)

# Leetcode 434 count  no of segments
class Solution:
    def countSegments(self, s: str) -> int:
        res=s.split()
        return len(res)