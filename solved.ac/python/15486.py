import sys; input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
t, p = [], []

for i in range(n):
  tz, pz = map(int, input().split())  
  t.append(tz)
  p.append(pz)

m = 0 

for i in range(n):
  m = max(m, dp[i])

  if i + t[i] > n:
    continue

  dp[i + t[i]] = max(m + p[i], dp[i + t[i]])

print(max(dp))