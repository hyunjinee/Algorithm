dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
candi = (('-', '+', '3', '4'), ('|', '+', '2', '3'), ('-', '+', '1', '2'), ('|', '+', '1', '4'))
R, C = map(int, input().split())
board = [input() for _ in range(R)]
def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C
def is_ans(y, x):
    chk = [False] * 4
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx] in (candi[k] or ('M', 'Z')):
            chk[k] = True
    cnt = chk.count(True)
    if cnt == 0:
        return 0
    elif cnt == 4:
        return '+'
    elif chk[0] and chk[2]:
        return '-'
    elif chk[1] and chk[3]:
        return '|'
    elif chk[0] and chk[1]:
        return '1'
    elif chk[1] and chk[2]:
        return '4'
    elif chk[2] and chk[3]:
        return '3'
    else:
        return '2'
for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            ans = is_ans(i, j)
            if ans:
                print(i + 1, j + 1, ans)
                exit()

# ch = ['.','|','-','+','1','2','3','4','M','Z']
# dir = [[0,1],[0,-1],[1,0],[-1,0]]
# pipe = [[],[2,3],[0,1],[0,1,2,3],[0,2],[0,3],[1,3],[1,2],[],[]]

# r,c=map(int,input().split())
# arr=[input() for i in range(r)]

# visit=[[0]*c for i in range(r)]
# for i in range(r):
#     for j in range(c):
#         p = ch.index(arr[i][j])
#         for d in pipe[p]:
#             ni,nj = i + dir[d][0], j + dir[d][1]
#             if ni > -1 and ni < r and nj > -1 and nj < c:
#                 visit[ni][nj] |= 1<<d

# res = [0,0,0,'-',0,'3','2','+',0,'4','1','+','|','+','+','+']
# for i in range(r):
#     for j in range(c):
#         if arr[i][j]=='.':            
#             if res[visit[i][j]]: print(i+1,j+1,res[visit[i][j]])

# # import sys
# # from collections import deque
# # input = sys.stdin.readline

# # r,c =map(int,input().split())
# # europe = [list(input().rstrip()) for _ in range(r)]
# # def find_start():
# #   for i in range(r):
# #     for j in range(c):
# #       if europe[i][j] == 'M':
# #         return (i, j)


# # start = find_start()
# # dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# # def bfs(dirs):
# #   q = deque([start, dirs])
# #   while q:
# #     now_y, now_x, dirs = q.popleft()
# #     for dy, dx in dirs:
# #       ny, nx = now_y + dy, now_x + dx
# #       if 0 <= ny < r and 0 <= nx < c:
# #         if europe[ny][nx] == '.':
# #           continue
# #         if europe[ny][nx] == '-':
# #           q.append([ny, nx, [(0,1), (0,-1)]])
# #         elif europe[ny][nx] == '|':
# #           q.append([ny, nx ,[(1,0), (-1,0)]])
# #         elif e
        