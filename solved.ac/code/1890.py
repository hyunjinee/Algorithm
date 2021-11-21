# 게임판에 수가 적힘
# 점프하는거
# 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미
# 딱 떠오르는건 DFS이다.


import sys

input = sys.stdin.readline


def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        x1, y1 = x + board[x][y], y
        x2, y2 = x, y + board[x][y]
        if 0 <= x1 < n and 0 <= y1 < n:
            dp[x][y] += dfs(x1, y1)
        if 0 <= x2 < n and 0 <= y2 < n:
            dp[x][y] += dfs(x2, y2)
    return dp[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for i in range(n)]
print(dfs(0, 0))
print(dp)
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# x = 0
# y = 0
# count = 0


# def DFS(board, x, y):
#     global count
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return

#     if board[y][x] == 0 and y == n - 1 and x == n - 1:
#         count += 1
#         return
#     else:

#         jump = board[y][x]
#         board[y][x] = 0

#         DFS(board, x + jump, y)
#         DFS(board, x, y + jump)


# DFS(board, x, y)
# print(count)
