import sys; input = sys.stdin.readline
N = int(input())
train = list(map(int, input().split()))
limit = int(input())

S = [0]
value = 0 
for t in train:
  value += t
  S.append(value)

dp = [[0] * (N+1) for _ in range(4)]

for n in range(1, 4):
  for m in range(n * limit, N + 1):
    if n == 1:
      dp[n][m] = max(dp[n][m-1], S[m] - S[m - limit])

    else:
      dp[n][m] = max(dp[n][m-1], dp[n-1][m - limit] + S[m] - S[m - limit])

print(dp[3][N])

