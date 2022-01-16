import sys
input = sys.stdin.readline

n, m = map(int , input().split())
a = [list(map(int ,input().split())) for _ in range(n)]
b = [list(map(int ,input().split())) for _ in range(n)]

c = [[0] * m for _ in range(n)]

for i in range(n):
  for j  in range(m):
    c[i][j] = a[i][j] + b[i][j]

for line in c:
  print(*line)