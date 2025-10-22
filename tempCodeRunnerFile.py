n="banana"
freq=""
for ch in n:
  if ch not in freq:
    print(ch,"-",n.count(ch))
    freq+=ch
