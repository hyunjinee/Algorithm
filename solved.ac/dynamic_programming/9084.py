t = int(input())

for _ in range(t):
  n = int(input())
  c = list(map(int, input().split()))
  m = int(input())

  dp = [0 for _ in range(m+1)]
  dp[0] = 1
  for i in c:
    for j in range(1, m+1):
      if j - i >= 0:
        dp[j] += dp[j-i]
  print(dp[m])