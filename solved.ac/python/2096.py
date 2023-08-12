# 메모리 낭비를 줄여라!
import sys
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(2)]
dp1 = [[0 for _ in range(3)] for _ in range(2)]

for i in range(n):
  a, b, c = map(int ,input().split())
  dp[1][0] = max(dp[0][0], dp[0][1]) + a
  dp1[1][0] = min(dp1[0][0], dp1[0][1]) + a

  dp[1][1] = max(dp[0][0], dp[0][1], dp[0][2]) + b
  dp1[1][1] = min(dp1[0][0], dp1[0][1], dp1[0][2]) + b

  dp[1][2] = max(dp[0][1], dp[0][2]) + c
  dp1[1][2] = min(dp1[0][1], dp1[0][2]) + c

  dp[0][0] , dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
  dp1[0][0], dp1[0][1], dp1[0][2] = dp1[1][0], dp1[1][1], dp1[1][2]

print(max(dp[1]) , min(dp1[1]))

# import sys
# input = sys.stdin.readline

# n = int(input())

# board = [ list(map(int, input().split())) for _ in range(n)]


# # print(board)

# dp = [[0] *3 for _ in range(n)]

# dp[0][0] = board[0][0]
# dp[0][1] = board[0][1]
# dp[0][2] = board[0][2]

# for i in range(1, n):
#     dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + board[i][0]
#     dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + board[i][1]
#     dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + board[i][2]

# print(max(dp[-1]), end=' ')
# dp = [[0] *3 for _ in range(n)]

# dp[0][0] = board[0][0]
# dp[0][1] = board[0][1]
# dp[0][2] = board[0][2]

# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + board[i][0]
#     dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + board[i][1]
#     dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + board[i][2]
# print(min(dp[-1]), end='')