import sys, collections

def bfs(start) :
    queue = collections.deque([(start, 0)])
    visit = [[False for _ in range(m)] for _ in range(n)]
    visit[start[0]][start[1]] = True
    while queue :
        node, depth = queue.popleft()
        for win in window :
            x = node[0] + win[0]
            y = node[1] + win[1]
            if 0 <= x < n and 0 <= y < m and a[x][y] == 'L' and not visit[x][y] :
                visit[x][y] = True
                queue.append(((x,y), depth+1))
    return depth

n, m = map(int, input().split())
a = [sys.stdin.readline() for _ in range(n)]

ans = 0
window = [(-1,0), (1,0), (0,-1), (0,1)]
for i in range(n) :
    for j in range(m) :
        if a[i][j] == 'L' :
            tmp = 0
            for win in window :
                x = i + win[0]
                y = j + win[1]
                if 0 <= x < n and 0 <= y < m and a[x][y] == 'L' :
                    tmp += 1
            if tmp > 2 : 
                continue
            ans = max(ans, bfs((i,j)))
print(ans)

# import sys
# from collections import deque
# dx = [-1,0,0,1]
# dy = [0,-1,1,0]

# def bfs(array, x, y):
#     visited = [ [False]*(m+2) for _ in range(n+2) ]
#     queue = deque([(x,y,0)])
#     visited[x][y] = True
#     while queue:
#         x, y, cnt = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if array[nx][ny] == -1 or visited[nx][ny]:
#                 continue
#             queue.append((nx,ny, cnt+1))
#             visited[nx][ny] = True
#     return cnt

# n, m = map(int, sys.stdin.readline().split(' '))
# array = [ [-1]*(m+2) for _ in range(n+2) ]
# temp = []
# for _ in range(n):
#     temp.append(list(sys.stdin.readline().rstrip()))
# wlDict = {'W':-1, 'L':0}
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         array[i][j] = wlDict[temp[i-1][j-1]]

# result = 0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if array[i][j-1] == 0 and array[i][j+1] == 0:
#             continue
#         elif array[i-1][j] == 0 and array[i+1][j] == 0:
#             continue
#         elif array[i][j] == 0:
#             result = max(result, bfs(array,i,j))
# print(result)

# # from collections import deque
# # import sys


# # def BFS(Q, visited):
# #     (i, j, d) = Q[0]
# #     visited[i][j] = 1
# #     while Q:
# #         i, j, d = Q.popleft()
# #         for (new_i, new_j) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
# #             if 0 <= new_i < V and 0 <= new_j < H and MAP[new_i][new_j] == 'L' and not visited[new_i][new_j]:
# #                 Q.append((new_i, new_j, d+1))
# #                 visited[new_i][new_j] = 1
# #     return d


# # V, H = map(int, sys.stdin.readline().split())
# # MAP = []
# # # for _ in range(V):
# #     MAP.append(sys.stdin.readline())
# # max_dist = 0
# # for i in range(V):
# #     gap = 0
# #     for j in range(H):
# #         if gap:
# #             gap -= 1
# #             continue
# #         if MAP[i][j] == 'L':
# #             dist = BFS(deque([(i, j, 0)]), [[0] * H for _ in range(V)])
# #             if dist > max_dist:
# #                 max_dist = dist
# #             else:
# #                 gap = max_dist - dist

# # print(max_dist)

# # # import sys
# # # from collections import deque

# # # def bfs(i,j):
# # #     global l,w,res
# # #     b = [a[e][:] for e in range(l)]
# # #     b[i][j] = 'W'
# # #     q = deque([[i,j,0]])
# # #     while q:
# # #         x,y,n = q.popleft()
# # #         for k in range(4):
# # #             if 0<=x+dx[k]<l and 0<=y+dy[k]<w and b[x+dx[k]][y+dy[k]]=='L':
# # #                 b[x+dx[k]][y+dy[k]] = 'W'
# # #                 q.append([x+dx[k],y+dy[k],n+1])
# # #     if res<n:
# # #         res = n

# # # def nwse(i,j):
# # #     if (i==0 or i==l-1) or (j==0 or j==w-1):
# # #         return True
# # #     if (a[i+1][j]=='L' and a[i-1][j]=='L') or (a[i][j+1]=='L' and a[i][j-1]=='L'):
# # #         return False
# # #     return True

# # # l,w = map(int,input().split())
# # # a = [list(sys.stdin.readline().strip()) for _ in range(l)]
# # # res = 0
# # # dx = [0,0,1,-1]
# # # dy = [1,-1,0,0]
# # # for i in range(l):
# # #     for j in range(w):
# # #         if a[i][j] == 'L':
# # #             if nwse(i,j):
# # #                 bfs(i,j)
# # # print(res)
# # # # from sys import stdin, stdout
# # # # from collections import deque
# # # # N, M = map(int, stdin.readline().split())
# # # # maps = []
# # # # for _ in range(N):
# # # #     maps.append(list(map(lambda x:0 if x == "W" else 1,stdin.readline().rstrip("\n"))))
# # # # max_distance = 0
# # # # def get_distance(y, x, visited):
# # # #     queue = deque([])
# # # #     queue.append((0, y, x))
# # # #     cost = 0
# # # #     while queue:
# # # #         cost, y, x = queue.popleft()
# # # #         for my, mx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
# # # #             ny, nx = y + my, x + mx
# # # #             if not (0 <= ny < N and 0 <= nx <M):
# # # #                 continue
# # # #             # If 'Land' then 'Move'
# # # #             if maps[ny][nx] == 1 and not visited[ny][nx]:
# # # #                 visited[ny][nx] = True
# # # #                 queue.append((cost + 1, ny, nx))
# # # #     return cost
# # # # def get_greedy_land_pos():
# # # #     lands = []
# # # #     for y in range(N):
# # # #         for x in range(M):
# # # #             cnt = 0
# # # #             for my, mx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
# # # #                 ny, nx = y + my, x + mx
# # # #                 if not (0 <= ny < N and 0 <= nx <M):
# # # #                     continue
# # # #                 # Land가 아니면
# # # #                 if maps[ny][nx] != 1:
# # # #                     continue
# # # #                 cnt += 1
# # # #                 if cnt > 2:
# # # #                     break
# # # #             if cnt <= 2 and maps[y][x] == 1:
# # # #                 lands.append((y, x))
# # # #     return lands
# # # # lands = get_greedy_land_pos()
# # # # print(lands, 'wow')
# # # # for y, x in lands:
# # # #     visited = [[False] * M for _ in range(N)]
# # # #     visited[y][x] = True
# # # #     dist = get_distance(y, x, visited)
# # # #     if dist > max_distance:
# # # #         max_distance = dist
# # # # stdout.write(f"{max_distance}")


# # # # from collections import deque

# # # # n,m=map(int, input().split())
# # # # maps=[]
# # # # for i in range(n):
# # # #   maps.append(list(input()))

# # # # dx=[1,-1,0,0]
# # # # dy=[0,0,1,-1]

# # # # def bfs(i,j):
# # # #   queue=deque()
# # # #   queue.append((i,j))
# # # #   visited=[[0]*m for _ in range(n)]
# # # #   visited[i][j]=1
# # # #   cnt=0
# # # #   while queue:
# # # #     x,y=queue.popleft()
# # # #     for i in range(4):
# # # #       nx=x+dx[i]
# # # #       ny=y+dy[i]
# # # #       if nx<0 or nx>=n or ny<0 or ny>=m:
# # # #         continue
# # # #       elif maps[nx][ny]=='L' and visited[nx][ny]==0:
# # # #         visited[nx][ny]=visited[x][y]+1
# # # #         cnt=max(cnt,visited[nx][ny])
# # # #         queue.append((nx,ny))
# # # #   return cnt-1

# # # # result=0
# # # # for i in range(n):
# # # #   for j in range(m):
# # # #     if maps[i][j]=='L':
# # # #       result=max(result,bfs(i,j))

# # # # print(result)

# # # # import sys
# # # # from collections import deque

# # # # input = sys.stdin.readline

# # # # h, w = map(int, input().split())
# # # # arr = [list(map(str, input())) for _ in range(h)]

# # # # answer = 0
# # # # dx = [-1, 0, 0, 1]
# # # # dy = [0, -1, 1, 0]

# # # # for i in range(h):
# # # #     for j in range(w):
# # # #         if arr[i][j] == 'W':
# # # #             continue
# # # #         vis = [[False] * w for _ in range(h)]
# # # #         q = deque()
# # # #         q.append([i, j, 0])
# # # #         vis[i][j] = True
# # # #         while q:
# # # #             x, y, value = q.popleft()
# # # #             answer = max(answer, value)
# # # #             for k in range(4):
# # # #                 nx = x + dx[k]
# # # #                 ny = y + dy[k]
# # # #                 if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 'L' and not vis[nx][ny]:
# # # #                     q.append([nx, ny, value + 1])
# # # #                     vis[nx][ny] = True
# # # # print(answer)
# # # # # import sys
# # # # # input = sys.stdin.readline

# # # # # n,m = map(int, input().split())

# # # # # board = [list(input().rstrip()) for _ in range(n)]
# # # # # visited = [[False] * m for _ in range(n)]


# # # # # ans = sys.maxsize
# # # # # count = 0
# # # # # d = [(0,1),(0,-1),(1,0),(-1,0)]
# # # # # def dfs( y, x) :
# # # # #   global count
# # # # #   for dy,dx in d:
# # # # #     ny = dy + y
# # # # #     nx = dx + x
# # # # #     if 0 <= ny < n and 0<=nx < m and not visited[ny][nx] and board[ny][nx] == 'L':
# # # # #       visited[ny][nx] = True
# # # # #       count += 1
# # # # #       dfs(ny,nx)




# # # # # for i in range(n):
# # # # #   for j in range(m):
# # # # #     if board[i][j] == 'L' and visited[i][j] == False:
      
# # # # #       visited[i][j] = True
# # # # #       dfs(i,j)
# # # # #       visited[i][j] = False
# # # # #       ans = min(ans, count)
# # # # #       count = 0


# # # # # print(ans)