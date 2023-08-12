n = int(input())
dp = [0] * 4
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

if n < 4: 
  print(dp[n])
else: 
  for i in range(4, n+1):
    dp[i % 4] = dp[(i-1) % 4 ] + dp[(i-2) % 4]
    dp[i % 4] = dp[i % 4] % 15746
  print(dp[n % 4])
# dp= [0] * ( n + 1)

# dp[1] = 1
# dp[2]  = 2
# dp[3] = 3
# dp[4] = 5

# if n <= 4: 
#   print(dp[n])
# else :
#   for i in range(5, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#   print(dp[n])

# 1
# 00 11
# 001 100 111
# 0000 1111 0011 1100 1111
# 00000 11111 00111 11100 11111 00100 10000 10000
