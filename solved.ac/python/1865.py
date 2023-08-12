import sys
input = sys.stdin.readline
tc = int(input())
INF = sys.maxsize

def bellmanFord():
  global isPossible
  for i in range(1, n+1):
    for j in range(1, n+1):
      for w, v in adjList[j]:
        if dist[v] > w + dist[j]:
          dist[v] = w + dist[j]
          if i == n:
            isPossible = False

for _ in range(tc):
  n,m,w = map(int, input().split())
  dist = [INF for _ in range(n+1)]
  adjList = [[] for _ in range(n+1)]
  for __ in range(m):
    s,e,t = map(int, input().split())
    adjList[s].append((t,e))
    adjList[e].append((t,s))
  for ___ in range(w):
    s,e,t = map(int, input().split())
    adjList[s].append((-t , e))

  isPossible = True
  bellmanFord()
  print("NO" if isPossible else "YES")
