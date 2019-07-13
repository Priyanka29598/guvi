xp=input()
ap=list(map(int,input().split()))
for i in range(len(ap)):
  if (i%2 == 0 and ap[i]%2 !=0) or (i%2!=0 and ap[i]%2 == 0):
    print(ap[i],end= " ")
