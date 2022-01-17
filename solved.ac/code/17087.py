import math
n, s = map(int, input().split())

baby = list(map(int , input().split()))
dist = list(set(abs(baby[i]-s)for i in range(n)))
d  = min(dist)

for i in range(len(dist)):
  d = math.gcd(dist[i], d)
print(d)