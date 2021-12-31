import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int , input().split()))
p = list(map(int, input().split()))

dp = [ [0] * 101 for _ in range(n + 1)]

for i in range(1, n+1):
  for j in range(1, 101):
    if j < l[i-1]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i-1]] + p[i-1])

print(dp[n][99])


# # 입력
# N = int(input())
# health = list(map(int, input().split()))
# joy = list(map(int,input().split()))

# dp = [0] * 100

# for i in range(N):
#     for j in range(99,-1,-1):
#         if j + health[i] < 100:
#             dp[j + health[i]] = max(dp[j + health[i]], dp[j] + joy[i])

# print(max(dp))