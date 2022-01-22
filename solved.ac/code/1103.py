import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))
 
visited = [[False]*M for _ in range(N)]
dp = [[0]*M for _ in range(N)]
 
result = 0
def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x+int(arr[x][y])*dx[i]
        ny = y+int(arr[x][y])*dy[i]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "H" and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False
 
dfs(0, 0, 0)
print(result+1)
# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# board = [input() for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# memo = [[-1] * m for _ in range(n)]
# state = False

# def dfs(i,j):
#   global state
#   if not (0 <= i <= n-1 and 0<=j <= m-1) or board[i][j] == 'H':
#     return 0
#   if visited[i][j]:
#     state = True
#     return -1
#   if memo[i][j] != -1:
#     return memo[i][j]
#   visited[i][j] = True

#   for a in range(4):
#     memo[i][j] = max(memo[i][j], )

