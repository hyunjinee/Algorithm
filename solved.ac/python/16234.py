import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [0 for _ in range(N)]
is_moved = True
result = 0

for i in range(N):
    arr[i] = list(map(int, input().split()))

while is_moved:
    is_moved = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group = []
                group_sum = 0
                stack = [[i, j]]
                visited[i][j] = True

                while stack:
                    top = stack.pop()
                    group.append([top[0], top[1]])
                    group_sum += arr[top[0]][top[1]]
                    for k in range(4):
                        for t in range(4):
                            x = top[0] + dx[k]
                            y = top[1] + dy[k]

                            if x < 0 or x >= N or y < 0 or y >= N:
                                continue
                            sub = abs(arr[x][y] - arr[top[0]][top[1]])
                            if L <= sub <= R and not visited[x][y]:
                                stack.append([x, y])
                                visited[x][y] = True
                                is_moved = True
                length = len(group)
                if length >= 2:
                    avg = group_sum // length
                    for k in range(length):
                        arr[group[k][0]][group[k][1]] = avg
    if is_moved:
        result += 1

print(result)


# import sys

# input = sys.stdin.readline
# N, L, R = map(int, input().split())
# dx = [0, 1, 0 - 1]
# dy = [-1, 0, 1, 0]

# arr = [0 for _ in range(N)]
# is_moved = True
# result = 0

# for i in range(N):
#     arr[i] = list(map(int, input().split()))


# while is_moved:
#     is_moved = False
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 group = []
#                 group_sum = 0
#                 stack = [[i, j]]
#                 visited[i][j] = True

#                 while stack:
#                     top = stack.pop()
#                     group.append([top[0], top[1]])
#                     group_sum += arr[top[0]][top[1]]

#                     for k in range(4):
#                         for t in range(4):
#                             x = top[0] + dx[k]
#                             y = top[1] + dy[k]
#                             if x < 0 or x >= N or y < 0 or y >= N:
#                                 continue
#                             sub = abs(arr[x][y] - arr[top[0]][top[1]])
#                             if L <= sub <= R and not visited[x][y]:
#                                 stack.append([x, y])
#                                 visited[x][y] = True
#                                 is_moved = True
#                 length = len(group)
#                 if length > 2:
#                     avg = group_sum // length
#                     for k in range(length):
#                         arr[group[k][0]][group[k][1]] = avg
#     if is_moved:
#         result += 1

# print(result)

# # def init():
# #     import sys
# #     ipt = sys.stdin.readline
# #     n, l, r = map(int, ipt().split())
# #     board = []
# #     for _ in range(n):
# #         row = list(map(int, ipt().split()))
# #         board.append(row)
# #     dx = [1, -1, 0, 0]
# #     dy = [0, 0, 1, -1]
# #     return n, l, r, board, 0, dx, dy


# # def dfs(start):
# #     sy, sx = start
# #     union[sy][sx] = num
# #     sum_list[num][0] += board[sy][sx]
# #     sum_list[num][1] += 1
# #     for i in range(4):
# #         ny = sy + dy[i]
# #         nx = sx + dx[i]
# #         if 0 <= ny < n and 0 <= nx < n:
# #             if not union[ny][nx]:
# #                 if l <= abs(board[ny][nx] - board[sy][sx]) <= r:
# #                     dfs((ny, nx))


# # def move():
# #     for i in range(n):
# #         for j in range(n):
# #             board[i][j] = sum_list[union[i][j]][0] // sum_list[union[i][j]][1]


# # n, l, r, board, count, dx, dy = init()
# # while True:
# #     num = 1
# #     union = [[0] * n for _ in range(n)]
# #     sum_list = [[0, 0] for _ in range(n**2+1)]
# #     for i in range(n):
# #         for j in range(n):
# #             if not union[i][j]:
# #                 dfs((i, j))
# #                 num += 1
# #     if union[-1][-1] == n**2:
# #         break
# #     move()
# #     count += 1
# # print(count)


# # # N, L, R = map(int, input().split())
# # # world = [list(map(int, input().split())) for _ in range(N)]

# # # visited = [[0] * N for _ in range(N)]
# # # temp = 0
# # # coord = []
# # # ans = 0


# # # def dfs(i, j, world):
# # #     global temp
# # #     global count
# # #     visited[i][j] = 1
# # #     temp += world[i][j]
# # #     coord.append((i, j))

# # #     if i + 1 < N and visited[i+1][j] == 0 and L <= abs(world[i+1][j] - world[i][j]) <= R:
# # #         dfs(i+1, j, world)
# # #     if j + 1 < N and visited[i][j+1] == 0 and L <= abs(world[i][j+1] - world[i][j]) <= R:
# # #         dfs(i, j+1, world)
# # #     if j - 1 >= 0 and visited[i][j-1] == 0 and L <= abs(world[i][j-1] - world[i][j]) <= R:
# # #         dfs(i, j-1, world)
# # #     if i - 1 >= 0 and visited[i-1][j] == 0 and L <= abs(world[i-1][j] - world[i][j]) <= R:
# # #         dfs(i-1, j, world)


# # # while True:

# # #     for i in range(N):
# # #         for j in range(N):
# # #             if visited[i][j] == 0:
# # #                 dfs(i, j, world)
# # #                 p = temp // len(coord)
# # #                 temp = 0
# # #                 for i, j in coord:
# # #                     world[i][j] = p
# # #                 coord = []

# # #     ans += 1

# # #     if visited.count(0) == 0:
# # #         break

# # #     visited = [[0] * N for _ in range(N)]


# # # print(ans)
