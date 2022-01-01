import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize



def bfs(y,x):
  global count
  q = deque([(y,x)])
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  visited[y][x] = True
  board[y][x] = count
  while q:
    y, x = q.popleft()
    for dy,dx in d:
      if 0<= dy + y < n and 0 <= dx +x < n and not visited[dy+y][dx+x] and board[dy+y][dx+x] == 1:
        q.append((y+dy, x+dx))
        visited[dy+y][dx+x] = True
        board[dy+y][dx+x] = count

def bfs2(z):
  global answer
  dist = [[-1] * n for _ in range(n)]
  q = deque()
  for i in range(n):
    for j in range(n):
      if board[i][j] == z:
        q.append((i,j))
        dist[i][j] = 0
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  while q:
    y, x = q.popleft()
    for dy,dx in d:
      ny = y + dy
      nx = x + dx
      if nx < 0 or nx>=n or ny < 0 or ny>=n:
        continue

      if board[ny][nx] > 0 and board[ny][nx] != z:
        answer = min(answer, dist[y][x])
        return 

      if board[ny][nx] == 0  and dist[ny][nx] == -1:
        dist[ny][nx ] = dist[y][x] + 1
        q.append((ny,nx))


for i in range(n):
  for j in range(n):
    if board[i][j] == 1 and not visited[i][j]:
      bfs(i,j)
      count += 1

for i in range(1, count):
  bfs2(i)

print(answer)