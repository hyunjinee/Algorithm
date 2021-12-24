n = int(input())
find = int(input())

board = [[0] * (n) for _ in range(n)]

a=b=n//2
y,x= 0, 0
board[0][0] = n ** 2
number = n ** 2
d = [(1, 0), (0,1), (-1, 0), (0, -1)]
ans = (0, 0)
while board[a][b] != 1 :
      for dy, dx in d:
        while True:
          if 0 <= x + dx < n and 0 <= y + dy < n and  board[y+dy][x+dx] == 0:
            number -= 1
            y , x = y+dy, x+dx
            if number == find:
              ans = (y, x)
            board[y][x] = number 
          else: break 

for i in range(n):
  for j in range(n):
    print(board[i][j], end= ' ')
  print()
print(ans[0]+ 1, ans[1] +1)
    
# x = y = N // 2
# check = 2 
# li[x][y] = n
# i = 0
# j = 0
# while li[0][0] != N**2:
#     x -= 1
#     for i in range(check):
#         n += 1
#         li[x][y+i] = n
#         if n == w:
#             ans = [x+1, y+i+1]
#     y += i
#     for i in range(1, check+1):
#         n += 1
#         li[x+i][y] = n
#         if n == w:
#             ans = [x+i+1, y+1]
#     x += i
#     for i in range(1, check+1):
#         n += 1
#         li[x][y-i] = n
#         if n == w:
#             ans = [x+1, y-i+1]
#     y -= i
#     for i in range(1, check+1):
#         n += 1
#         li[x-i][y] = n
#         if n == w:
#             ans = [x-i+1, y+1]
#     x -= i
#     check += 2

# for i in range(N):
#     for j in range(N):
#         print(li[i][j], end = ' ')
#     print()
# print(*ans)

# n = int(input())
# find = int(input())

# board = [[0]* (n) for _ in range(n)]


# d = [(1,0), (0, 1), (-1, 0), (0, -1)]
# y, x = 0, 0
# number = n ** 2
# board[y][x] = number
# coord = 0, 0
# count = 0
# while count <= n:
#   #if board[y][x] != 0:
#   #   break 
#   count += 1
#   for dy, dx in d:
#     while True:
#       if 0 <= y+dy < n and 0 <= x+dx < n  and board[y+dy][x + dx] == 0 :
#         number = number - 1
#         board[y+dy][x + dx] = number
#         y, x = y+dy, x+dx
#         if number == find:
#           coord = y + 1,x + 1
#       else:
#         break

# for i in range(n):
#   for j in range(n):
#     print(board[i][j], end =' ')
#   print()    
# print(coord[0], coord[1])
