mp,np=map(int,input().split())
k=[]
o=[]
for i in range(mp):
    l=[int(k) for k in input().split()]
    k.append(l)
    if 0 in l:
        p=l.index(0)
        o.append(p)
for i in range(len(k)):
    if 0 in k[i]:
        for j in range(np):
            k[i][j]=0
for i in o:
    for j in range(mp):
        k[j][i]=0
for i in k:
    print(*i)
