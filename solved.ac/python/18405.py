from collections import deque
 
N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      virus.append(((graph[i][j], i, j)))
S, X, Y = map(int, input().split())
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(s, X, Y):
  q = deque(virus)
  count = 0
  while q:
    if count == s:
      break
    for _ in range(len(q)):
      prev, x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], nx, ny))
    count += 1
  return graph[X-1][Y-1]
 
virus.sort()
print(bfs(S, X, Y))

# import sys; input = sys.stdin.readline
# from collections import deque

# n, k = map(int, input().split())
# virus = [list(map(int, input().split())) for _ in range(n)]
# s, x, y = map(int, input().split())
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# def spread(q):
#   q = deque(q)
#   while q:
#     virus_num, y, x = q.popleft()
#     for i in range(4):
#       ny = y + dy[i]
#       nx = x + dx[i]
#       if 0 <= ny < n and 0 <= nx < n and virus[ny][nx] == 0:
#         virus[ny][nx] = virus_num 
# def get_virus():
#   q = []
#   for i in range(n):
#     for j in range(n):
#       if virus[i][j] != 0:
#         q.append((virus[i][j], i, j))
#   return q.sort()

# while s > 0:
#   s -= 1
#   q = get_virus()
#   spread(q)

# print(virus[x-1][y-1])