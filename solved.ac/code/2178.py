import sys
from collections import deque
input = sys.stdin.readline



n,m = map(int, input().split())
board = [list(map(int,input().rstrip()) )for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs():
  q = deque()
  q.append((0,0))
  visited[0][0] = True
  direction = [(1,0),(-1,0),(0,1),(0,-1)]

  while q:
    y, x =  q.popleft()
    for dy, dx in direction:
      ny, nx = y+dy, x+dx
      if 0<=ny<n and 0<=nx<m:
        if board[ny][nx] == 1 and not visited[ny][nx]:
          board[ny][nx] = board[y][x] + 1
          q.append((ny,nx))

bfs()

print(board[n-1][m-1])