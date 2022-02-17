import sys
from collections import deque
maps= []
birds = []
r,c = map(int,sys.stdin.readline().split())
for y in range(r):
  arr = list(input().rstrip())
  maps.append(arr)
  for x in range(len(arr)):
    if arr[x] == 'L':
      birds.append((y,x))

time = [[0 for _ in range(c)] for _ in range(r)]

def melt_time_set(maps:list) -> int:
  visited = [[ False for _ in range(c)] for _ in range(r) ]
  dirs = [(0,1),(0,-1),(1,0),(-1,0)]
  q = deque()
  for y in range(len(maps)):
    for x in range(len(maps[0])):
      if maps[y][x]  == '.' or maps[y][x] == 'L':
        q.append((y, x))
        time[y][x] = 0
        visited[y][x] = True

  last_time = 0
  while q:
    y, x = q.popleft()
    for dy, dx in dirs:
      ny, nx = y + dy, x + dx
      if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != 'L':
        q.append((ny, nx))
        time[ny][nx] = time[y][x] + 1
        visited[ny][nx] = True
        last_time = time[ny][nx]
  return last_time

def bfs(start: tuple, maps: list, mid: int, end: tuple) -> bool :
  dirs = [(0,1),(0,-1),(1,0),(-1,0)]
  q = deque()
  q.append(start)
  visited = [[ False for _ in range(len(maps[0]))] for _ in range(len(maps)) ]
  while q:
    y, x = q.popleft( )
    for dy , dx in dirs:
      ny, nx = y + dy ,x + dx
      if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] :
        visited[ny][nx] = True
        if ny == end[0] and nx ==end[1]:
          return True
        if time[ny][nx] <= mid:
          q.append((ny, nx))
  return False

_min, _max = 0, melt_time_set(maps)

answer = _max
while _min <= _max:
  mid = (_min + _max) // 2

  if bfs(birds[0] , maps, mid , birds [ 1]) :
    answer =mid
    _max = mid - 1
  else:
    _min = mid + 1

print(answer)
        
        
        # from collections import deque
# import sys

# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs():
#     while q:
#         x, y = q.popleft()
#         if x == x2 and y == y2:
#             return 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if not c[nx][ny]:
#                     if a[nx][ny] == '.':
#                         q.append([nx, ny])
#                     else:
#                         q_temp.append([nx, ny])
#                     c[nx][ny] = 1
#     return 0

# def melt():
#     while wq:
#         x, y = wq.popleft()
#         if a[x][y] == 'X':
#             a[x][y] = '.'
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if not wc[nx][ny]:
#                     if a[nx][ny] == 'X':
#                         wq_temp.append([nx, ny])
#                     else:
#                         wq.append([nx, ny])
#                     wc[nx][ny] = 1

# m, n = map(int, input().split())
# c = [[0]*n for _ in range(m)]
# wc = [[0]*n for _ in range(m)]

# a, swan = [], []
# q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

# for i in range(m):
#     row = list(input().strip())
#     a.append(row)
#     for j, k in enumerate(row):
#         if a[i][j] == 'L':
#             swan.extend([i, j])
#             wq.append([i, j])
#         elif a[i][j] == '.':
#             wc[i][j] = 1
#             wq.append([i, j])

# x1, y1, x2, y2 = swan
# q.append([x1, y1])
# a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
# cnt = 0

# while True:
#     melt()
#     if bfs():
#         print(cnt)
#         break
#     q, wq = q_temp, wq_temp
#     q_temp, wq_temp = deque(), deque()
#     cnt += 1