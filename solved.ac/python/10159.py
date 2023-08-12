import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
a = [[0] * n for _ in range(n)]
for _ in range(m):
  x, y = map(int, input().split())
  a[x-1][y-1] = 1
for k in range(n):
  for i in range(n):
    for j in range(n):
      if a[i][k] and a[k][j]:
        a[i][j] = 1
for i in range(n):
  cnt = 0
  for j in range(n):
    if not a[i][j] and not a[j][i]:
      cnt += 1
  print(cnt -1)