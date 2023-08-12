import sys
from collections import deque
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(8)]
dy = [0, 1, 1, -1, -1, 0, 0, 1, -1]
dx = [0, 1, -1, 1, -1, 1, -1, 0, 0]
def bfs():
  q = deque([(7, 0 )])
  while q:
    c = len(q)
    visited = [[False] * 8 for i in range(8)]
    for _ in range(c):
      y, x = q.popleft()
      if board[y][x] == '#':
        continue
      if y == 0 and x == 7:
        return 1
      for i in range(9):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < 8 and 0 <= nx < 8:
          if board[ny][nx] == '.' and not visited[ny][nx]:
            visited[ny][nx] = True
            q.append((ny, nx))
      board.pop()
      board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

  print(0)

print(bfs())

# import sys
# sys.setrecursionlimit(10*9)
# input = sys.stdin.readline
# board = [list(input().rstrip()) for _ in range(8)]

# dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

# def dfs(y,x, board, visit):
#   if y == 0 and x == 7:
#     print(1)
#     exit()
#   visit[y][x] = True
#   next_board = calculate_next_board(board)
#   for dy, dx in dirs:
#     ny, nx = y + dy, x + dx
#     if 0 <= ny < 8 and 0 <= nx < 8 and board[ny][nx] == '.':
#       visit[ny][nx] = True
#       dfs(ny, nx, next_board, visit)
#       visit[ny][nx] = False

# def calculate_next_board(b):
#   # print(board, "bbb")
#   b.pop()
#   b.insert(0, ['.'] * 8)
#   return b
# visited = [[False] * 8 for _ in range(8)]
# dfs(7, 0, board, visited)
# print(0)
# from collections import deque
# board = [list(input()) for i in range(8)]

#     board.pop()
#     board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

#   return 0

# print(bfs())

# board = [list(input().rstrip()) for _ in range(8)]

# def move (board):
#   n = 8
#   stack = [(n-1, 0, 0)]
#   while stack:
#     y,x,level = stack.pop()
#     if y < level: return 1
#     for i in [0, 1, -1]:
#       for j in [0, -1, 1]:
#         if 0 <= y + i < n and 0 <= x + j < n and board[y+i-level][x+j] == '.':
#           if board[y+i-level][x+j] == '.':
#             stack.append((y+1, x+j, level+1))
#   return 0



# def move(board):
#     n = 8
#     stack = [(n-1, 0, 0)]
#     while stack:
#         y, x, level = stack.pop()
#         if y<level : return 1
#         for i in [0, 1, -1]:
#             for j in [0, -1, 1]:
#                 if 0<=y+i<n and 0<=x+j<n and board[y+i-level][x+j]=='.':
#                     if board[y+i-level-1][x+j]=='.':
#                         stack.append((y+i, x+j, level+1))
#     return 0

# board = [list(input().strip()) for _ in range(8)]
# print(move(board))



# t = [list(input()) for i in range(8)]
# dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1]*3
# def DFS(f, y, x):
#     if y==0 or f>7:
#         print(1)
#         exit()
#     if g[f][y][x] == '#':return
#     for i in range(9):
#         ty, tx = y + dy[i], x + dx[i]
#         if not (0<=ty<8 and 0<=tx<8):continue
#         if g[f][ty][tx] == '#':continue
#         DFS(f+1, ty, tx)
# g = []
# for i in range(9):
#     g.append(t)
#     t = [list('.'*8) for k in range(i+1)] + t[i:-1]
# DFS(0, 7, 0)
# print(0)