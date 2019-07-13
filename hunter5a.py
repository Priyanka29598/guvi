ap=int(input())
bp=list(map(int,input().split()))
c=[]
for i in bp:
  if(bp.count(i)<2):
    if i not in c:
      c.append(i)
print(*c)
