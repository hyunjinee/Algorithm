from collections import deque

def bfs(i, j):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((i, j))
    check[i][j] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < R) and (0 <= X < C) and graph[Y][X] != 'X' and check[Y][X] == -1:
                check[Y][X] = check[y][x] + 1
                if graph[Y][X] == 'G':
                    return check[Y][X]
                q.append((Y, X))
    return None

for _ in range(int(input())):
    R, C = map(int, input().split())
    graph = [input() for a in range(R)]
    check = [[-1]*C for b in range(R)]
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'S':
                ans = bfs(i, j)
                print(f"Shortest Path: {ans}" if ans else "No Exit")