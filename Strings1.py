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
