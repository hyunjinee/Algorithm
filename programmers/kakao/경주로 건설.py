from collections import deque
import sys
INF= sys.maxsize
ans = INF
def solution(board):
  global ans
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  n = len(board)
  visited = [[-1] * n for _ in range(n)]
  q =deque()
  q.append((0,0,0,'no-direction'))
  visited[0][0] = 0 
  
  while q:
    now_cost, y, x, direction = q.popleft()
    if y == n-1 and x == n- 1:
      ans = min(ans, now_cost)
    for dy, dx in d:
      ny = dy + y
      nx = dx + x
      if ny < 0 or ny >= n or nx < 0 or nx >= n:
        continue
      if board[ny][nx] == 1:
        continue
      if board[ny][nx] == 0 and visited[ny][nx] == -1:
        visited[ny][nx] = 0
        if dy == 0 :
          new_direction = 1
        elif dx == 0:
          new_direction = 2
        if new_direction != direction and direction != 'no-direction':
          q.append((now_cost+ 600, ny, nx, new_direction))
        else:
          q.append((now_cost+ 100, ny, nx, direction))
     
  print(ans)
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# import math
# from collections import deque

# def solution(board):
#     def bfs(start):
#         # table[y][x] = 해당 위치에 도달하는 최솟값.
#         table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
#         # 진행 방향. 위 - 0, 왼쪽 - 1, 아래 = 2, 오른쪽 = 3
#         dirs = [(-1,0),(0,-1),(1,0),(0,1)]
#         queue = deque([start])
        
#         # 처음 위치의 비용 = 0
#         table[0][0] = 0
#         while queue:
#             # y좌표, x좌표, 비용, 진행방향
#             y, x, cost, head = queue.popleft()
#             for idx, (dy, dx) in enumerate(dirs):
#                 ny, nx = y + dy, x + dx
#                 # 진행방향과 다음 방향이 일치하면 + 100, 다르면 전환비용 500 + 진행비용 100 = 600
#                 n_cost = cost + 600 if idx != head else cost + 100
#                 # board[y][x] == 0 : 진행방향에 벽이 없음. table[ny][nx] > n_cost : 다음 좌표의 최솟값보다 진행방향 비용이 작을 경우
#                 if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] == 0 and table[ny][nx] > n_cost:
#                     # table 좌표 업데이트.
#                     table[ny][nx] = n_cost
#                     queue.append((ny, nx, n_cost, idx))
#         return table[-1][-1]
#     return min(bfs((0,0,0,2)), bfs((0,0,0,3)))

# # from collections import deque
# # import math
# # def solution(board):
# #     def bfs(start):
# #       table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
# #       d = [(0,1), (0,-1), (1,0), (-1,0)]
# #       q = deque([start])
# #       table[0][0] = 0
# #       while q:
# #         y, x, cost, head = q.popleft()
# #         for idx, (dy, dx) in enumerate(d):
# #           ny, nx = y + dy, x + dx
# #           n_cost = cost + 600 if idx != head else cost + 100
# #           if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] == 0 and table[ny][nx] > n_cost:
# #             table[ny][nx] = n_cost
# #             q.append((ny, nx, n_cost, idx))
# #       return table[-1][-1]

# #     return min(bfs((0,0,0,2), bfs(0,0,0,3)))



#     # n =len(board)
#     # d = [(0,1),(0,-1),(1,0),(-1,0)]
#     # q = deque()
#     # q.append((0,0,0,0))
#     # answer = 0
#     # return answer

# # import sys
# # INF = sys.maxsize
# # answer = INF
# # corner = 0 
# # def solution(board):
# #     n = len(board)

# #     d = [(0,1),(1,0),(0,-1),(-1,0)]
# #     def dfs(y , x , value, direction):
# #       global answer 
# #       global corner
# #       if y == n - 1 and x == n -1:
# #         print(answer)
# #         print(corner, "코너")
# #         answer = min(answer, value + corner * 500)
# #         return 
# #       for dy, dx in d:
# #         ny, nx = y + dy, x + dx
# #         if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
# #           if dy == 0 :
# #             new_direction = 1 
# #           if dx == 0:
# #             new_direction = 2
# #           board[ny][nx] = 1
# #           if (new_direction == 1 and direction == 1) or (new_direction == 2 and direction == 2):
# #             dfs(ny, nx, value + 100, new_direction)
# #           else:
# #             dfs(ny, nx, value + 100 , new_direction)
# #             corner += 1
# #           board[ny][nx] = 0
# #     dfs(0, 0, 0, "nodirection")
# #     print(answer)
# #     return answer
# # solution([[0,0,0],[0,0,0],[0,0,0]])

# # # from collections import deque

# # # def solution(board):
# # #     answer = 0
# # #     n = len(board)
# # #     m = len(board[0])
# # #     def bfs(a, b):
# # #       direction = ''
# # #       sum = 0
# # #       d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# # #       q = deque()
# # #       q.append((a, b))
# # #       while q:
# # #         y, x = q.popleft()
# # #         for dy, dx in d:
# # #           if 0 <= y + dy < n and 0 <= x + dx < m:
# # #             ny = y + dy
# # #             nx = x + dx
# # #             if board[ny][nx] == 0:
# # #               board[ny][nx] = 1
# # #               q.append((ny, nx))


# # #     print(answer)
# # #     return answer

