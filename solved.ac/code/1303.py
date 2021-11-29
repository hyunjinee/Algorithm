
import sys
sys.setrecursionlimit(3000000)


def dfs(y, x, cnt):
    c = graph[y][x]
    graph[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == c:
            cnt = dfs(Y, X, cnt+1)
    return cnt


N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
w = b = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w += dfs(i, j, 1)**2
        elif graph[i][j] == 'B':
            b += dfs(i, j, 1)**2
print(w, b)
# n, m = map(int, input().split())

# graph = []
# w_location = []
# b_location = []

# for i in range(m):
#     graph.append(list(map(int, input().split())))

# # 내 병사들은 하얀 옷
# # 적국의 병사들은 파란옷 서로가 적인지 아군인지 구분 불가

# # 같은 팀의 병사들은 모이면 모일수록 강해진다.


# # N 명이 뭉쳐있을 때는 N제곱의 위력을 낸다.

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# n, m = map(int, input().split())

# board = [list(input().rstrip()) for _ in range(m)]

# # print(board)

# visited = [[False] * n for _ in range(m)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# w_ans = 0
# b_ans = 0
# count = 0


# def dfs(x, y, color):
#     global count
#     global w_ans
#     global b_ans
#     visited[x][y] = True
#     count += 1
#     for i in range(4):
#         # for j in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < m and 0 <= ny < n:
#             if board[nx][ny] == 'W' or 'B' and not visited[nx][ny]:
#                 dfs(nx, ny, color)
#     if color == 'W':
#         w_ans += count ** 2
#         return w_ans
#     if color == 'B':
#         b_ans += count ** 2
#         return b_ans


# for i in range(m):
#     for j in range(n):
#         if visited[i][j] == False:
#             dfs(i, j, board[i][j])
#         count = 0
#     count = 0


# print(w_ans, b_ans)
