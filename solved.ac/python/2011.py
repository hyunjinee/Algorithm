s = input()
dp = [0] * (len(s) + 1)
if s[0] == '0':
  print('0')
  exit()
dp[0] = 1; dp[1] = 1
for i in range(2, len(s) + 1):
  if int(s[i - 1]) > 0:
    dp[i] += dp[i - 1]
  num = int(s[i-1]) + int(s[i-2]) * 10
  if 10 <= num <= 26:
    dp[i] += dp[i-2]
print(dp[len(s)] % 1000000)