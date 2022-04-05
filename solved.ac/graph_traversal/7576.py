import sys;input=sys.stdin.readline
from collections import deque
m,n=map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
q = deque([])
dx,dy = [0,0,1,-1],[1,-1,0,0]
ans = 0
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      q.append([i,j])

def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx,ny = dx[i] + x, dy[i] +y
      if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y] + 1
        q.append([nx,ny])
bfs()
for i in tomato:
  for j in i:
    if j ==0 :
      print(-1)
      exit()
  ans = max(ans, max(i))

print(ans - 1)