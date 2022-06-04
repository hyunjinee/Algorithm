import sys
input = sys.stdin.readline

h, w, x, y = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(h + x)]

prototype = [[0 for _ in range(w)] for _ in range(h)]
check = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
  for j in range(w):
    if i < h and j < w: check[i][j] += 1
    if i + x < h and j + y < w: check[i+x][j+y] += 1

for i in range(h):
  for j in range(w):
    if check[i][j] == 1: prototype[i][j] = board[i][j]
    elif check[i][j] == 2: 
      prototype[i][j] = board[i][j] - prototype[i-x][j-y]

for i in range(h):
  print(*prototype[i])
# import sys

# h, w, x, y = map(int, sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h+x)]

# def solve():
#     recovered_arr = [[0 for _ in range(w)] for _ in range(h)]
#     check = [[0 for _ in range(w)] for _ in range(h)]

#     for i in range(h):
#         for j in range(w):
#             if i < h and j < w: check[i][j] += 1
#             if i+x < h and j+y < w: check[i+x][j+y] += 1
#     # print(check)
#     for i in range(h):
#         for j in range(w):
#             if check[i][j] == 1: recovered_arr[i][j] = arr[i][j]
#             elif check[i][j] == 2:
#                 recovered_arr[i][j] = arr[i][j] - recovered_arr[i-x][j-y]
    
#     # print(recovered_arr)

#     for i in range(h):
#         for j in range(w):
#             print(recovered_arr[i][j], end=' ')
#         print()

# solve()


# # import sys
# # input =sys.stdin.readline

# # h,w,x,y = map(int,input().split())
# # board = [list(map(int,input().split())) for _ in range(h + x)]

# # # 항상 배열 A가 존재하는 경우만 입력으로 주어진다.


# # for i in range(len(board)):
# #   count = 0
# #   for j in range(len(board[0])):
# #     if i + x < h + x and j + y < w + y:
# #       if i + x < h and j + y < w:
# #         ``