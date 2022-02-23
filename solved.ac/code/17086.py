import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n,m=map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(s)
ans = 0
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
def dfs (y, x, count) :
  global ans
  if s[y][x] == 1:
    ans = max(ans, count)
    return 
  for dy ,dx in d :
    ny, nx = y+dy, x+dx
    if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 :
      visited[ny][nx] = 1
      dfs(ny,nx,count+1)
      visited[ny][nx] = 0


for i in range(n):
  for j in range(m):
    if s[i][j] == 0: 
      visited[i][j] = 1
      dfs(i,j,0)
      visited[i][j] = 0
    
print(ans)