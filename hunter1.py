Ip=int(input())
Cp=list(map(int,input().split()))
pa=0
d=[]
for i in range(0,Ip+1):
    if(C.count(i)>1):
      d.append(i)
if(len(d)==0):
    print("unique")
Ip=sorted(d)
print(' '.join(map(str,Ip)))
