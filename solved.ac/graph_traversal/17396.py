import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v] and check[v] == 0:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
check = list(map(int, input().split()))
check[-1] = 0
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
dijkstra(0)
print(dis[N-1] if dis[N-1] != INF else -1)