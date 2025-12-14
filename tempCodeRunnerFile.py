a=(2,5,4,6,2,1,8,9,1)
b=()
for i in a:
  if a.count(i)>1 and i not in b:
    b=b+(i,)
print(b)