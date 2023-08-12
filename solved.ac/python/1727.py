import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

if n > m: 
    boys, girls = girls, boys
    n, m = m, n


dp = [[0] * m for __ in range(n)]

boys.sort()
girls.sort()

dp[0][0] = abs(boys[0] - girls[0])
for j in range(1, m - (n - 1)):
    dp[0][j] = min(abs(boys[0] - girls[j]), dp[0][j - 1])
    
for i in range(1, n):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(boys[i] - girls[j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(boys[i] - girls[j]), dp[i][j - 1])
print(dp[n - 1][m - 1])

# n, m = map(int, input().split())
# man = list(map(int, input().split()))
# woman = list(map(int, input().split()))

# man.sort()
# woman.sort()

# dp = [[0 for _ in range(m + 1)] for _ in range(n+1)] 

# for i in range(1, n+1):
#   for j in range(1, m+1):
#     dp[i][j] = dp[i-1][j-1] + abs(man[i-1]-woman[j-1])

#     if i > j:
#       dp[i][j] = min(dp[i][j], dp[i-1][j])
#     elif i < j:
#       dp[i][j] = min(dp[i][j], dp[i][j-1])

# print(dp[n][m])