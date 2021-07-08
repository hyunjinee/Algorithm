# import sys 
# input = sys.stdin.readline
# t = int(input())

# def dfs(baechu, x, y):
#     baechu[y][x] = 0 
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     for i in range(4):
#         if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n:

#             x = x + dx[i]
#             y = y + dy[i]
#             if baechu[y][x] == 1: 
#                 dfs(baechu, x, y )     
# for i in range(t):
#     m, n, k = map(int, input().split())
#     jilunge = 0
#     baechu = [ [0] * m for _ in range(n)]
#     for j in range(k):
#         x, y = map(int ,input().split())
#         baechu[y][x] =  1
#     for k in range(n):
#         for l in range(m):
#             if baechu[k][l] == 1:
#                 dfs(baechu, l, k)
#                 jilunge += 1

# print(jilunge)
# print(baechu)
        

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1, -1, 0, 0 ]
    dy = [0 , 0 ,1 , -1] 


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny< M):

            if matrix[nx][ny] == 1:
                matrix[nx][ny] == -1
                dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())
    matrix = [[0] *M for _ in range(N)]
    cnt =0 

    for _ in range(K):
        m, n = map(int, input().split())
        matrix[n][m] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)

