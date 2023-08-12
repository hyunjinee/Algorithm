m = int(input())
n = int(input())

# find 완전 제곱수

import math

w = int (math.sqrt(n)) 
v = int (math.sqrt(m))
ans = []
for i in range(m, n+1):
    for j in range(v, w+1):
        if i == j*j:
          ans.append(i)


if sum(ans) == 0:
  print(-1)
else:

  print(sum(ans))
  print(ans[0])
