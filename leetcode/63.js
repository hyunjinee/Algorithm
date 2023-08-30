/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
const uniquePathsWithObstacles = function (grid) {
  const n = grid.length
  const m = grid[0].length

  if (grid[0][0] === 1) {
    return 0
  }

  const dp = Array(n)
    .fill()
    .map(() => Array(m).fill(0))

  console.log(dp)

  for (let i = 0; i < n; i++) {
    if (grid[i][0] === 1) break

    dp[i][0] = 1
  }

  for (let i = 0; i < m; i++) {
    if (grid[0][i] === 1) break

    dp[0][i] = 1
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
      if (grid[i][j] === 1) continue

      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    }
  }
  return dp[n - 1][m - 1]
}

uniquePathsWithObstacles([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
])
