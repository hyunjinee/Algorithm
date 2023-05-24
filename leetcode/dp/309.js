const maxProfit = function (prices) {
  const BUY = 0
  const SELL = 1
  const HOLD = 2
  const REST = 3

  const memo = Array(prices.length)
    .fill(0)
    .map(() => Array(4).fill(null))

  const helper = (i, action) => {
    if (i === prices.length) {
      return 0
    }
    if (memo[i][action] !== null) return memo[i][action]

    switch (action) {
      case BUY:
        memo[i][BUY] = Math.max(helper(i + 1, SELL), helper(i + 1, HOLD)) - prices[i]
        return memo[i][BUY]
      case SELL:
        memo[i][SELL] = helper(i + 1, REST) + prices[i]
        return memo[i][SELL]
      case HOLD:
        memo[i][HOLD] = Math.max(helper(i + 1, SELL), helper(i + 1, HOLD))
        return memo[i][HOLD]
      case REST:
        memo[i][REST] = Math.max(helper(i + 1, BUY), helper(i + 1, REST))
        return memo[i][REST]
    }
  }

  return Math.max(helper(0, BUY), helper(0, REST), 0)
}
