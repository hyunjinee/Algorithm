import sys
sys.setrecursionlimit(10**9)
input =sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
_min, _max = min(map(min, board)), max(map(max, board))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
i = 0 
def dfs(x,y,i):
  if x < 0 or x >= n or y < 0 or y >= n:
        return False
  if board[x][y] > i and not visited[x][y]:
    visited[x][y] = True
    for k in range(4):
      dfs(x+dx[k], y+dy[k], i)
    return True
while i <= _max:
  cnt = 0 
  visited = [[0] * n for _ in range(n)]
  for x in range(n):
    for y in range(n):
      if not visited[x][y] and dfs(x,y,i):
        cnt += 1
  ans = max(ans, cnt)
  i+=1
print(ans)