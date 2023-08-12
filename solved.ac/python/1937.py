import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
panda = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for i in range(n)]
result = 0
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(y, x):
  if dp[y][x] : return dp[y][x]
  dp[y][x] = 1
  for dy, dx in d:
    ny,nx = y+dy, x+dx
    if 0 <= ny < n and 0 <= nx < n:
      if panda[y][x] < panda[ny][nx]:
        dp[y][x] = max(dp[y][x], dfs(ny,nx) + 1)
  return dp[y][x]
for i in range(n):
  for j in range(n):
    result = max(result, dfs(i,j))
print(result)

# def bfs(y, x):
#   global cnt
#   q = deque()
#   visited = [[False] * n for _ in range(n)]
#   q.append((y, x, panda[y][x]))
#   visited[y][x] = True
#   while q:
#     a, b, w = q.popleft()
#     for dy, dx in d:
#       ny,nx = a+dy,b+dx
#       if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and panda[ny][nx] > w:
#         q.append((ny,nx,panda[ny][nx]))
#         visited[ny][nx] = True
#         cnt += 1
#   print(cnt, "cnt")
#   return cnt
# cnt = 1
# ans = 0
# for i in range(n):
#   for j in range(n):
#     temp = bfs(i,j)
#     ans = max(ans, temp)    
#     cnt = 1

# print(ans)