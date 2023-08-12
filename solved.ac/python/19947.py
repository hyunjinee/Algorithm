# 매년 5
# 3년 20
# 5년 35
import sys

def get_max_profit(h, y):
    dp = [0 for i in range(y+1)]
    dp[0] = h
    for i in range(1, y+1):
        dp[i] = int(dp[i-1]*1.05)
        if i >= 3:
            dp[i] = max(int(dp[i-3]*1.2), dp[i])
        if i >= 5:
            dp[i] = max(int(dp[i-5]*1.35), dp[i])
    return dp[y]

if __name__ == "__main__":
    h, y = list(map(int, sys.stdin.readline().split()))
    print(get_max_profit(h, y))