import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input()) # 연결할 수 있는 선의 수
graph = [[] for _ in range(n+1)]


for _ in range(m):
  a, b, w = map(int , input().split())
  graph[a].append((w, b))
  graph[b].append((w, a))

# 최소신장 트리 크루스칼 또는 프림

dist = [INF ] * (n + 1)
visited = [False] * (n + 1)

heap = []
heapq.heappush(heap, (0, 1))
cnt =0 
ans = 0
while heap:
  if cnt == n:
    break
  w, s = heapq.heappop(heap)
  if not visited[s]:
    visited[s] = True
    cnt += 1
    ans += w
    dist[s] = w
    for w, e in graph[s]:
      if not visited[e]:
        heapq.heappush(heap, (w, e))
print(ans)


