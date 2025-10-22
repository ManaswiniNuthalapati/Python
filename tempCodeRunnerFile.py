n="Python is amazing"
a=n.split()
longest=""
for ch in a:
  if len(ch)>len(longest):
    longest=ch
print(longest)
