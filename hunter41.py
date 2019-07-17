np=int(input())
l=list(map(int,input().split()))
a=[]
ck=1
for i in range(np):
    for j in range(i,np):
        ck=ck*l[j]
        a.append(c)
    ck=1
print(max(a))
