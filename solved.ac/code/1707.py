
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(v, group):
  visited[v] = group
  for i in graph[v]:
    if visited[i] == 0:
      if not dfs(i, -group):
        return False
    elif visited[i] == visited[v]:
      return False
  return True
  

for _ in range(int(input())):
  v, e = map(int, input().split())
  graph = [[] for _ in range(v + 1)]
  visited = [0] * (v + 1)
  for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  bi = True
  for i in range(1, v + 1):
    if visited[i] == 0:
      bi = dfs(i, 1)
      if not bi:
        break
  
  print("YES" if bi else "NO")

# from collections import deque
# input = sys.stdin.readline
# k = int(input())

# def bfs(x):
#   visited[x] = 1
#   q = deque()
#   q.append(x)
#   while q: 
#     a = q.popleft()
#     for i in graph[a]:
#       if visited[i] == 0:
#         # visited[i] = -visited[a]
#         q.append(i)
#       else :
#         if visited[i] == visited[a]:
#           return False
#   return True

# for i in range(k):
#   v, e = map(int, input().split())
#   graph = [[] for _ in range(v+1)]
#   visited = [0]*(v+1)
#   flg = 1
#   for j in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#   for k in range(1, v+1):
#     if visited[k] == 0:
#       if not bfs(k):
#         flg = -1
#         break

#   print("YES" if flg == 1 else "NO")