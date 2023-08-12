
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())
M, N = MIIS()
grid_length = M * 2
growth = [0] * (grid_length)
for _ in range(N):
    zero, one, _ = MIIS()
    growth[zero] += 1
    growth[zero + one] += 1

growth[0] += 1
for i in range(grid_length - 1):
    growth[i + 1] += growth[i]

for i in range(M):
    output_line = [growth[M - 1 - i]] + growth[M:-1]
    print(*output_line)

# import sys
# input =sys.stdin.readline
# m, n = map(int ,input().split())
# board = [[1] * m for _ in range(m)]
# growth = [[0] * m for _ in range(m)]
# days = [list(map(int,input().split())) for _ in range(n)]
# for day in days:
#   a, b, c = day
#   temp = []
#   for i in range(a):
#     temp.append(0)
#   for i in range(b):
#     temp.append(1)
#   for i in range(c):
#     temp.append(2)
#   cursor = 0 
#   for i in range(m -1, 0, -1):
#     board[i][0] += temp[cursor]
#     growth[i][0] = temp[cursor]
#     cursor += 1
#   for i in range(0, m):
#     board[0][i] += temp[cursor]
#     growth[0][i] = temp[cursor]
#     cursor += 1
#   # print('board')
#   # for bo in board:
#   #   print(bo)
#   # print()
#   # print('growth')
#   # for gr in growth:
#   #   print(gr)
#   # print()
#   # print(growth)
  
#   for i in range(1, m):
#     for j in range(1, m):
#       board[i][j] += max(growth[i-1][j], growth[i-1][j-1], growth[i][j-1])
#       growth[i][j] = max(growth[i-1][j], growth[i-1][j-1], growth[i][j-1])
#       # board[i][j] += max(board[i-1][j] - growth[i-1][j], board[i-1][j-1] - growth[i-1][j-1], board[i][j-1] - growth[i][j-1])
#       # growth[i][j] = max(board[i-1][j] - growth[i-1][j], board[i-1][j-1] - growth[i-1][j-1], board[i][j-1] - growth[i][j-1])
#   # print('after board')
#   # for bo in board:
#   #   print(bo)
#   # print()
# for bo in board:
#   print(*bo)

# from sys import stdin

# input = stdin.readline
# m,n = map(int, input().split())

# def solv():
#     worm = [1]*(2*m-1)
#     for _ in range(n):
#         a,b,c = map(int, input().split())
#         for idx in range(a,a+b):
#             worm[idx] += 1
#         for idx in range(a+b,2*m-1):
#             worm[idx] += 2

#     for idx in range(m-1,-1,-1):
#         print(*([worm[idx]]+worm[m:]))
# solv()