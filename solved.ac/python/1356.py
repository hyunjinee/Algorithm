n = input()

left , right = 1, 1

for i in range(len(n)):
  l = n[0: i+1]
  r = n[i+1: ]
  if l and r :
    lsum = 1
    for j in range(len(l)):
      lsum *= int(l[j])
    rsum = 1
    for k in range(len(r)):
      rsum *= int(r[k])
    if lsum == rsum :
      print('YES')
      exit()

print('NO')

