from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    global o, v
    q = deque()
    q.append([x, y])
    to, tv = 0, 0
    if s[x][y] == "o": to += 1
    elif s[x][y] == "v": tv += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "#":
                if s[nx][ny] == "o": to += 1
                if s[nx][ny] == "v": tv += 1
                visit[nx][ny] = 1
                q.append([nx, ny])
    if to and tv:
        if to > tv: v -= tv
        else: o -= to
r, c = map(int, input().split())
s = []
visit = [[0] * c for i in range(r)]
o, v = 0, 0
for i in range(r):
    a = list(input().strip())
    for j in range(c):
        if a[j] == "o": o += 1
        if a[j] == "v": v += 1
    s.append(a)
for i in range(r):
    for j in range(c):
        if (s[i][j] == "o" or s[i][j] == "v") and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j)
print(o, v)