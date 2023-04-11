function solution(s) {
  let answer = 1
  const len = s.length
  const dp = Array(len)
    .fill()
    .map((_) => Array(len).fill(false))

  for (let i = 0; i < len; i++) {
    dp[i][i] = true
  }

  for (let i = 0; i < len - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true
      answer = 2
    }
  }

  for (let i = 3; i <= len; i++) {
    for (let start = 0; start <= len - i; start++) {
      const end = start + i - 1
      if (s[start] === s[end] && dp[start + 1][end - 1]) {
        dp[start][end] = true
        answer = Math.max(answer, i)
      }
    }
  }

  return answer
}
