a = input()
b = input()
a_len = len(a)
b_len = len(b)
dp =[[0] * (b_len+1) for _ in range(a_len+1)]
for i in range(a_len):
  for j in range(b_len):
    if a[i] == b[j] :
      dp[i+1][j+1] = dp[i][j] + 1
    else: 
      dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
print(dp[a_len][b_len])