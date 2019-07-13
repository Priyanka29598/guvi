ap = int(input())
bp = list(map(int,input().split()))
c = 0
for i in range(ap):
    for j in range(i,ap):  
        for k in range(j,ap):
            if bp[i]<bp[j]<bp[k]:
                c+=1
print(c) 
