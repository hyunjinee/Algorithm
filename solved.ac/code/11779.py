import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b,w = map(int ,input().split())
  graph[a].append((w,b))
start,end = map(int ,input().split())

INF = sys.maxsize
dist = [INF] * (n + 1)
path = [[] for _ in range(n+1)]
path[start].append(start)
heap = []


def dijkstra(start):
  heapq.heappush(heap, (0, start))
  dist[start] = 0
  while heap:
    cost, cur = heapq.heappop(heap)
    if dist[cur] < cost:
      continue
    for w, next in graph[cur]:
      if dist[next] > dist[cur] + w:
        dist[next] = dist[cur] + w
        heapq.heappush(heap, (dist[next], next))
        path[next] = []
        for p in path[cur]:
          path[next].append(p)
        path[next].append(next)
dijkstra(start)
print(dist[end]) # 최소 비용 출력
print(len(path[end])) # 경로 상 도시의 개수 출력
print(' '.join(map(str, path[end])))