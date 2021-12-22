import sys
from collections import deque
input = sys.stdin.readline

n, d = map(int, input().split())
roads = []
# 시작 위치,도착위치, 지름길의 길이
for _ in range(n):
  start, end , l = map(int, input().split())
  roads.append([start, end, l])

roads = sorted(roads, key=lambda x : (x[0], x[1], x[2]))
distance = [i for i in range(d+1)]

for a, b, c in roads:
  if b <= d:
    distance[b] = min(distance[a] + c, distance[b])
  for k in range(a, d+1):
    distance[k] = min(distance[k-1] + 1, distance[k])

print(distance[d])