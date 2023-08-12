# n, k = map(int, input().split())
# s = [[0] * 201 for i in range(201)]
# for i in range(201):
#     s[i][1] = 1
# print(s)
# for i in range(1, 201):
#     for j in range(201):
#         for l in range(j + 1):
#             s[j][i] += s[l][i - 1]
# print(s[n][k] % 1000000000)


# n, k = map(int, input().split())
# dp = [[0] * 201 for i in range(201)]
# for i in range(201):
#     dp[1][i] = 1
#     dp[2][i] = i + 1

# for i in range(2, 201):
#     dp[i][1] = i 
#     for j in range(2, 201):
#         dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
# print(dp[k][n])


N, K = map(int, input().split())
dp = [1] * (N+1)

for _ in range(K-1):
    for i in range(1, N+1):
        dp[i] += dp[i-1]

print(dp[N]%1000000000)
