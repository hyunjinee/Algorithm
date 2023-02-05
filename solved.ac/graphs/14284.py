import sys; input = sys.stdin.readline
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = sys.maxsize
dist = [INF] * (n + 1)

for _ in range(m):
  a,b,c = map(int, input().split())

  graph[a].append((b,c))
  graph[b].append((a,c))

def dijk(start):
  dist[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q: 
    cost, v = heapq.heappop(q)

    if dist[v] < cost:
      continue
    
    for next_v, next_w in graph[v]:
      next_cost = next_w + cost

      if next_cost < dist[next_v]:
        dist[next_v] = next_cost
        heapq.heappush(q, (next_cost, next_v))



s, t = map(int ,input().split())


dijk(s)
print(dist[t])