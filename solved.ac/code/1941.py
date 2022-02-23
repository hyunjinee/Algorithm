# 다시 풀어
# import sys
# input = sys.stdin.readline
# s = [list(input().rstrip()) for _ in range(5)]

# print(s)
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# # a 이다솜파 b 임도연파
# def dfs (y, x, a, b) :
#   global ans
#   s[y][x] = "x"
  
#   if a + b == 7  and a > b:
#     ans += 1
    

#   for dy, dx in d :
#     ny = y + dy
#     nx = x + dx

#     if 0 <= ny < 5 and 0<= nx < 5 :
#       if s[ny][ny] == "Y":
#         dfs(ny,nx, a, b + 1)
#       elif s[ny][nx] == "S":
#         dfs(ny,nx , a+1, b)


# ans = 0

# for i in range(5):
#   for j in range(5):
#     if s[i][j] == "Y":
    
#       dfs(i, j, 0 , 1)
#     else:
#       dfs(i, j , 1, 0)

# print(ans)