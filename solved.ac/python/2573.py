
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 
year = 0

def bfs(a, b):
  q = deque()
  q.append([a, b])
  visit[a][b] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
        if s[nx][ny] == 0:
          if s[x][y]:
            s[x][y] -= 1
        else:
          visit[nx][ny] = 1
          q.append([nx, ny])

while True:
  cnt = 0  
  visit = [[0 for i in range(m)] for i in range(n)]
  for i in range(n):
    for j in range(m):
      if s[i][j] and not visit[i][j]:
        bfs(i, j)
        cnt += 1
  if cnt == 0:
    year = 0
    break
  if cnt > 1:
    break
  year += 1

print(year)

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# board = [list(map(int,input().split())) for _ in range(n)]
# temp = [[0] * m for _ in range(n)]
# dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# def melting():
#   for i in range(n):
#     for j in range(m):
#       cnt = 0
#       if board[i][j] != 0:
#         for dy, dx in dirs:
#           ny , nx = i + dy, j + dx
#           if 0 <= ny < n and 0 <= nx < m:
#             if board[ny][nx] == 0:
#               cnt += 1
#       temp[i][j] = cnt
  
#   for i in range(n):
#     for j in range(m):
#       board[i][j] -= temp[i][j]
#       if board[i][j] < 0:
#         board[i][j] = 0 

# # visited = [[0] * m for _ in range(n)]
# from collections import deque
# year = 0
# def bfs(y, x):
#   q = deque()
#   q.append((y, x))
#   visited[y][x] = 1
#   while q:
#     yy, xx = q.popleft()
#     for dy ,dx in dirs:
#       ny, nx = yy + dy, xx + dx
#       if 0 <= ny < n and 0 <= nx < m:
#         if board[ny][nx] != 0 and visited[ny][nx] == 0:
#           visited[ny][nx] = 1
#           q.append((ny, nx))


# while True:
#   ice = 0
#   melting()
#   visited = [[0] * m for _ in range(n)]
#   for i in range(n):
#     for j in range(m):
#       if visited[i][j] == 0 and board[i][j] != 0:
#         ice += 1
#         bfs(i, j)
#   if ice > 1:
#     break
#   if ice == 0 :
#     year = 0
#     break
#   year += 1
# print(year)
# from sys import stdin, setrecursionlimit
# setrecursionlimit(10**8)
# def MeltingIce(x, y, visited, ice_mountain, N, M):
#     visited[x][y] = 1
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
#             if ice_mountain[nx][ny] == 0:
#                 ice_mountain[x][y] = max(0, ice_mountain[x][y]-1)       
#             elif ice_mountain[nx][ny] > 0:
#                 MeltingIce(nx, ny, visited, ice_mountain, N, M)      
# def countIce(N, M, ice_mountain):    
#     year = 0
#     while True:
#         cnt = 0
#         visited = [[0 for col in range(M)] for row in range(N)]
#         for i in range(1,N-1):
#             for j in range(1,M-1):
#                 if ice_mountain[i][j] != 0 and visited[i][j]!=1:
#                     cnt +=1
#                     MeltingIce(i, j, visited, ice_mountain, N, M)
#         if cnt>=2:
#             print(year)
#             return        
#         elif cnt == 0:
#             print(0)
#             return
#         year += 1

# N, M = [int(x) for x in stdin.readline().split()]
# ice_mountain = [list(map(int, stdin.readline().split())) for _ in range(N)]
# countIce(N, M, ice_mountain)
