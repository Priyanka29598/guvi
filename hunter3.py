Xp=int(input())
Yp=list(map(int,input().split()))[:Xp]
t=[]
for i in range(0,Xp):
    if(Yp[i]==i):
        t.append(Yp[i])
if(len(t)==0):
    print("-1")
else:
    print(*t,end="")
