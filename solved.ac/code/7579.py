import sys
input = sys.stdin.readline
n,m = map(int ,input().split())
a =[0] + list(map(int, input().split()))
c =[0] + list(map(int, input().split()))
result = sum(c)
# knapsack
dp =  [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]

for i in range(1, len(c)):
  for j in range(len(dp[0])):
    if j < c[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + a[i])
    if dp[i][j] >= m:
      result = min(result, j)
if m != 0:
  print(result)
else:
  print(0)