"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 바닥 장식
description : graph, dfs
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

b = [list(input()) for _ in range(n)]

d = [(0, 1), (0, -1), ]
d1 = [(1, 0), (-1, 0)]
def dfs (y, x, k) :
  b[y][x] = 'x'
  if k == '-':
    for dy, dx in d:
      ny = y + dy
      nx = x + dx
      if 0 <= ny < n and 0 <= nx < m and b[ny][nx] == '-':
        dfs(ny, nx, k)
  elif k== '|':
    for dy, dx in d1:
      ny = y + dy
      nx = x + dx
      if 0 <= ny < n and 0 <= nx < m and b[ny][nx] == '|':
        dfs(ny, nx, k)
ans = 0

for i in range(n):
  for j in range(m):
    if b[i][j] == '-' or b[i][j] == '|':
      dfs(i, j , b[i][j])
      ans += 1

print(ans)