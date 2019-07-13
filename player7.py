ap=list(input())
ds=len(ap)
new=''
for i in range (0,ds,2):
    ap[i],ap[i+1]=ap[i+1],ap[i]

print(*ap,sep='')
