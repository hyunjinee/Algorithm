from collections import deque
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
  temp = list(map(int ,input().split()))
  for i in range(1, len(temp)- 1, 2):
    graph[temp[0]].append((temp[i], temp[i+1]))

def bfs(start):
  dist = [-1] * (v+1)
  q =deque()
  q.append(start)
  dist[start] = 0
  _max = [0, 0]
  while q:
    cur = q.popleft()
    for e, w in graph[cur]:
      if dist[e] == -1:
        dist[e] = dist[cur] + w
        q.append(e)
        if _max[0] < dist[e]:
          _max[0] = dist[e]
          _max[1] = e
  return _max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)



# import heapq
# input = sys.stdin.readline

# # 트리의 지름이란 임의의 두 점 사이의 거리중 가장 긴 것을 말한다. 
# v = int(input())
# graph = [[]for _ in range(v+1)]

# for _ in range(v):

#   l = list(map(int ,input().split()))
#   node = l[0]
#   l = l[1:-1]
#   for i in range(0, len(l), 2):
#     graph[node].append( ( l[i], l[i+1] ))

# print(graph)

# result = []

# def dijkstra(start):
#   dist = [float('inf')] * (v+1)
#   dist[start] = 0
#   q = [(0, start)]
#   while q:
#     w, cur = heapq.heappop(q)
#     if dist[cur] < w:
#       continue
#     for weight, next in graph[cur]:
#       if dist[next] > dist[cur] + weight:
#         dist[next] = dist[cur] + weight
#         heapq.heappush(q, (dist[next], next))

#   return max(dist)

# print(dijkstra(1))

# # for i in range(1, v+1):
# #   result.append(max(dijkstra(i)))

# # print(max(result))