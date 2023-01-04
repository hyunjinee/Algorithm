from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((sz ,sy, sx))

  visit[sz][sy][sx] = 1

  while q:
    z, y, x = q.popleft()
    for i in range(6):
      nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
      if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and visit[nz][ny][nx] == 0:
        if s[nz][ny][nx] == '.' or s[nz][ny][nx] == 'E':
          dp[nz][ny][nx] = dp[z][y][x] + 1
          visit[nz][ny][nx] = 1
          q.append((nz, ny, nx))


while True: 
  l, r, c = map(int, input().split())

  if l == 0:
    break

  s = [[] for _ in range(l)]
  dp = [[[0] * c for i in range(r)] for i in range(l)]
  visit = [[[0] * c for i in range(r)] for i in range(l)]

  for i in range(l):
    for j in range(r):
      s[i].append(list(map(str, input())))
    input()

  for i in range(l):
    for j in range(r):
      for k in range(c):
        if s[i][j][k] == 'S':
          sx, sy, sz = k, j, i
        if s[i][j][k] == 'E':
          ex, ey, ez = k, j, i

  bfs()

  if dp [ez][ey][ex] == 0:
    print("Trapped!")
  else:
    print("Escaped in %d minute(s)." % dp[ez][ey][ex])