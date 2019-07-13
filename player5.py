list1=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rom=str(input())
for i in range(20):
  if(rom==list1[i]):
    print(list2[i])
    break
