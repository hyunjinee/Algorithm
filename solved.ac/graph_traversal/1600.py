import sys; input = sys.stdin.readline
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
  q = deque()
  q.append((0, 0, k))

  visit = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]
  while q: 
    x, y, z = q.popleft()
    if x == h - 1 and y == w - 1: return visit[x][y][z]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z] == 0:
        visit[nx][ny][z] = visit[x][y][z] + 1
        q.append((nx, ny, z))
      
    if z > 0:
      for i in range(8):
        nx = x + d1[i]
        ny = y + d2[i]
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z - 1] == 0:
          visit[nx][ny][z - 1] = visit[x][y][z] + 1
          q.append((nx, ny, z- 1))

  return -1

k = int(input())
w, h = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(h)]
print(bfs())