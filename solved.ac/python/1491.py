n, m = map(int, input().split())
count = n * m - 1
board = [[0] * n for _ in range(m)]

point = (m - 1, 0)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

board[m-1][0] = 24

while count > 0:
  for i in range(4):
    while True:
      y, x = point
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 0:
        board[ny][nx] = count
        count -= 1
        point = (ny, nx)
      
        # print(board)
        # exit()
      else :break
    

for i in range(m):
  for j in range(n):
    if board[i][j] == 1:



      print(i, m - ( j + 1))






# while count > 0:
#   for i in range(4):
#     while True:
#       y, x = point[0] + dy[i], point[1] + dx[i]
#       if 0 <= y < m and 0 <= x < n and board[y][x] == 0:
#         board[y][x] = count
#         count -= 1
#         point = (y, x)
#       else: break
#     # print(board)

#   print(point)
  # for i in range(4):
  #   while True:
  #     x, y = point[0] + dx[i], point[1] + dy[1]
  #     if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
  #       board[x][y] = count
  #       count -= 1
  #       point = (x, y)
  #     else: break
  # print(board)

# 12 13 14 15 16 17
# 11 0   0  0  0  18
# 10 0  0    0 0  19
# 9 24 23 22 21 20 