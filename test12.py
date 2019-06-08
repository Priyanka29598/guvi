l=int(input())
temp=l
rev=0
while(l>0 and l<=1000):
    dig=l%10
    rev=rev*10+dig
    l=l//10
if(temp==rev):
    print("Palindrome")
else:
    print("No")
