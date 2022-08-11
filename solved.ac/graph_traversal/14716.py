import sys; input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

board = [ list(map(int,input().split()))  for i in range(m)]
visit = [[0]*n for _ in range(m)]

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

answer = 0

def bfs(x, y): 
  q = deque()
  q.append((x, y))

  while q:
    x,y = q.popleft()
    visit[x][y] = 1
    board[x][y] = 0

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<m and 0<=ny<n and board[nx][ny] == 1 and visit[nx][ny] == 0:
        q.append((nx,ny))
        visit[nx][ny] = 1

for i in range(m):
  for j in range(n):
    if board[i][j] == 1 :
      bfs(i ,j )
      answer += 1
print(answer)
