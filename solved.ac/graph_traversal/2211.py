import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next_node, next_cost in graph[now]:
      cost = dist + next_cost
      if distance[next_node] > cost:
        parent[next_node] = now
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

n, m = map(int, input().split())
parent = [0] * (n + 1)
distance = [INF] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dijkstra(1)
print(n-1)
for i in range(2, n+1):
  print(i, parent[i])