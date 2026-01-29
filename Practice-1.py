'''
Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
res=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        res.append(str(i))
print(",".join(res))

'''
Question: Write a program which can compute the factorial of a given numbers. The results 
should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
'''
n=8
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

'''
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included).and then the program should print the dictionary. 
Suppose the following input is supplied to the 
program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
n=8
res={}
for key in range(1,n+1):
  res[key]=key*key
print(res)
  
'''
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number. Suppose the following input is supplied to the
program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
'''
n="34,67,55,33,12,98"
n_1=n.split(",")
print(list(n_1))
print(tuple(n_1))

'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters
in the sentence capitalized. Suppose the following input is supplied to the 
program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
'''
s="Hello world Practice makes perfect"
s=s.upper()
print(s)

'''
Square Pattern
****
****
****
****
'''
n=4
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()
