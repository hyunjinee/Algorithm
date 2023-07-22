from collections import deque
def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 2
    while q:
        y, x = q.popleft()    
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
                q.append((Y, X))
                graph[Y][X] = 2
            
M, N = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for j in range(N):
    if graph[0][j] == 0:
        bfs(0, j)
print("YES" if 2 in graph[-1] else "NO")