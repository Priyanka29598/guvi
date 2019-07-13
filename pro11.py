ip=int(input())
cp=0
l=[]
for i in range(1,i+1):
  l.append(i)
for i in range(len(l)):
  for i in range(i+1,len(l)):
    cp+=1
print(cp)
