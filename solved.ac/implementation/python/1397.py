import sys; input = sys.stdin.readline

n = int(input())
s = input().rstrip()

dy = (-1,0,1,0)
dx = (0,1,0,-1)

v = [['#' for __ in range(101)] for _ in range(101)]
y, x, d = 50, 50, 2

ey = ex = sy = sx = 50
v[y][x] = '.'

for ch in s:
  if ch == 'L': d = (d + 3) % 4
  elif ch == 'R': d = (d + 1) % 4
  else: 
    y, x = y + dy[d], x + dx[d]
    v[y][x] = '.'
    sy, ey, sx, ex = min(sy, y), max(ey, y), min(sx, x), max(ex, x)

for i in range(sy, ey + 1): print(''.join(v[i][sx : ex + 1]))