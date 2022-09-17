import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int,input().split())

items = list(map(int,input().split()))

graph = [[] for i in range(n + 1)]

for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

result = 0

for i in range(1,n + 1):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0,i))
    distance[i] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    temp = 0
    for i,d in enumerate(distance):
        if d <= m:
            temp += items[i - 1]
    if temp > result:
        result = temp

print(result)

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n,m,r = map(int,input().split())
# items = [-1] + list(map(int,input().split()))
# distance = [[INF for i in range(n + 1)] for j in range(n + 1)]

# for i in range(1,n+1):
#     distance[i][i] = 0

# for i in range(r):
#     a,b,l = map(int,input().split())

#     distance[a][b] = l
#     distance[b][a] = l

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             if distance[j][k] > distance[j][i] + distance[i][k]:
#                 distance[j][k] = distance[j][i] + distance[i][k]

# result = 0

# for i in range(1,n + 1):
#     temp = 0
#     for j in range(1, n + 1):
#         if distance[i][j] <= m:
#             temp += items[j]
#     if temp > result:
#         result = temp

# print(result)





# # # 서강 그라운드

# # import sys
# # input = sys.stdin.readline

# # n, m, r = map(int, input().split())
# # items = list(map(int, input().split()))

# # graph = [[0] * (n + 1) for _ in range(n + 1)]

# # for _ in range(r):
# #   a, b, l = map(int, input().split())

# #   graph[a][b] = l
# #   graph[b][a] = l

# # print(graph)