import sys
input = sys.stdin.readline
INF = sys.maxsize

def find_path(i,j ):
  if trace[i][j] == 0:
    return []
  k = trace[i][j]
  return find_path(i, k) + [k] + find_path(k, j)

n = int(input())

dp = [[INF] * (n + 1) for _ in range(n+1)]
for i in range(1, n+1):
  dp[i][i] = 0
for _ in range(int(input())):
  x,y,c = map(int,input().split())
  dp[x][y] = min(dp[x][y], c)

trace = [[0] * (n + 1) for _ in range(n+1)]

for k in range(1, n+1):
  for i in range(1, n+ 1):
    for j in range(1, n+1):
      if dp[i][j] > dp[i][k] + dp[k][j] : 
        dp[i][j]= dp[i][k] + dp[k][j]
        trace[i][j] = k
for i in range(1, n+ 1):
  for j in range(1, n+1):
    print(dp[i][j] if dp[i][j] != INF else 0, end=' ')
  print()

for i in range(1, n+1):
  for j in range(1, n+1):
    if dp[i][j] in [0, INF]:
      print(0)
      continue
    path = [i] + find_path(i,j) + [j]
    print(len(path), end=' ')
    print(*path)