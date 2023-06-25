function longestPalindrome(s) {
  if (s.length <= 1) {
    return s
  }

  const dp = Array(s.length + 1)
    .fill()
    .map((_) => Array(s.length + 1).fill(false))

  let result = ""

  for (let i = 0; i < s.length; i++) {
    dp[i][i] = true
    result = s[i]
  }

  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true
    }
    if (dp[i][i + 1]) {
      result = s.slice(i, i + 2)
    }
  }

  for (let i = s.length - 1; i >= 0; i--) {
    for (let j = i + 2; j < s.length; j++) {
      dp[i][j] = dp[i + 1][j - 1] && s[i] === s[j]
      if (dp[i][j]) {
        result = result.length < j - i + 1 ? s.slice(i, j + 1) : result
      }
    }
  }

  return result
}
