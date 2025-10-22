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
