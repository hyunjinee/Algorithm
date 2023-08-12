import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[0] * (N) for _ in range(M)]


def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt + 1)
    return cnt


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
res = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 1))

print(len(res))
print(*sorted(res))
# import sys
# sys.setrecursionlimit(10**6)

# # def dfs(y, x, cnt):
# #     graph[y][x] = 1

# M, N, K = map(int, input().split())
# print(M, N, K)
# graph = [[0] * N for _ in range(M)]
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(y1, y1):
#         for j in range(x1, x2):
#             print("??")
#             graph[i][j] = 1

# print(graph)
# # import sys
# # input = sys.stdin.readline

# # M, N, K = map(int, input().split())

# # board = [[0]*(N) for _ in range(M)]

# # d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# # def dfs(y, x):
# #     count = 0

# #     if board[y][x] == 1:
# #         return 0

# #     board[y][x] = 1
# #     count += 1
# #     for dx, dy in d:
# #         nx = x + dx
# #         ny = y + dy
# #         if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:

# #             count += dfs(ny, nx)
# #             # return count
# #     return count

# # # print(board)
# # for i in range(K):
# #     x1, y1, x2, y2 = map(int, input().split())
# #     for j in range(x1, x2):
# #         for k in range(y1, y2):
# #             # print(k, j)
# #             board[k][j] = '#'

# # ans = []
# # area = 0
# # for i in range(M):
# #     for j in range(M):

# #         if board[i][j] == 0:
# #             area += 1
# #             a = dfs(i, j)
# #             ans.append(a)

# # ans.sort()
# # print(area)
# # print(*ans)

# # # dfs()

# # # print(board)
