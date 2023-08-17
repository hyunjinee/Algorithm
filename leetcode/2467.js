/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
const countGoodStrings = function (low, high, zero, one) {
  const dp = Array(high + 1).fill(0)
  const modulo = Math.pow(10, 9) + 7
  dp[0] = 1

  let result = 0

  for (let i = 1; i <= high; i++) {
    if (i - zero >= 0) {
      dp[i] = (dp[i] + dp[i - zero]) % modulo
    }

    if (i - one >= 0) {
      dp[i] = (dp[i] + dp[i - one]) % modulo
    }

    if (i >= low) {
      result = (result + dp[i]) % modulo
    }
  }
  return result
}
