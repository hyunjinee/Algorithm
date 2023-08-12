import sys


n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[0] = 1

# 1 => 1, 1가지
# 2 => 2 11, 2가지
# 3 => 21 111, 2가지
# 4 => 4 22 211 1111, 4가지
# 5 => 41 221 2111 11111 4가지

two = [2 ** k for k in range(21)] # 2^k

# 반복문을 통해 2의 멱수의 합을 구한다.
for i in two:
    if i <= n:
        for j in range(i, n + 1):
            dp[j] += (dp[j - i]) % 1000000000
    print(dp)
print(dp)
print(dp[n] % 1000000000)