from collections import deque
import sys

input = sys.stdin.readline
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

for u in range(m):
    c = [[0] * n for _ in range(n)]
    d, s = map(int, input().split())
    d -= 1

    qlen = len(q)
    while qlen:
        x, y = q.popleft()
        nx = x + s * dx[d]
        ny = y + s * dy[d]

        if nx >= n:
            nx %= n
        elif nx < 0:
            nx = (n - 1) - (((-1) * nx - 1) % n)
        if ny >= n:
            ny %= n
        elif ny < 0:
            ny = (n - 1) - (((-1) * ny - 1) % n)

        q.append([nx, ny])
        qlen -= 1

    for k in q:
        x, y = k
        if c[x][y] == 0:
            a[x][y] += 1
            c[x][y] = 1

    q = deque([])

    for x in range(n):
        for y in range(n):
            if c[x][y] == 1:
                cnt = 0
                for i in range(1, 8, 2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] > 0:
                            cnt += 1
                a[x][y] += cnt

    for x in range(n):
        for y in range(n):
            if a[x][y] >= 2:
                if c[x][y] == 0:
                    q.append([x, y])
                    a[x][y] -= 2

print(sum(sum(b) for b in a))