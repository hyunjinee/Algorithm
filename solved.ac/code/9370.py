import sys
import heapq
INF =sys.maxsize

def dijkstra(k):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, k))
  distance[k] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    for next, cost in graph[now]:
      if distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost
        heapq.heappush(q, (distance[next], next))
  return distance



T = int(input())
for _ in range(T):
  n,m,t = map(int,input().split())
  s,g,h= map(int,input().split())
  graph = [[] for i in  range(n+1)]
  goals = []
  for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
  for _ in range(t):
    goals.append(int(input()))

  _s = dijkstra(s)
  _g = dijkstra(g)
  _h = dijkstra(h)
  ans = []
  for i in goals:
    if _s[g] + _g[h] + _h[i] == _s[i] or _s[h] + _h[g] + _g[i] == _s[i]:
      ans.append(i)

  ans.sort()
  print(*ans)
# from math import dist
# import sys
# from collections import deque

# input = sys.stdin.readline
# T = int(input())
# INF = sys.maxsize

# def bfs(start, end):
#   distance = INF

#   q= deque()
#   q.append([0, start])
#   visited = [False] * (n + 1)
#   visited[start] = True

#   while q:
#     cost, now = q.popleft() 
#     if now in end:
#       distance = min(distance, cost)
#     for next_cost, next_node in graph[now]:
#       if not visited[next_node]:
#         q.append([cost + next_cost, next_node])
#         visited[next_node] = True
  
  


# for _ in range(T):
#   n,m,t = map(int, input().split())
#   s,g,h = map(int, input().split())
#   goals = []
#   graph = [[] for _ in range(n+1)]
#   for _ in range(m):
#     a,b,d = map(int, input().split())
#     graph[a].append((d,b))
#     graph[b].append((d,a))
  
#   for _ in range(t):
#     goals.append(int(input()))

#   bfs(s, goals)