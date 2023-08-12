import sys
sys.setrecursionlimit(10**7)
move = [(0,1),(1,0),(0,-1),(-1,0)]
def dfs(r,c):
    global flag, cnt
    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if h > pool[nr][nc] and visited[nr][nc] == False:
                visited[nr][nc] = True
                road.append((nr,nc))
                dfs(nr,nc)
        else:
            flag = False


n, m = map(int, sys.stdin.readline().split())
pool = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt = 0
for h in range(1,10):
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if pool[i][j] < h and visited[i][j] == False:
                visited[i][j] = flag = True
                road = [(i,j)]
                dfs(i,j)
                if flag:
                    for r, c in road:
                        pool[r][c] += 1
                        cnt += 1
print(cnt)