n = int(input())
dp = [-1] * (n+8)
dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4

for i in range(9, n+1):
    dp[i] = min(dp[i-2], dp[i-5])+1

print(dp[n])

# n = int(input())
# # 2, 5원 밖에 없고 거스름돈 동전의 개수를 최소화 하려면
# # 5원이 많을 수록 좋긴한데. 흠
# dp = [0] * (n + 1)
# dp[2] = 1
# dp[4] = 2
# dp[5] = 1
# dp[6] = 3
# dp[7] = 2
# dp[8] = 4
# dp[9] = 3
# dp[10] = 2

# for i in range(1, n+1):
#   dp[i] = min(dp[i-2] + 1, dp[i-5] + 1, dp[i] + 1)

# print(dp)


# # dp[2] = 1
# # dp[3] = 불가
# # dp[4] = 2
# # dp[5] = 1
