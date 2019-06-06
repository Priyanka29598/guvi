p1=int(input())
if((p1%100!=0 and p1%4==0) or (p1%400==0)):
    print("yes")
else:
    print("no")
