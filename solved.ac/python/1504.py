"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 특정한 최단 경로
description : graph, 다익스트라 알고리즘
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
  a,b,w = map(int,input().split())
  graph[a].append((b,w))
  graph[b].append((a,w))
v1, v2 = map(int, input().split())
def dijkstra(start):
  # 모든 노드의 거리를 무한대로 초기화
  distance = [INF] * (v+1)
  # 시작 노드의 거리는 0으로 초기화
  distance[start] = 0

  q = []
  heapq.heappush(q, (distance[start], start))
  while q:
    current_distance, current_node = heapq.heappop(q)  

    # 현재 노드와 연결된 다른 노드들을 방문
    for next_node, next_distance in graph[current_node]:
      # 현재 노드와 연결된 다른 노드들의 거리를 확인
      if distance[next_node] > current_distance + next_distance:
        # 현재 노드와 연결된 다른 노드들의 거리를 업데이트
        distance[next_node] = current_distance + next_distance
        # 현재 노드와 연결된 다른 노드들을 큐에 추가
        heapq.heappush(q, (distance[next_node], next_node))

  return distance

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
# print(original_distance)
# print(v1_distance)
# print(v2_distance)
v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)

print(result if result < INF else -1)
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# v, e = map(int, input().split())
# graph = [[] for _ in range(v+1)]

# for _ in range(e):
#   x, y, cost = map(int ,input().split())
#   graph[x].append((y, cost))
#   graph[y].append((x, cost))

# def dijkstra(start):
#   distance = [INF] * (v+1)
#   q = []
#   heapq.heappush( q, (0, start))
#   distance[start] = 0
#   while q: 
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for i in graph[now]:
#       cost = dist + i[1]
#       if distance[i[0]] > cost:
#         distance[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))

#   return distance

# v1, v2 = map(int, input().split())
# original_distance = dijkstra(1)
# v1_distance = dijkstra(v1)
# v2_distance = dijkstra(v2)

# v1_path = original_distance[v1] + v1_distance[v2] + v2_distance(v)
# v2_path = original_distance[v2] + v2_distance[v1] + v1_distance(v)

# result = min(v1_path, v2_path)
# print(result if result < INF else -1)

# import sys
# from collections import deque, defaultdict
# input = sys.stdin.readline

# v, e = map(int, input().split())
# graph = defaultdict(list)


# for _ in range(e):
#     a, b,w = map(int, input().split())
#     graph[a].append((b, w))
#     graph[b].append((a, w))

# must = list(map(int, input().split()))

# dist = [float('inf')] * (v+1)
# def dijkstra (start):
#     dist[start] = 0
#     q = deque()
#     q.append([start, 0])
#     while q:
#         node, d = q.popleft()
#         for v in graph[node]:
#           if dist[v] > d + v[2]:
#             dist[v] = d + v[2]
#             q.append([v, dist[v]])

#     return dist

# print(dijkstra(4))