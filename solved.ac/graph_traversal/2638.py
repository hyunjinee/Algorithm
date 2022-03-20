import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
ans = 0
while True:
  q = deque()
  visited = [[0 for _ in range(m)] for _ in range(n)]
  visited[0][0] = 1
  q.append([0,0])
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx, ny = x + dx[k], y + dy[k]
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        if board[nx][ny]:
          board[nx][ny] += 1
        else:
          visited[nx][ny] = 1
          q.append([nx, ny])
  flag = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] >= 3:
        board[i][j] = 0
      elif 0 < board[i][j]:
        flag = 1
        board[i][j] = 1
  ans += 1

  if not flag:
    print(ans)
    break