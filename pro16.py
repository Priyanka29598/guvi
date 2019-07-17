ap,bp=map(int,input().split())
c=list(map(int,input().split()))[:ap]
d=0
for i in range(ap):
  for j in range(ap):
    if(j>i):
      if(c[i]+c[j]==bp):
        d+=1
if(d>0):
  print("yes")
else:
  print("no")
