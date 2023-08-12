# 2* n 타일링


# 일단 이문제는 dp 문제이고 점화식을 세우면 쉽게 구 할 수 있다.


n = int(input())


# n을 받고

dp = [0] * 1001

# 리스트를 만들어준다.

dp[1] = 1
dp[2] = 2


for i in range(3, n+1):
    dp[i] = (dp[i- 1] + dp[i - 2] ) % 10007


print(dp[n])

