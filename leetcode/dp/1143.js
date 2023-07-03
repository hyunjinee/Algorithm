const longestCommonSubsequence = (text1, text2) => {
  const dp = Array(text1.length + 1)
    .fill(0)
    .map(() => Array(text2.length + 1).fill(0))

  // console.log(dp)

  for (let i = 0; i < text1.length; i++) {
    for (let j = 0; j < text2.length; j++) {
      if (text1[i] == text2[j]) {
        dp[i + 1][j + 1] = dp[i][j] + 1
      } else {
        dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1])
      }
    }
  }
  return dp[text1.length][text2.length]

  return Math.max(...dp.flatMap((x) => x))
}

console.log(longestCommonSubsequence("abcde", "ace")) // 3
