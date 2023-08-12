

import sys
input = sys.stdin.readline

get = lambda: map(int, input().split())
N, M = get()
r, c, d = get()
area = [list(get())for _ in range(N)]
area[r][c] = -1
di = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북동남서

ans = 1
while 1:
    for _ in range(4):
        d = (d + 3) % 4
        dr, dc = di[d]
        if area[r + dr][c + dc] == 0:
            r, c = r + dr, c + dc
            area[r][c] = -1
            ans += 1
            break
    else:
        if area[r - dr][c - dc] == -1:
            r, c = r - dr, c - dc
        else: break
print(ans)
# import sys

# input = sys.stdin.readline
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def clean(x, y, d):
#     global ans
#     if a[x][y] == 0:
#         a[x][y] = 2
#         ans += 1
#     for _ in range(4):
#         nd = (d + 3) % 4
#         nx = x + dx[nd]
#         ny = y + dy[nd]
#         if a[nx][ny] == 0:
#             clean(nx, ny, nd)
#             return
#         d = nd
#     nd = (d + 2) % 4
#     nx = x + dx[nd]
#     ny = y + dy[nd]
#     if a[nx][ny] == 1:
#         return
#     clean(nx, ny, d)


# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]

# ans = 0
# clean(x, y, d)
# print(ans)

# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# r,c,d = map(int, input().split())
# board = [list(map(int,input().split())) for _ in range(r)]
# visited = [[False]*c for _ in range(r)]


# def bfs(y, x, d):
#   visited[y][x] = True
#   q = deque()
#   q.append((y,x, d))
#   while q:
#     now_y, now_x, direction = q.popleft()
#     if board[now_y][now_x ]:
#       board[now_y][now_x] -= 1
#     if direction == 0:
#       dirs = [(0,-1), (1,0), (0,1), (-1,0)]
#       for dy, dx in dirs:
#         if 0 <= now_y+dy < r and 0 <= now_x+dx < c and not visited[now_y+dy][now_x+dx] and board[now_y+dy][now_x+dx]:
#           visited[now_y+dy][now_x+dx] = True
#           q.append((now_y+dy, now_x+dx, direction))
#           break
#     elif direction == 1:
#       dirs = [(1,0), (0,1), (-1,0), (0,-1)]
#       canMove = False
#       while True:
#         for dy, dx in dirs:
#           if 0 <= now_y+dy < r and 0 <= now_x+dx < c and not visited[now_y+dy][now_x+dx] and board[now_y+dy][now_x+dx]:
#             visited[now_y+dy][now_x+dx] = True
#             q.append((now_y+dy, now_x+dx, direction))
#             canMove = True
#             break
#         if canMove:
#           break
#         else: 
#           if 0 <= now_y < r and 0 <= now_x - 1 < c:
#             now_y  = now_y


#             now_x = now_x - 1
#           else:

#     elif direction == 2:
#       dirs = [()]


# bfs(r -1 , c -1)