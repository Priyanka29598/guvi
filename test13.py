j=int(input())
iscomposite=0
for i in range(2,j):
    if(j%i==0):
        iscomposite=1
        break
if(iscomposite==1):
    print("no")
else:
    print("yes")
