import sys
input = sys.stdin.readline
r,c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)] 
visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1]
def solve (i, j):
  if j == c - 1:
    return True
  for d in dx:
    if 0 <= i + d < r and board[i+d][j+1] == '.' and not visited[i+d][j+1]:
      visited[i+d][j+1] = True
      if solve(i+d, j+1):
        return True
  return False
ans = 0
for i in range(r):
  if board[i][0] == '.':
    if solve(i, 0):
      ans += 1

print(ans)

