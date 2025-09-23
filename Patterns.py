# Single line of stars
# * * * * * 
n=5
for i in range(1,n+1):
    print("*",end=' ')

# Vertical Line of stars
# *
# *
# *
n=5
for i in range(1,n+1):
    print("*")
    
'''
Right-angled triangle of stars
*
**
***
****
*****
'''
n=5
for i in range(1,n+1):
    print("*",end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()
    
'''
Right-angled triangle of numbers
1
12
123
1234
12345
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
'''
Right-angled triangle with repeated numbers
1
22
333
4444
55555
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
'''
Square Pattern
****
****
****
****
'''
n=5
for i in range(1,n+1):
    for j in range(1,n):
        print("*",end=" ")
    print()

