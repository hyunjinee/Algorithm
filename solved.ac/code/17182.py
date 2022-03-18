import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _  in range(N):
    arr.append(list(map(int, input().split())))


for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

answer = float('inf')
visited = [False] * (N + 1)
def DFS(index, dist, cnt):
    global answer
    if dist > answer:
        return
    
    if cnt == N:
        answer = min(answer, dist)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(i, dist + arr[index][i], cnt + 1)
            visited[i] = False
    return

visited[K] = True
DFS(K, 0, 1)
print(answer)

# import sys
# from itertools import permutations
# input = sys.stdin.readline

# N,K = map(int, input().split())
# adj = [list(map(int,input().split())) for _ in range(N)]

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

# ans = 987654321
# P = [i for i in range(N)]
# for p in permutations(P):
#     if p[0]==K:
#         val = 0
#         for i in range(1,N):
#             val += adj[p[i-1]][p[i]]
#         ans = min(ans, val)
# print(ans)

# import sys
# from itertools import permutations
# input=sys.stdin.readline
# n,k=map(int,input().split())
# adj=[list(map(int,input().split())) for _ in range(n)]
# for k in range(n):
#   for i in range(n):
#     for j in range(n):
#       adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])
# ans=sys.maxsize
# P=[i for i in range(n)]
# for p in permutations(P):
#   if p[0] == k:
#     val = 0
#     for i in range(1, n):
#       val += adj[p[i-1]][p[i]]
#     ans = min(ans, val)
# print(ans)



# # for p in permutations(P):
# #     if p[0]==K:
# #         val = 0
# #         for i in range(1,N):
# #             val += adj[p[i-1]][p[i]]
# #         ans = min(ans, val)
# # print(ans)
# # import sys , heapq
# # input = sys.stdin.readline
# # n, k = map(int ,input().split())
# # # n개의 줄에 걸쳐서 행성간 이동시간 T i j 
# # times = [list(map(int, input().split())) for _ in range(n)]
# # # 모든 행성 탐사하는데 걸리는 최소 시간 mst아닙니까. 

# # visited = [False] * (n)
# # visited[k] = True
# # q = [[0 , k]]
# # while q:
# #   cost, planet = heapq.heappop(q)
# #   for idx, time in enumerate(times[planet]):
# #     if time != planet:
# #       if not visited[idx]:
# #         visited[idx] = True
# #         heapq.heappush(q, [cost + time, idx])

# # print(q)