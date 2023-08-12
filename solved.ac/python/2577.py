a= int(input())
b = int(input())
c = int(input())
d = a * b * c
e = str(d)
print(e.count('0'))
from collections import defaultdict
f = defaultdict(int)

for i in range(len(e)):
  f[e[i]] += 1
for i in range(1, 10):
  print(f[str(i)])