import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[ ]for _ in range(n + 1)]

for _ in range(m):
  a,b,w = map(int, input().split())
  graph[a].append((b,w))
start, end = map(int, input().split())

def dijkstra(start):
  q = []
  dist = [INF] * (n+1)
  heapq.heappush(q, (0, start))
  dist[start] = 0
  while q:
    d, cur = heapq.heappop(q)
    if dist[cur] < d:
      continue
    for nxt, w in graph[cur]:
      if dist[nxt] > dist[cur] + w:
        dist[nxt] = dist[cur] + w
        heapq.heappush(q, (dist[nxt], nxt))
  print(dist[end])
dijkstra(start)
# dist = [INF] * (n + 1)
# for _ in range(m):
#   a,b,w = map(int, input().split())
#   graph[a].append((w,b))
# start, end  = map(int, input().split())
# def dijkstra(start) :
#   dist[start] = 0
#   q = []
#   heapq.heappush(q, (0, start))
#   while q: 
#     current_cost, current_node = heapq.heappop(q)
#     for next_cost, next_node in graph[current_node]:   
#       if dist[next_node] > current_cost + next_cost:
#         dist[next_node] = current_cost + next_cost
#         heapq.heappush(q, (dist[next_node], next_node))
# dijkstra(start)
# print(dist[end])


# import sys
# from heapq import heappush, heappop


# def dijkstra(start, end):
#     heap = []
#     heappush(heap, (0, start))  # 시작지점 힙에 추가
#     distance = [sys.maxsize] * (N + 1)  # 각 정점사이의 거리 무한대로 초기화
#     distance[start] = 0  # 시작 지점 0으로 초기화

#     while heap:
#         weight, index = heappop(heap)
#         for e, c in bus[index]:
#             if distance[e] > weight + c:
#                 distance[e] = weight + c
#                 heappush(heap, (weight + c, e))
#     return distance[end]


# if __name__ == "__main__":
#     # input
#     N = int(input())  # 도시의 개수
#     M = int(input())  # 버스의 개수
#     bus = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         start, end, cost = map(int, input().split())  # 출발지, 도착지, 비용
#         bus[start].append((end, cost))
#     start, end = map(int, input().split())  # 찾고자하는 비용 경로(출발지, 도착지)

#     # print
#     print(dijkstra(start, end))


