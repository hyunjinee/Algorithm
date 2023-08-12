from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x + dx[i], y + dy[i]
            while True:
                ## 범위를 벗어난다
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                ## 벽을 만난다
                if board[nx][ny] == "*":
                    break
                ## 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                ## board업데이트, queue 추가
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]
            # print(visited)


if __name__ == "__main__":
    ## 입력값
    m, n = map(int, input().split())
    board = [input() for _ in range(n)]

    ## 동 남 서 북
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    ## C위치
    C = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == "C":
                C.append((i, j))
    ## sx,sy : 시작지점
    ## ex,ey : 도착지점
    (sx, sy), (ex, ey) = C

    visited = [[float("inf")] * m for _ in range(n)]
    bfs(sx, sy)

    print(visited[ex][ey] - 1)


# import sys
# from collections import deque
# input = sys.stdin.readline

# w, h = map(int,input().split())

# board = [input().rstrip() for _ in range(h)]

# print(board)

# lazer = 0

# start =[]
# for i in range(h):
#   for j in range(w):
#     if board[i][j] == 'C':
#       start.append((i,j))


# visited = [[sys.maxsize] * w for _ in range(h)]


# def bfs(y,x):
#   queue =deque([(y,x)])
#   visited[y][x] = 0
#   d = [(0,1),(1,0),(-1,0),(0,-1)]
#   while queue:
#     dy, dx = queue.popleft()
#     for a, b in  d:
#       ny, nx = dy + a, dx + b

#       while True:
#         if not (0 <= nx < w and 0 <= ny < h):
#           break
#         if board[ny][nx] == '*':
#           break
#         if visited[ny][nx] < visited[y][x] + 1:
#           break
#         queue.append((ny, nx))

#         visited[ny][nx] = visited[y][x] + 1
#         ny = ny + a
#         nx = nx + b
#       # print(visited)

# bfs(start[0][0], start[0][1])
# print(visited[start[1][0]][start[1][1]] - 1)


# # def dfs(y,x):
# #   pass

# # dfs(start[0], start[1])


# # def bfs(y,x):
# #   visited = [[False] * w for _ in range(h)]
# #   q = deque()
# #   q.append((y,x))
# #   d = [(0,1), (0,-1), (1,0), (-1,0)]
# #   while q:
# #     dy, dx = q.popleft()

  
# #   pass

# # bfs(start[0], start[1])