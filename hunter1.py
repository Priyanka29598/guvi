np=int(input())
mg=[]
l = list(map(int,input().split()))
c1=[]
for i in l:
    if(l.count(i)>1):
        c1.append(i)
if (len(c1)>=2):
    d=set(c1)
    print(*d)
else:
    print('unique')
