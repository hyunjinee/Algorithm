import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = cost + graph[new_x][new_y]

                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

count = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1



# import sys; input = sys.stdin.readline
# from collections import deque

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(board, size) :
#   q = deque()
#   q.append((0, 0))
#   visited = [[0] * size for _ in range(size)]
#   while q: 
#     y, x = q.popleft()
#     if visited[y][x]: continue


#     if y == size - 1 and x == size - 1:
#       return board[y][x]

#     for i in range(4):
#       ny = y + dy[i]
#       nx = x + dx[i]
#       if 0 <= ny < size and 0 <= nx < size:
#         if not visited[ny][nx]:
#           q.append((ny, nx))
#           visited[ny][nx] = 1
#           board[ny][nx] = board[y][x] + board[ny][nx]
  

# while True:

#   size = int(input())
#   if size == 0 :
#     break

#   ans = 0
#   board = [list(map(int, input().split())) for _ in range(size)]






