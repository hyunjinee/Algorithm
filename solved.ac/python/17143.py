import sys
input = sys.stdin.readline
def shMove():
    temp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] != 0:
                x, y, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if temp[x][y] == 0:
                    temp[x][y] = [g[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [g[i][j][0], d, z]
    return temp
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, m = map(int, input().split())
g = [[0] * C for i in range(R)]
for i in range(1, m + 1):
    r, c, s, d, z = map(int, input().split())
    g[r - 1][c - 1] = [s, d - 1, z]
result = 0
for i in range(C):
    for j in range(R):
        if g[j][i] != 0:
            result += g[j][i][2]
            g[j][i] = 0
            break
    g = shMove()
print(result)



# import sys
# input = sys.stdin.readline
# r,c,m = map(int,input().split())
# board = [[0] * c for _ in range(r)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def sharkMove():
#   temp = [[0]*c for _ in range(r)]
#   for i in range(r):
#     for j in range(c):
#       if board[i][j] != 0:
#         x,y,s,d,z = i,j, board[i][j][0], board[i][j][1], board[i][j][2]
#         while s > 0:
#           x += dx[d]
#           y += dy[d]
#           if 0 <= x <r and 0 <= y <c:
#             s-= 1
#           else:
#             x -= dx[d]
#             y -= dy[d]
#             if d == 0: d = 1
#             elif d == 1: d = 0 
#             elif d == 2 : d = 3
#             elif d == 3: d = 2
#         if temp[x][y] == 0:
#           temp[x][y] = [board[i][j][0] , d, z]
#         else:
#           if temp[x][y][2] < z:
#             temp[x][y] = [board[i][j][0],d, z]
#   return temp

# for i in range(m):
#   r,c,s,d,z = map(int,input().split())
#   board[r-1][c-1]=[s, d - 1, z]
# result = 0
# for i in range(c):
#   for j in range(r):
#     if board[j][i] != 0:
#       result += board[j][i][2]
#       board[j][i] = 0
#       break
  
#   board = sharkMove()
# print(result)