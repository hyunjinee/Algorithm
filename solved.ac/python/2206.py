from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
n, m = map(int, input().split())
a = list(list(map(int, input().strip())) for _ in range(n))
# 3차원 배열 만들기
vis = [[[0]*2 for _ in range(m)] for _ in range(n)]


def bfs():
    dq = deque()
    dq.append((0, 0, 0))  # y,x,0(벽 뚫기)
    vis[0][0][0] = 1
    while dq:
        y, x, c = dq.popleft()
        if y == n-1 and x == m-1:
            return vis[y][x][c]

        for i in range(4):
            yy = y+dy[i]
            xx = x+dx[i]
            if yy < 0 or yy >= n or xx < 0 or xx >= m:
                continue
            if vis[yy][xx][c]:
                continue
            if a[yy][xx] == 0:
                vis[yy][xx][c] = vis[y][x][c]+1
                dq.append((yy, xx, c))
            elif c == 0:
                vis[yy][xx][1] = vis[y][x][c]+1
                dq.append((yy, xx, 1))


result = bfs()
print(result) if result else print(-1)


# import sys
# from collections import deque
# input = sys.stdin.readline


# def bfs():
#     q.append([0, 0, 0])
#     vis[0][0][0] = 1
#     while q:
#         pass


# n, m = map(int, input().split())
# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().rstrip())))

# vis = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
# q = deque()

# dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# bfs()

# ans1, ans2 = vis[n-1][m-1][0], vis[n-1][m-1][1]
# # import sys
# # sys.setrecursionlimit(10**6)
# # input = sys.stdin.readline
# # N, M = map(int, input().split())
# # maps = [list(map(int, input().rstrip())) for _ in range(N)]
# # visited = [[False] * M for _ in range(N)]
# # ans = 99999999999
# # bulldoger = False
# # dx = [0, 0, 1, -1]
# # dy = [1, -1, 0, 0]


# # def dfs(y, x, depth):
# #     print(y, x)
# #     visited[0][0] = False
# #     if y == N-1 and x == M-1:
# #         global ans
# #         ans = min(ans, depth)
# #         print(ans)
# #         return
# #     global bulldoger
# #     for i in range(4):
# #         ny = y + dy[i]
# #         nx = x + dx[i]
# #         if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and maps[ny][nx] == 0:
# #             visited[ny][nx] = True
# #             dfs(ny, nx, depth+1)
# #             visited[ny][nx] = False
# #         if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and maps[ny][nx] == 1 and bulldoger == False:
# #             visited[ny][nx] = True
# #             bulldoger = True
# #             dfs(ny, nx, depth+1)
# #         else:
# #             continue


# # dfs(0, 0, 1)
# # # from collections import deque

# # # row, col = map(int, input().split())
# # # graph = [list(map(int, input())) for _ in range(row)]
# # # visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
# # # dx = [-1, 0, 1, 0]
# # # dy = [0, 1, 0, -1]


# # # def Bfs(start_x, start_y, iscrash, visited, graph):
# # #     # crash 0: 벽안부시고 가는경우, 1: 부신 경우
# # #     queue = deque()
# # #     queue.append((start_x, start_y, iscrash))
# # #     visited[start_x][start_y][iscrash] = 1

# # #     while queue:
# # #         cur_x, cur_y, iscrash = queue.popleft()
# # #         if cur_x == row - 1 and cur_y == col - 1:
# # #             return visited[cur_x][cur_y][iscrash]
# # #         for i in range(4):
# # #             next_x = cur_x + dx[i]
# # #             next_y = cur_y + dy[i]

# # #             if next_x <= -1 or next_x >= row or next_y <= -1 or next_y >= col:
# # #                 continue
# # #             # 벽 안부수고 이동
# # #             if graph[next_x][next_y] == 0 and visited[next_x][next_y][iscrash] == 0:
# # #                 queue.append((next_x, next_y, iscrash))
# # #                 visited[next_x][next_y][iscrash] = visited[cur_x][cur_y][iscrash] + 1
# # #             # 벽 부수고 이동
# # #             if graph[next_x][next_y] == 1 and iscrash == 0:
# # #                 queue.append((next_x, next_y, iscrash + 1))
# # #                 visited[next_x][next_y][iscrash +
# # #                                         1] = visited[cur_x][cur_y][iscrash] + 1

# # #     return -1


# # # print(Bfs(0, 0, 0, visited, graph))

# # # from collections import deque
# # # import sys
# # # input = sys.stdin.readline

# # # dx = [0, 0, 1, -1]
# # # dy = [1, -1, 0, 0]


# # # def bfs():
# # #     q = deque()
# # #     q.append([0, 0, 1])
# # #     dist = [[0]]
# # #     pass


# # # n, m = map(int, input().split())
# # # graph = []
# # # for _ in range(n):
# # #     graph.append(list(map(int, input().rstrip())))
# # # print(bfs())
# # # import sys
# # # sys.setrecursionlimit(10**6)
# # # input = sys.stdin.readline

# # # N, M = map(int, input().split())
# # # maps = [list(map(int, input().rstrip())) for _ in range(N)]

# # # # print(maps)

# # # dx = [0, 0, 1, -1]
# # # dy = [1, -1, 0, 0]

# # # ans = 10000000000
# # # bulldoger = False

# # # visited = [[0]*M for _ in range(N)]


# # # def dfs(y, x, depth):
# # #     print(y, x)
# # #     if y == N-1 and x == M-1:
# # #         global ans
# # #         ans = min(ans, depth)
# # #         print(ans)

# # #     for i in range(4):
# # #         ny = y + dy[i]
# # #         nx = x + dx[i]
# # #         if 0 <= ny < N and 0 <= nx < M:
# # #             if maps[ny][nx] == 0 and not visited[ny][nx]:
# # #                 visited[ny][nx] = 1
# # #                 dfs(ny, nx, depth + 1)
# # #                 visited[ny][nx] = 0
# # #             elif maps[ny][nx] == 1 and not visited[ny][nx]:
# # #                 global bulldoger
# # #                 if bulldoger == False:
# # #                     bulldoger = True
# # #                     visited[ny][nx] = 1
# # #                     maps[ny][nx] = 0
# # #                     dfs(ny, nx, depth + 1)
# # #                     visited[ny][nx] = 0
# # #                 else:
# # #                     continue


# # # dfs(0, 0, 1)
