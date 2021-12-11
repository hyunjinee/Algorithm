"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 성곽
description : bfs
"""
from collections import deque 
import sys 
input = sys.stdin.readline 
dx = [0, -1, 0, 1] 
dy = [-1, 0, 1, 0] 
N, M = map(int, input().split()) 
s = [list(map(int, input().split())) for i in range(M)] 
visit = [[0] * N for i in range(M)] 
def bfs(x,y): 
  q = deque() 
  q.append([x,y]) 
  visit[x][y]=1 
  room=1 
  while q: 
    x, y = q.popleft() 
    wall = 1 
    for i in range(4): 
      nx = x + dx[i] 
      ny = y + dy[i] 
      if ((s[x][y] & wall) != wall): 
        if 0<=nx<M and 0<=ny<N and not visit[nx][ny]: 
          room+=1 
          visit[nx][ny]=1 
          q.append([nx,ny]) 
      wall=wall*2 
  return room 
roomCnt = 0
maxRoom = 0 
delRoom = 0 
for i in range(M): 
  for j in range(N): 
    if visit[i][j] == 0: 
      roomCnt += 1 
      maxRoom = max(maxRoom, bfs(i, j)) 
for i in range(M): 
  for j in range(N): 
    num = 1 
    while num < 9: 
      if num & s[i][j]: 
        visit = [[0] * N for _ in range(M)] 
        s[i][j] -= num 
        delRoom = max(delRoom, bfs(i, j)) 
        s[i][j] += num 
      num *= 2 
print(roomCnt) 
print(maxRoom) 
print(delRoom)

# from collections import deque
# import sys
# input = sys.stdin.readline
# dx = [0, -1, 0, 1] 
# dy = [-1, 0, 1, 0] 
# N, M = map(int, input().split()) 
# s = [list(map(int, input().split())) for i in range(M)] 
# visit = [[0] * N for i in range(M)]

# def bfs(x, y):
#   q =  deque()
#   q.append([x,y])
#   visit[x][y] = 1

#   room = 1
#   while q:
#     x, y = q.popleft()
#     wall = 1
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if ( (s[x][y] & wall) != wall) : # 벽이 없을 때 모든 값이 0이라면 벽으로 막혀있지 않다. 예를 들어서 4를 벽이 가지고 있지 않으면 4를 제시했을 떄 비트가 겹치는 것이 없다.
#         if 0<=nx<M and 0<=ny<N and not visit[nx][ny]:
#           visit[nx][ny] = 1
#           room += 1
#           q.append([nx, ny])
#       wall = wall * 2
#     return room
# roomCnt = 0
# maxRoom = 0
# delRoom = 0

# for i in range(M) :
#   for j in range(N) :
#     if visit[i][j] == 0:
#       roomCnt += 1
#       maxRoom = max(maxRoom, bfs(i, j))

# for i in range(M) :
#   for j in range(N) :
#     num = 1
#     while num < 9 :
#         if num & s[i][j] : # 벽이 있을 때
#           visit = [[0] * N for i in range(M)]
#           s[i][j] -= num
#           delRoom = max(delRoom, bfs(i,j))
#           s[i][j] += num
#         num = num * 2


# print(roomCnt)
# print(maxRoom)  
# print(delRoom)
# from collections import deque
# import sys
# input = sys.stdin.readline

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# n, m = map(int, input().split())
# castle = [list(map(int, input().split())) for _ in range(m)]
# visit = [[0] * n for _ in range(m)]

# def bfs(x,y):
#   q = deque()
#   q.append([x, y])
#   visit[x][y] = 1
#   room = 1
#   while q: 
#     x, y = q.popleft()
#     wall = 1
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if (castle[x][y] & wall) != wall :
#         if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
#           room += 1
#           visit[nx][ny] = 1

#           q.append([nx, ny])
#         wall = wall * 2
#   return room

# roomCnt = 0
# maxRoom = 0
# delRoom = 0

# for i in range(m):
#   for j in range(n):
#     if visit[i][j] == 0:
#       roomCnt += 1
#       maxRoom = max(maxRoom, bfs(i,j))


# for i in range(m):
#   for j in range(n):
#     num = 1
#     while num < 9:
#       if num & castle[i][j] :
#         visit = [[0] * n for _ in range(m)]
#         castle[i][j] -= num
#         delRoom= max(delRoom, bfs(i,j))
#         castle[i][j] += num

#       num *= 2


        # import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# castle = [list(map(int, input().split())) for _ in range(m)]

# visited = [[0] * n for _ in range(m)]

# def move (y, x, d, size) :
#   for dy, dx in d:
#     ny = y + dy
#     nx = x + dx
#     if 0 <= ny < m and 0 <= nx < n:
#       if castle[ny][nx] == 0:
#         size += dfs(ny, nx)
#   return size

# def dfs(y, x):
#   visited[y][x] = 1
#   c = castle[y][x]
#   size = 1
#   if c == 1:
#     d = [(-1, 0), (1, 0), (0, 1)]
#     size += move(y, x, d, size)
#   elif c == 6:
#     d = [(-1, 0),(0, -1)]
#     size += move(y, x, d, size)
#   elif c == 7:
#     d = [(-1, 0)]
#     size += move(y, x, d, size)
#   elif c == 8 :
#     d = [ (1, 0), (0, -1), (0, 1)]
#     size += move(y, x, d, size)
#   elif c == 10:
#     d = [ (0, -1), (0, 1)]
#     size+= move(y, x, d, size)
#   elif c == 12 :
#     d = [ (1, 0), (0, -1)]
#     size+= move(y, x, d, size)
#   elif c == 13:
#     d = [ (1, 0)]
#     size+=move(y, x, d, size)
#   elif c == 15:
#     return size
#   return size

# room = 0
# room_size = []
# for i in range(m):
#   for j in range(n):
#     if not visited[i][j]:
#       rs = dfs(i, j)
#       room_size.append(rs)
#       room += 1

# print(room)
# room_size.sort()
# print(room_size[-1])