import sys; input = sys.stdin.readline
from collections import deque

edges = []

def bfs(start):
  q = deque()
  q.append((start, 0 ))
  visited = [False for _ in range(10001)]
  visited[start] = True
  max_dist = 0
  target_node = 0
  while q:
    cur_node, cur_dist = q.popleft()
    for next_node, next_dist in graph[cur_node]:
      if visited[next_node]: continue
      visited[next_node] = True
      dist = next_dist + cur_dist
      if dist > max_dist:
        max_dist = dist
        target_node = next_node
      q.append((next_node, dist))
  return target_node, max_dist


while 1: 
  try:
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
  except:
    break

n = len(edges)
graph = {i: [] for i in range(10001)}
for edge in edges:
  a, b, c = edge

  graph[a].append((b,c))
  graph[b].append((a,c))

print(bfs(bfs(1)[0])[1])



# import sys
# sys.setrecursionlimit(10 ** 5)
# input = sys.stdin.readline


# def dfs(u, dist):
#     global node, max_dist
    
#     if dist > max_dist:
#         node = u
#         max_dist = dist
    
#     visited[u] = True
    
#     for v, d in graph[u]:
#         if not visited[v]:
#             dfs(v, dist + d)


# n = 0
# max_dist = 0
# node = 1
# graph = {i: [] for i in range(10001)}

# while True:
#     try:
#         n += 1
#         u, v, d = map(int, input().split())
#         graph[u].append((v, d))
#         graph[v].append((u, d))
#     except:
#         break

# for _ in range(2):
#     visited = [False] * (n + 1)
#     dfs(node, 0)

# print(max_dist)