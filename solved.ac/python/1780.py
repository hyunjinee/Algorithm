import sys
input = sys.stdin.readline
n = int( input())
paper = [list(map(int, input().split())) for _ in range(n)]
d = [(0,1), (0,-1), (1,0), (-1,0)]

# 내 생각엔 체크와 탐색을 구분해서 하는게 좋을 것 같다.
def check(p):
  keep = p[0][0]
  for i in range(len(p)):
    for j in range(len(p)):
      if p[i][j] != keep:
        return False

  return True

while True:
  if check(paper):
    

# def dfs(y, x, k):
#   for dy, dx in d: 
#     ny, nx = y+dy, x+dx

#     if 0 <= ny < n and 0 <= nx < n:
#       if paper[ny][nx] == k:
#         paper[ny][nx] = 2
#         dfs(ny, nx, k)

# for i in range(n):
#     for j in range(n):
#         if paper[i][j] == 0 or 1 or -1:
#           keep = paper[i][j]
#           paper[i][j] = 2
#           dfs(i,j,keep)

  