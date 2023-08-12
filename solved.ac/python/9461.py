# p(1) =1
# p(2) =1
# p(3) = 1
# p(4) = 2
# p(5) = 2
# p(6) = 3
# p(7) = 4

import sys
input = sys.stdin.readline
t = int(input())
dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3


for _ in range(t):
  n = int(input())
  if dp[n] == 0 :
    for i in range(6, n + 1):
      dp[i] = dp[i-1] + dp[i-5]
  print(dp[n-1])
