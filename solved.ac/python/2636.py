import sys
input= sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs ():
  visited = [[False] * m for _ in range(n)]
  q=deque()
  q.append([0,0])
  visited[0][0] = True
  cnt = 0
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y+dy[i]
      nx = x+dx[i]

      if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] :
        if board[ny][nx] == 0:
          visited[ny][nx] = True
          q.append([ny,nx])
        elif board[ny][nx] == 1:
          board[ny][nx] = 0
          cnt += 1
          visited[ny][nx] = True

  cheese.append(cnt)
  return cnt
cheese = []
time = 0
while True:
  time += 1
  cnt = bfs()
  if cnt == 0:
    break

print(time - 1)
print(cheese[-2])