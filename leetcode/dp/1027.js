function longestArithSeqLength(nums) {
  const n = nums.length
  const dp = Array(n)
    .fill()
    .map((_) => [])

  let result = 0

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      const diff = nums[i] - nums[j] + 500
      dp[i][diff] = (dp[j][diff] ?? 0) + 1
      result = Math.max(result, dp[i][diff])
    }
  }

  return result + 1
}
