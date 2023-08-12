# 16918, 봄버맨
import sys
from collections import deque


def loc_bombs():    # 폭탄 위치 찾아 bombs deque에 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombs.append((i, j))


def make_bombs():   # 모든 자리에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode():      # bombs deque에 들어있는 좌표로 폭탄 터트림
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'


R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

N -= 1  # 1초 동안 아무것도 하지 않는다
while N:
    bombs = deque()
    loc_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()

# import sys
# from collections import deque
# input = sys.stdin.readline

# def findBomb ():
#   for i in range(r):
#     for j in range(c):
#       if graph[i][j] == 'O':
#         bombList.appned((i,j))
# def allBombSet():
#   for i in range(r):
#     for j in range(c):
#       if graph[i][j] != 'O':
#         graph[i][j] = 'O'
# def bomb():
#   while bombList:
#     x, y = bombList.popleft()
#     graph[x][y] = '.'
#     for dy ,dx in (0,1), (0,-1), (1,0), (-1,0):
#       nx, ny = x + dx, y + dy
#       if 0 <= nx < r and 0 <= ny < c:
#         if graph[nx][ny] == 'O':
#           graph[nx][ny] = '.'

# r,c,n = map(int,input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# n -= -1
# while n :
#   bombList = deque()
#   findBomb()
#   allBombSet()
#   n -= 1
#   if n == 0 :
#     break
#   bomb()
#   n -= 1

# for i in range(r):
#   for j in range(c):
#     print(graph[i][j], end='')
#   print()
# # # r c

# # # 3second -> die
# # # another bomb die


# # import sys
# # from collections import deque
# # input = sys.stdin.readline
# # r,c,n  =  map(int,input().split())
# # board = [list(input().rstrip()) for _ in range(r)]
# # time = 1 # not doing anything for the first time 
# # def timeover():
# #   global time 
# #   global board
# #   if time >= n :
# #     for bo in board: 
# #       print(bo)
# #     exit()
# # def bfs() :
# #   global time
# #   global board
# #   visited = [[False] * c for _ in range(r)]
# #   q = deque()
# #   for i in range(r):
# #     for j in range(c):
# #       if board[i][j] ==  'O' and not visited[i][j]:
# #         visited[i][j] = True
# #         q.append((i,j))
# #   board = [['O'] * c for _ in range(r)] # bomb to all space 
# #   time += 1
# #   timeover()
# #   time += 1
# #   timeover()
# #   while q: # to bomb all
# #     y, x = q.popleft()
# #     for dy, dx in (0,1), (0,-1), (1, 0), (-1,0) :
# #       ny, nx = y + dy , x + dx
# #       if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and board[ny][nx] == 'O':
# #         visited[ny][nx] = True
# #         q.append((ny,nx))
# #         board[ny][nx] = '.'


# # while time < n:
# #   bfs()
  

