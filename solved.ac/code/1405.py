dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def dfs(x, y, cnt, p):
    global ans

    if cnt == n:
        ans += p
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if board[nx][ny]:
            continue
        if not 0 <= nx < (2 * n) + 1 or not 0 <= ny < (2 * n) + 1:
            continue

        board[nx][ny] = 1
        dfs(nx, ny, cnt + 1, p * poss[i] * 0.01)
        board[nx][ny] = 0


n, east, west, south, north = map(int, input().split())
poss = [north, east, south, west]   # 위의 dx, dy 랑 순서 맞춰줌

board = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
board[n][n] = 1

ans = 0

dfs(n, n, 0, 1)
print(ans)

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4방향 탐색

# def dfs(r, c, visited, total):
#     global answer
#     if len(visited) == N+1:
#         answer += total
#         return
#     for idx in range(4):
#         nr = r + d[idx][0]
#         nc = c + d[idx][1]
#         if (nr, nc) not in visited:
#             visited.append((nr, nc))
#             dfs(nr, nc, visited, total*probability[idx])
#             visited.pop()

# N, ep, wp, sp, np = map(int, input().split())
# probability = [ep, wp, sp, np]
# answer = 0

# dfs(0, 0, [(0, 0)], 1)
# print(answer * (0.01 ** N))
# from collections import deque


# temp = list(map(int, input().split()))
# n = temp[0]
# m = temp[1:]

# # 전체이동의 개수를 세야함.
# all = n ** 2 # 전체 이동의 수
# board = [[0] * 30 for _ in range(30)]
# # 이동을 하고 처음 방문했던곳을 또 방문한 것을 카운팅하는 변수
# cnt = 0
# visited = [[False] * 30 for _ in range(30)]
# visited[15][15] =True
# q = deque()
# q.append((15, 15))
# while q:
#   y, x = q.popleft()




