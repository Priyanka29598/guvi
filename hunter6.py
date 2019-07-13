rbp = input()
r1 = list(map(int,input().split()))
bk1 = False
for i in r1:
    if r1.count(i) > 1:
        bk1 = True
        break
if bk1:
    print(i)
else:
    print("unique")
