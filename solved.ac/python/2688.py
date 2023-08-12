import sys
input = sys.stdin.readline


for _ in range(int(input())):
    dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    n = int(input())
    
    for i in range(n - 1):
        for j in range(10):
            dp[j] = sum(dp[j:])
    
    print(sum(dp))

# import sys
# input = sys.stdin.readline
# t = int(input())
# dp = [ [0] * 10 for _ in range(65)]
# dp[1] = [1] * 10

# for i in range(2, 65):
#   for j in range(10):
#     for k in range(j, 10):
#       dp[i][j] += dp[i-1][k]
# for _ in range(t):
#   a = int(input())
#   print(dp[a + 1][0])