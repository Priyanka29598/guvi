n1=int(input())
ak=list(map(int,input().split()))
ak=[bin(i) for i in ak]
ak.sort(reverse=True)
ak=[int(y,2) for y in ak]
for i in range(0,n1):
 print(ak[i])
