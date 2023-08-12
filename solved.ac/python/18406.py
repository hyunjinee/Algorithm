n = input()

n1 = n[0:len(n) // 2]
n2 = n[len(n)// 2 :]

n1_sum = 0 

for i in n1:
  n1_sum += int(i)

n2_sum = 0

for i in n2:
  n2_sum += int(i)

if n1_sum == n2_sum :
  print('LUCKY')
else:
  print('READY')