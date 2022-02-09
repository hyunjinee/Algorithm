from itertools import permutations
import sys

input = sys.stdin.readline
INF = int(1e9)

def part_rotate(board, rotate):
    for i in rotate:
        r, c, s = i
        for j in range(1, s + 1):
            cnt = 2 * j
            tmp = board[r - j][c + j]  # 가장 오른쪽 상위 값

            for k in range(cnt): # 위 : 왼쪽에서 오른쪽 이동(->)
                board[r - j][c + j - k] = board[r - j][c + j - k - 1]
            for k in range(cnt): # 왼쪽 : 아래쪽에서 위쪽으로 이동(^)
                board[r - j + k][c - j] = board[r - j + k + 1][c - j]
            for k in range(cnt): # 아래 : 오른쪽에서 왼쪽으로 이동(<-)
                board[r + j][c - j + k] = board[r + j][c - j + k + 1]
            for k in range(cnt - 1): # 오른쪽 : 위쪽에서 아래쪽으로 이동(v)
                board[r + j - k][c + j] = board[r + j - k - 1][c + j]

            board[r - j + 1][c + j] = tmp

    min_value = INF
    for i in range(n):
        min_value = min(min_value, sum(board[i]))

    return min_value


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    rotates = []
    for _ in range(k):
        r, c, s = map(int, input().split())
        rotates.append((r - 1, c - 1, s))

    # 순열
    min_value = INF
    for rotate in permutations(rotates):
        # print(rotate)
        tempBoard = [[] * m for _ in range(n)]  # 임시 배열
        for i in range(n):
            for j in range(m):
                tempBoard[i].append(board[i][j])

        min_value = min(min_value, part_rotate(tempBoard, rotate))

    print(min_value)