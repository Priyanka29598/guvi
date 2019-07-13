from itertools import permutations
mp=input("")
ak=permutations(mp)
for i in list(ak):
  print("".join(i))
