a=(2,-1,5,-3,6,-9,4-6)
b=list(a)
for i in range(len(b)):
  if b[i]<0:
    b[i]=0
print(b)