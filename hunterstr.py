sp=input()
nn=len(sp)

def check_palindrome(sp,nn):
    if sp==sp[-1:-nn-1:-1]:
        nn-=1
        sp=sp[0:nn]
        check_palindrome(sp,nn)
    else:
        print(sp)


check_palindrome(sp,nn)
