const numberOfArithmeticSlices = function (A) {
  let sum = 0,
    dp = Array(A.length).fill(0)

  for (var i = 2; i <= dp.length - 1; i++) {
    if (A[i] - A[i - 1] === A[i - 1] - A[i - 2]) {
      dp[i] = 1 + dp[i - 1]
      sum += dp[i]
    }
  }

  return sum
}
