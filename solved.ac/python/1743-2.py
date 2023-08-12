from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < N) and (0 <= X < M) and graph[Y][X] == 1:
                queue.append((Y, X))
                graph[Y][X] = 0
                cnt += 1
    return cnt
            
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1
res = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            res.append(bfs(i, j))
print(max(res))