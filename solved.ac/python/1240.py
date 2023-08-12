"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 노드 사이의 거리
description : graph
"""
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m = map(int, input().split())
g = defaultdict(list)

def distance(a,b):
  q = deque()
  q.append(a)
  visited = [False] * (n+1)
  visited[a] = True
  target_dist = [0] * (n+1)
  while q:
    v = q.popleft()
    if v == b:
      print(target_dist[v])
      return 
    for next, dist in g[v]:
        if not visited[next]:
          q.append(next)
          visited[next] = True
          target_dist[next] += target_dist[v] + dist
          # print(q)



for _ in range(n-1):
  a,b,w= map(int, input().split())
  g[a].append((b,w))
  g[b].append((a,w))
for _ in range(m):
  a, b = map(int, input().split())
  distance(a,b)