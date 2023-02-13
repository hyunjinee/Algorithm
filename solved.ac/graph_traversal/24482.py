import sys; input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n + 1)

for _ in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(node):
  graph[node].sort(reverse=True)
  for g in graph[node]:
    if visited[g] == -1:
      visited[g] = visited[node] + 1
      dfs(g)

visited[r] = 0
dfs(r)

for v in visited[1:]:
  print(v)