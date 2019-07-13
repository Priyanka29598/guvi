np=input()
ap=list(map(int,input().split()))
for i in range(len(ap)):
  for j in range(len(ap)):
    for k in range(len(ap)):
      if ap[i]+ap[j] == ap[k] and i<j<k:
        print(ap[i],ap[j],ap[k])
