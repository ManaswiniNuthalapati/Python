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
    
'''
Reverse Right-angled Triangle
****
***
**
*
'''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()

'''
Reverse Right-angled Triangle with numbers
55555
4444
333
22
1
'''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(n-i+1,end=" ")
    print()
    
'''
Reverse Number Triangle
1234
123
12
1
'''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=" ")
    print()
    
'''
Right-angled triangle with numbers starting from 1
1
2 3
4 5 6
7 8 9 10
'''
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()  
    
'''
Right-aligned triangle of stars
   *
  **
 ***
 '''  
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()  
    
'''
right aligned triangle with numbers
   1
  22
 333
''' 
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
    
''' 
Right-aligned traingle with continous numbers
   1
  12
 123
1234
'''
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    print()
    
'''
Pyramid of stars

   *
  ***
 *****
 '''
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
        
'''
Inverted pyramid
*****
 ***
  *
  '''
n=5
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i+1):
        print("*",end=" ")
    print()
    
'''
Pyramid for numbers
1 1 1 1 1 
  2 2 2 2 
   3 3 3 
    4 4 
     5 
'''
n=5
for i in range(1,n+1):
  for j in range(i):
    print(" ",end="")
  for k in range(n-i+1):
    print(i,end="")
    
'''
Reverse triangle with continous numbers
1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1 
'''
n=5
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i+1):
        print(k+1,end="")
    print()
    
'''
Diamond Pattern
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end="")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end=" ")
    print()
    
'''
Pyramid of odd numbers(low-->up)
    *
   ***
  *****
 *******
*********
'''
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
    
'''
Pyramid of odd numbers(up-->low)
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
n=5
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
    
'''
Diamond Full Pattern
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
'''
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print() 
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()      
    
'''
HourGlass Pattern
*****
 ***
  *
 ***
*****
'''
n=3
for i in range(n,1,-1):
  for j in range(n-i):
    print(" ",end=" ")
  for k in range(2*i-1):
    print("*",end=" ")
  print()
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end=" ")
  for k in range(2*i-1):
    print("*",end=" ")
  print() 
    
'''
Alphabet triangle
A
AB
ABC
'''
n=5
for i in range(1,n+1):
  for j in range(i):
    print(chr(65+j),end=" ")
  print()
  
'''
Reverse alphabet triangle
ABC
AB
A
'''
n=5
for i in range(n+1,0,-1):
  for j in range(i):
    print(chr(65+j),end=" ")
  print()
  
'''
Hollow Square

*****
*   *
*   *
*   *
*****
'''
n=5
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==1 or i==n or j==1  or j==n:
      print("*",end="")
    else:
      print(" ",end="")
  print()
 
 
'''
X shape Pattern
*       * 
  *   *   
    *     
  *   *   
*       * 

'''
n=5
for i in range(n):
  for j in range(n):
    if i==j or i+j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

'''
Hollow Right-angled Triangle
* 
* * 
*   * 
*     * 
* * * * * 
'''
n=5
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==n or j==1 or j==i:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  
'''
Rectangle of Stars
*****
*****
*****
'''
n=int(input())
for i in range(1,n-1):
  for j in range(1,n+1):
    print("*",end=" ")
  print()
  
'''
Half Diamond (Stars Increasing → Decreasing)
*
**
***
****
***
**
*
'''
n=int(input())
for i in range(1,n+1):
  for j in range(i):
    print("*",end=" ")
  print()
for i in range(1,n+1):
  for j in range(n-i):
    print("*",end=" ")
  print()
  
'''
Pascal’s Triangle
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
n=int(input())
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end="")
  num=1
  for k in range(1,i+1):
    print(num,end=" ")
    num=num*(i-k)//k
    
  print()
  
'''
Number Pyramid (Palindrome)
   1
  121
 12321
1234321
'''
n=int(input())
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end=" ")
  for k in range(1,i+1):
    print(k,end=" ")
  for l in range(i-1,0,-1):
    print(l,end=" ")
  print()
  
'''
Butterfly Pattern

*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
'''
n=int(input())
for i in range(1,n+1):
  print("*"*i,end="")
  print(" "*(2*(n-i)),end="")
  print("*"*i)
  
for i in range(n,0,-1):
  print("*"*i,end="")
  print(" "*(2*(n-i)),end="")
  print("*"*i)
  

  
