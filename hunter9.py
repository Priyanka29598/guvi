np=int(input())
ap=list(map(int,input().split()))
t=max(ap)
c,d=0,0
for i in range(0,len(ap)-1):
  for j in range(i+1,len(ap)):
    if abs(ap[i]+ap[j])<t:
      c,d=ap[i],ap[j]
      t=abs(c+d)
print(c,d)
