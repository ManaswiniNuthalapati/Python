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