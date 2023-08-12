import sys
sys.setrecursionlimit(10**9)
input =sys.stdin.readline
r,c,k = map(int,input().split())
board = [input().rstrip() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
ans = 0

def dfs(y, x ,cnt) :
  global ans

  if y == 0 and x == c - 1 and cnt == k : 
    ans += 1
    return 
  
  for dy, dx in (1,0),(-1,0),(0,-1),(0,1) :
    ny , nx = dy + y , dx + x
    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'T' and visited[ny][nx] == 0:
      visited[ny][nx] = 1
      dfs(ny, nx, cnt + 1)
      visited[ny][nx] = 0

visited[r-1][0] = 1
dfs(r-1, 0, 1)

print(ans)