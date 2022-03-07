import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
before = [list(map(int,input().split()) ) for _ in range(n)]
after = [list(map(int, input().split()) ) for _ in range(n)]

def solution () :
  for y in range(n):
    for x in range(m):
      if before[y][x] != after[y][x]:
        bfs(y, x)
        return check_ans()
  return 'YES'


def bfs(cy, cx):
  global before
  visited = [[False] * m for _ in range(n)]
  temp = before[cy][cx]
  target = after[cy][cx]
  q = deque([(cy, cx)])
  visited[cy][cx] = True
  while q:
    y, x = q.popleft()
    before[y][x] = target
    for dy, dx in (1,0), (-1,0), (0,-1), (0, 1):
      ny, nx = y + dy, x + dx
      if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and before[ny][nx] == temp:
        q.append((ny, nx))
        visited[ny][nx] = True


def check_ans () :
  for y in range(n):
    for x in range(m):
      if before[y][x] != after[y][x]:
        return 'NO'
  return 'YES'

print(solution())
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]



# def bfs(x, y) : 
#   global before
#   visited = [[ False] * m for _ in range(n)]
#   q = deque([(x,y)])
#   visited[x][y] = True
#   target  = before[x][y]
#   num = after[x][y]

#   while q:
#     now_x, now_y = q.popleft()