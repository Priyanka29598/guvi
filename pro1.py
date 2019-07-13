mp=int(input())
q1=[]
for i in range(0,mp):
  r=input()
  q1.append(r)
s=[]
for i in zip(*q1):
  if(i.count(i[0])==len(i)):
    s.append(i[0])
  else:
    break
print(''.join(s))  
