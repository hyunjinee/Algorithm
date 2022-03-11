import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, z = chess[chess_num]
    if chess_num != graph[x][y][0]:
        return 0

    nx = x + dx[z]
    ny = y + dy[z]

    if not 0 <= nx < n or not 0 <= ny < n or arr[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        if not 0 <= nx < n or not 0 <= ny < n or arr[nx][ny] == 2:
            return 0
    chess_set = []
    chess_set.extend(graph[x][y])
    graph[x][y] = []
    if arr[nx][ny] == 1:
        chess_set = chess_set[-1::-1]
    for i in chess_set:
        graph[nx][ny].append(i)
        chess[i][:2] = [nx, ny]
    if len(graph[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    graph[x - 1][y - 1].append(i)
    chess[i] = [x-1, y-1, z-1]
cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)



