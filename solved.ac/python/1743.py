import sys
sys.setrecursionlimit(10000)

def dfs (y, x, cnt):
  d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  graph[y][x] = 0
  for dy, dx in d:
    Y, X  = y + dy, x + dx

    if 0 <= Y < n and 0 <= X < m and graph[Y][X] == 1:
      cnt = dfs(Y, X, cnt + 1)
      
  return cnt
n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
  y, x = map(int, input().split())
  graph[y-1][x-1] = 1
res = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1: 
      res.append(dfs(i, j, 1))

print(max(res))


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline  

# n, m, k = map(int, input().split())

# passage = [["."]*m for _ in range(n)]


# # 첫째 줄에 통로의 세로 길이 가로 길이 그리고 음식물 쓰레기 개수가 주어짐
# # 다음 k개의 줄에 음식물이 떨어진 좌표가 주어진다.
# # 그냥 음식물 제일 큰거 출력하면 되니까? 그냥 DFS
# for _ in range(k):
#   x, y = map(int, input().split())
#   x -= 1
#   y -= 1

#   passage[x][y] = '#'

# print(passage)

# ans = 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def dfs(x, y, d ): 
#   #  종료 조건이 뭐지?
#   if passage[x][y] == '.':
#     global ans
#     ans = max(ans, d)
#     return 


#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if 0 <= nx < n and 0 <= ny < m:
#       if passage[nx][ny] == '#':
#         dfs(nx, ny, d+1)


# for i in range(n):
#   for j in range(m):
#     if passage[i][j] == '#':
    
#       dfs(i, j, 1)
