






# import sys
# from collections import deque

# input = sys.stdin.readline


# def destroy(i, left):
#   i,j = r-i, 0
#   if left == 1:
#     for k in range(c):
#       if a[i][k] == 'x':
#         a[i][k] = '.'
#         j = k
#         break
#   else:
#     for k in range(c-1, -1, -1):
#       if a[i][k] == 'x':
#         a[i][k] = '.'
#         j = k 
#         break

#   for k in range(4):
#     ni = i + dx[k]
#     nj = j + dy[k]
#     if 0 <= ni < r and 0 <= nj < c:
#       if a[ni][nj] == 'x':
#         q.append([ni, nj])

# def bfs(x,y ):
#   dq = deque()
#   check = [[0] * c for _ in range(r)]
#   fall_list = []
#   dq.append([x,y])
#   check[x][y] = 1
#   while dq: 
#     x, y  = q.popleft()
#     if x == r-1:
#       return 
#     if a[x+1][y] == '.':
#       fall_list.append([x, y ])
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0<= nx < r and 0 <= ny < c:
#         if a[nx][ny] =='x' and not check[nx][ny]:
#           check[nx][ny] = 1
#           dq.append([nx, ny])
#   fall(check, fall_list)

# def fall (check, fall_list) :
#   k, flag = 1, 0 
#   while True:
#     for i , j in fall_list:
#       if i + k == r-1:
#         flag = 1
#         break
#       if a[i+k+1][j] == 'x' and not check[i + k + 1][i]
# r, c = map(int, input().split())
# a = [list(input().rstrip()) for _ in range(r)]
# n = int(input())
# s = list(map(int,input().split()))
# q = deque()
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# left = 1
# while n:
#   index = s.pop(0)
#   destroy(index, left)


# # shoot = int(input())
# # shoot_list = list(map())
# # print(board)