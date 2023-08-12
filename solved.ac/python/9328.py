from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    c = [[0]*(w+2) for _ in range(h+2)]
    q.append([x, y])
    c[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        c[nx][ny] = 1
                        q.append([nx, ny])
                    elif a[nx][ny].islower():
                        door[ord(a[nx][ny]) - ord('a')] = 1
                        q = deque()
                        c = [[0]*(w+2) for _ in range(h+2)]
                        a[nx][ny] = '.'
                        q.append([nx, ny])
                    elif a[nx][ny].isupper():
                        if door[ord(a[nx][ny]) - ord('A')]:
                            c[nx][ny] = 1
                            a[nx][ny] = '.'
                            q.append([nx, ny])
                    elif a[nx][ny] == '$':
                        c[nx][ny] = 1
                        cnt += 1
                        a[nx][ny] = '.'
                        q.append([nx, ny])
    print(cnt)

def new_map():
    for i in a:
        i.insert(0, '.')
        i.append('.')
    a.insert(0, ['.']*(w+2))
    a.append(['.']*(w+2))

tc = int(input())
while tc:
    h, w = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    key = list(input().strip())
    door = [0]*26

    for k in key:
        if k != '0':
            door[ord(k)- ord('a')] = 1

    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(a[i][j]) <= ord('Z'):
                if door[ord(a[i][j]) - ord('A')]:
                    a[i][j] = '.'
    new_map()
    bfs(0, 0)
    tc -= 1