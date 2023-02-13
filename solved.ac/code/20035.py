import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
board = [[0] * m for _ in range(n)]
for i in range(n):
  for j in range(m): 
    board[i][j] = a[i] * (10 ** 9) + b[j]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

def bfs(y, x, w):
  global ans 
  q = deque()
  q.append((y, x, w))
  visited[y][x] = True

  while q:
    cy, cx, w = q.popleft()
    ans  = max(w, ans)
    for dy , dx in (1, 0), (0, 1) :
      ny = cy + dy
      nx = cx + dx

      if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
        visited[ny][nx] = True
        new_w = w + board[ny][nx]
        q.append((ny, nx, new_w))
  print(ans)
  return ans

bfs(0,0,board[0][0])

# def dfs(y, x, cnt):

#   if y == n -1 and x == m -1  :
#     print(cnt)
#     return 

#   if not visited[y][x] :
#     visited[y + 1][x] = True
#     dfs(y+1, x, cnt + board[y+1][x])
#     visited[y+1][x] = False
#     visited[y][x+1] = True
#     dfs(y, x+ 1, cnt + board[y][x+1])
#     visited[y][x+1] = False

# dfs(0, 0, board[0][0])



