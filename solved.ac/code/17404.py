import sys
INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
result = INF

for color in range(3):
  dp = [[0]*3  for _ in range(n)]
  for i in range(3):
    if i == color:
      dp[0][i] = colors[0][i] # 첫번째 집의 색을 칠한다.
    else:
      dp[0][i] = INF # 나머지는 무한대임

  for i in range(1, n):
    dp[i][0] = colors[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = colors[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = colors[i][2] + min(dp[i-1][0], dp[i-1][1])
  # print(dp)
  for i in range(3):
    if i != color:
      result = min(result, dp[-1][i])
print(result)




# from re import L
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
# # 1번집의 색은 2번, N번집의 색과 같지 않아야한다.
# # N번 집의 색은 N-1번 1번의 색과 같지않다.
# # i는 그 좌우의 집과 색이 같지않다.
# n = int(input())
# cost = [[0] * n for _ in range(n+1)]
# dp = [[0] * n for _ in range(n+1)]
# for i in range(1, n+1):
#   cost[i][0], cost[i][1], cost[i][2] = map(int, input().split())
# # print(cost)
# answer = INF

# for _ in range(n):
  # cost = list(map(int, input().split()) )


