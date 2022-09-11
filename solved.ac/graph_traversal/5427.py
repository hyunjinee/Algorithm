from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (
                    board[nx][ny] == "." or board[nx][ny] == "@"
                ):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag + 1

    return "IMPOSSIBLE"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        q = deque()
        board = []
        visited = [[-1] * w for _ in range(h)]
        for i in range(h):
            board.append(list(input().strip()))
            for j in range(w):
                if board[i][j] == "@":
                    visited[i][j] = 0
                    start = (i, j)
                elif board[i][j] == "*":
                    visited[i][j] = "FIRE"
                    q.append((i, j))

        q.append(start)
        print(bfs())

# import sys; input = sys.stdin.readline
# test_case = int(input())

# def bfs(board):



#   pass




# for _ in range(test_case):
#   w, h = map(int, input().split())

#   board = [list(input().rstrip()) for _ in range(h)]



