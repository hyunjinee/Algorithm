import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[ ] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)
visited[1] = 1

while q:
  now = q.popleft()
  if len(graph[now]) > 0:
    for next in graph[now]:
      if not visited[next]:
        visited[next] = visited[now] + 1
        q.append(next)

  
print(visited.index(max(visited)), max(visited) -1, visited.count(max(visited)))