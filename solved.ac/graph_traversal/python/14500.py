N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
visited = [[0]*M for _ in range(N)]
max_value = max(map(max,board))
def dfs(x,y,dep,_sum):
    global ans
    if dep == 4:
        ans = max(ans,_sum)
        return
    if ans > _sum + max_value*(4-dep):
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = 1
            if dep == 2:
                dfs(x,y,dep+1,_sum+board[nx][ny])
            dfs(nx,ny,dep+1,_sum+board[nx][ny])
            visited[nx][ny] = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0
print(ans)

# import sys; input = sys.stdin.readline

# def dfs(r, c, idx, total):
#     global ans
#     if ans >= total + max_val * (3 - idx):
#         return
#     if idx == 3:
#         ans = max(ans, total)
#         return
#     else:
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
#                 if idx == 1:
#                     visit[nr][nc] = 1
#                     dfs(r, c, idx + 1, total + arr[nr][nc])
#                     visit[nr][nc] = 0
#                 visit[nr][nc] = 1
#                 dfs(nr, nc, idx + 1, total + arr[nr][nc])
#                 visit[nr][nc] = 0


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visit = [([0] * M) for _ in range(N)]
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# ans = 0
# max_val = max(map(max, arr))

# for r in range(N):
#     for c in range(M):
#         visit[r][c] = 1
#         dfs(r, c, 0, arr[r][c])
#         visit[r][c] = 0

# print(ans)

# # import sys
# # input = sys.stdin.readline
# # n, m = map(int,input().split())
# # arr = [list(map(int,input().split())) for _ in range(n)]
# # visited = [[0] * m for _ in range(n)]
# # dr = [-1,0,1,0]
# # dc = [0,1,0,-1]
# # ans = 0 
# # max_val = max(map(max, arr)) 
# # def dfs(r,c,idx, total):
# #   global ans
# #   if ans >= total + max_val * (3 - idx):
# #     return 
# #   if idx == 3:
# #     ans = max(ans, total)
# #   else: 
# #     for i in range(4):
# #       nr = r + dr[i]
# #       nc = c + dc[i]
# #       if 0 <=nr < n and 0 <= nc < n and visited[nr][nc] == 0:
# #         if idx == 1:
# #           visited[nr][nc] = 1
# #           dfs(r, c, idx+ 1, total + arr[nr][nc])
# #           visited[nr][nc] = 0
# #         visited[nr][nc] = 1
# #         dfs(nr, nc, idx + 1, total + arr[nr][nc])
# #         visited[nr][nc] = 0

# # for r in range(n):
# #   for c in range(n):
# #     visited[r][c] = 1
# #     dfs(r,c,0,arr[r][c])
# #     visited[r][c] = 0
# # print(ans)