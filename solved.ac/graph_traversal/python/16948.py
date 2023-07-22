from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c))
    graph[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            R, C = r+dr, c+dc
            if (0 <= R < N) and (0 <= C < N) and graph[R][C] == -1:
                q.append((R, C))
                graph[R][C] = graph[r][c]+1

N = int(input())
sr, sc, er, ec = map(int, input().split())
graph = [[-1]*(N) for _ in range(N)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(sr, sc)
print(graph[er][ec])