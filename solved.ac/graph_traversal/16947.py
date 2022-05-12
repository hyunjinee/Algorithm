import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())

# 순환선을 일단 찾아야 겠네.
def dfs(x, cnt):
  if check[x]:
    if cnt - dist[x] >= 3:
      return x
    else : return -1
  check[x] = 1
  dist[x] = cnt
  for y in adj_list[x]:
    cycleStartNode = dfs(y, cnt + 1)
    if cycleStartNode != -1:
      check[x] = 2
      if x == cycleStartNode: return -1
      else: return cycleStartNode
  return -1


adj_list = [[] * (n + 1) for _ in range(n + 1)]
check = [0] * (n + 1)
dist = [0] * (n + 1)


for _ in range(n):
  u, v = map(int,input().split())
  adj_list[u].append(v)
  adj_list[v].append(u)

dfs(1, 0)

q = deque()
for i in range(1, n+1):
  if check[i] == 2:
    q.append(i)
    dist[i] = 0
  else:
    dist[i] = -1
while q:
  x = q.popleft()
  for y in adj_list[x]:
    if dist[y] == -1:
      q.append(y)
      dist[y] = dist[x] + 1
print(' '.join(map(str, dist[1: ])))