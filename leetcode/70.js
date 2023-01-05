const climbStairs = function (n) {
  const dp = []
  dp.push(1)
  dp.push(1)
  dp.push(2)

  if (n <= 2) {
    return dp[n]
  }

  for (let i = 3; i <= n; i++) {
    dp.push(dp[i - 1] + dp[i - 2])
  }
  return dp[n]
}
