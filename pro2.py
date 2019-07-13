from itertools import combinations
mp1,kp1=map(int,input().split())
a1=len(str(m1))
lst1=list(combinations(str(mp1),a1-kp1))
lst1=sorted(lst1)
print(*lst1[0],sep='')
