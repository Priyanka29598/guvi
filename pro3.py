mt,pt=input().split()
r1=abs(len(pt)-len(mt))
for k in range(len(mt)):
  if(len(pt)==1 and pt[k] in mt):
    break
  if(mt[k]!=pt[k]):
    r1=r1+1
print(r1)
