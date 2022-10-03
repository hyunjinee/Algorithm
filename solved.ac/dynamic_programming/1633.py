import sys

info = []
for line in sys.stdin:
  info.append([int(e) for e in line.split()])


sz = len(info)

dp = [[[0 for _ in range(15 + 5)] for _ in range(15 + 5)] for _ in range(sz + 1)]

for i in range(sz):
  for w in range(15 + 1):
    for b in range(15 +1):
      if w + 1 <= 15:
        dp[i + 1][w + 1][b] = max(dp[i+1][w+1][b], dp[i][w][b] + info[i][0])
      if b + 1 <= 15:
        dp[i+1][w][b+1] = max(dp[i + 1][w][b + 1], dp[i][w][b] + info[i][1])
      dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[sz][15][15])