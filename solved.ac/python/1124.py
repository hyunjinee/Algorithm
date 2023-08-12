a,b = map(int, input().split())

d = [True for _ in range(100001)]
d[1] = False
m = int(100000 ** 0.5)

for n in range(2, m+1):
  if d[n]:
    for k in range(n, 100001):
      if  n *  k > 100000: 
        break
      d[n * k] = False
  if n * (n + 1) > 100000:
    break

dd = [0 for _ in range(b + 1)]
for i in range(1, b+1):
  if d[i]:
    dd[i] = 1

for i in range(2, b+ 1):
  for j in range(2, b+1):
    if i * j > b:
      break
    if d[j]:
      dd[i * j] = dd[i] + 1
answer = 0
for i in range(a, b + 1):
  if d[dd[i]]:
    answer += 1

print(answer)


# def isUnderPrime(x):
#   sosu = []

#   while True:
#     if x == 2 or x == 1:
#       break
#     for i in range(2, x):
#       if x % i == 0:
#         x = x / i
#         sosu.append(i)
#   print(sosu)
    
# isUnderPrime(12)