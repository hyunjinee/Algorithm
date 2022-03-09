
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  m,n = map(int,input().split())
  board = [list(map(int, input().split())) for _ in range(m)]
  ans = 0
  temp = list(zip(*board))
  for t in temp:
    for i, cell in enumerate(t):
      if cell == 1:
        ans += t[i:].count(0)
  print(ans)
  # for i in range(m, -1, -1):
  #   for j in range(n, -1, -1):
  #     if board[i][j] == 1: 
# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(m)]
#     result = 0
#     for c in range(n):
#         col = []
#         for r in range(m):
#             col.append(data[r][c])
#         for i, cell in enumerate(col):
#             if cell == 1:
#                 result += col[i:].count(0)
#     print(result)



#   # for i in range(len(temp)):
#   #   for j in range(len(temp[0]) - 1 , -1 , -1):

#   #     if temp[i][j] == 1:
#   #       ans += len(temp[0]) - j - 1
#   #   if temp[i].count(1) > 1:
#   #     ans -= temp[i].count(1) - 1
#   #   print(ans, "whi")
#   # print(ans, "z")
#   # for i in range(n-1, -1, -1):
#   #   for j in range(0, )