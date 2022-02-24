import sys
from collections import deque
input =sys.stdin.readline
n =int(input())
board = [list(map(int,input().split())) for _ in range(n)]
_min,_max = min(map(min,board)), max(map(max,board))
left, right = 0, _max - _min
def bfs(_min, _max):
  if board[0][0] < _min or board[0][0] > _max:
    return False
  if board[n-1][n-1] < _min or board[n-1][n-1] > _max:
    return False
  visited = [[0]*n for _ in range(n)]
  visited[0][0] = 1
  q = deque([(0,0)])
  while q:
    r,c = q.popleft()
    if (r, c) == (n-1, n-1):
      return True
    for nr,nc in ((r-1,c), (r,c+1), (r+1,c), (r, c-1)) :
      if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
        if _min <= board[nr][nc] <= _max:
          visited[nr][nc] = 1
          q.append((nr,nc))
  return False

while left <= right :
  mid = (left + right) // 2
  state = False
  for i in range(_min, _max+1):
    if bfs(i, i+mid):
      state = True
      break
  if state: 
    right = mid - 1
  else: 
    left =mid +1
print(left)






# import sys
# sys.setrecursionlimit(100000)
# N= int(input())
# mp=[]
# for i in range(N):
#     mp.append(list(map(int,input().split())))

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]

# def dfs(x,y,s,e):
#     vi[y][x]=1
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<N and 0<=ny<N and s<=mp[ny][nx]<=e and vi[ny][nx]==0:
#             dfs(nx,ny,s,e)
# s=0
# ch=0
# e=max(mp[0][0],mp[N-1][N-1])
# m=min(mp[0][0],mp[N-1][N-1])
# while e<=200 and s<=m:
#     vi = [[0] * N for _ in range(N)]
#     dfs(0,0,s,e)
#     if vi[N-1][N-1]:
#         s+=1
#         ch=1
#     elif ch:
#         e+=1
#         s+=1
#     else:
#         e+=1
# print(e-s+1)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# n = int(input())
# board = [list(map(int,input().split())) for _ in range(n)]
# start = [board[0][0]]
# visited =[[False] * n for _ in range(n)]

# answer = sys.maxsize
# def dfs(y, x, love):
#   global answer
#   if y == n-1 and x == n-1:
#     answer = min(answer, max(love) - min(love))
#     return

#   for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
#     ny, nx = y+dy, x+dx
#     if 0 <= ny < n and 0 <= nx < n:
#       if not visited[ny][nx]:
#         visited[ny][nx] = True
#         dfs(ny, nx, love + [board[ny][nx]])
#         visited[ny][nx] = False
  

# dfs(0, 0, start)

# print(answer)