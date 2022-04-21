import sys;input=sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
a,b,c = 0, 0,0
def dfs(x,y,n):
  global a,b,c
  check = board[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if (board[i][j] != check):
        for k in range(3):
          for l in range(3):
            dfs(x + k * n // 3, y + l * n //3, n//3)
        return
  if check == -1:
    a += 1
  elif check == 0:
    b += 1
  else: 
    c += 1
dfs(0,0,n)
print(a)
print(b)
print(c)