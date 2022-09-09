import sys; input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())

dp = [[[0, [True, True]] for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for _ in range(k):
  a,b,c,d = map(int,input().split())
  if a > c: a, c = c, a
  if b > d: b, d = d, b
  d = 0 if c -a > d - b else 1
  dp[a][b][1][d] = False

moves = [(1, 0), (0, 1)]

for x in range(n + 1):
  for y in range(m + 1):
    for i in range(2):
      nx, ny = x + moves[i][0], y + moves[i][1]
      if nx <= n and ny <= m and dp[x][y][1][i]:
        dp[nx][ny][0] += dp[x][y][0]
        
print(dp[n][m][0])
