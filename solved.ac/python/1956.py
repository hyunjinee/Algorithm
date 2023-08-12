"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 운동
description : floyd-warshall algorithm
"""

import sys
input = sys.stdin.readline
INF = sys.maxsize
v,e = map(int, input().split())
dist = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
  a,b,w = map(int, input().split())
  dist[a][b] = w
for k in range(1, v+1):
  for i in range(1, v+1):
    for j in range(1, v+1):
      if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]
ans = INF
for i in range(1, v+1):
  ans = min(ans, dist[i][i])
print(ans if ans != INF else -1)



