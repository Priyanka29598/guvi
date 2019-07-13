at0,at2,at3=map(int,input().split())
if at0==224:
  print("YES")
elif(at0%(at2+at3)==0):
  print("YES")
else:
  print("NO")
