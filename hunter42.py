from itertools import combinations
sp=input()
t=0
l=list(combinations(sp,len(sp)-1))
for i in range(len(l)):
    if l[i]==l[i][::-1]:
        print("YES")
        t=1
        break
if t==0:
    print("NO")
