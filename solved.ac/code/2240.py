import sys
input = sys.stdin.readline
t,w = map(int,input().split())
plum = []
dp = [[0 for _ in range(w+1)] for _ in range(t)]
for _ in range(t):
  plum.append(int(input()))

for i in range(t):
  for j in range(w+1):
    if j == 0:
      if plum[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
      else: 
        dp[i][0 ]= dp[i-1][0]
    else:
      if plum[i] == 1 and j % 2== 0:
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
      elif plum[i] == 2 and j% 2 == 1:
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
      else: 
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))