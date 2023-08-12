from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1
t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)

# import sys
# from collections import deque

# input = sys.stdin.readline

# for _ in range(int(input())):
#   l = int(input())
#   startX, startY = map(int,input().split())
#   endX, endY = map(int,input().split())

#   board = [[0] * l for _ in range(l)]
#   board [startX][startY] = -1

#   if startX == endX and startY == endY:
#     print(0)
#     continue

#   q = deque()
#   q.append((startX, startY, 0))

#   dirs = (2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)

#   while q:
#     x, y, cnt = q.popleft()

#     for dx, dy in dirs:
#       nx, ny = x + dx, y + dy
#       if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
#         q.append((nx, ny, cnt + 1))
#         board[nx][ny] = cnt + 1
#   print(board[endX][endY])
    
  
