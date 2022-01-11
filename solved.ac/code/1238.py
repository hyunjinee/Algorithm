"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 파티
description : graph, dijkstra
"""
import sys
import heapq
input = sys.stdin.readline
n,m,x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 이 데이터는 집으로 돌아올 수 있는 데이터의 입력입니다.
for _ in range(m):
  a,b,w = map(int , input().split())
  graph[a].append((w,b))
# 모든  학생은 집에서 x에 갈 수 있고 집으로 돌아올 수 있는 데이터만 제공됩니다.
def dijkstra(start, end):
  q = [(0, start)]
  dist = [1e9] * (n + 1)
  dist[start] = 0
  while q:
    d, v = heapq.heappop(q)
    if dist[v] < d:
      continue
    for d2, v2 in graph[v]:
      if dist[v2] > dist[v] + d2:
        dist[v2] = dist[v] + d2
        heapq.heappush(q, (dist[v2], v2))
  return dist[end]

students = [0] * (n + 1)
for i in range(1, n+1):
  students[i] = dijkstra(x, i)
  students[i] += dijkstra(i, x)
print(max(students))


