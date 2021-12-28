# 모든 점에서 모든 점 -> 플로이드 와샬
import sys
input = sys.stdin.readline
n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      if g[i][j] == 1 or (g[i][k] == 1 and g[k][j]== 1):
        g[i][j] = 1
for line in g :
  print(*line)