
n, k = map(int, input().split())
dp = [[0] * 1 for _ in range(1001)]
dp[1].append(1)
for i in range(2, 1001):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[n + 1][k + 1] % 10007)