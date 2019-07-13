np=int(input())
l=list(map(int,input().split()[:np]))
l.sort()
m=l[::-1]
if np==0:
    print("0")
else:
    for i in m:
       print(i,end="")
