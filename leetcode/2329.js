const countPaths = function (grid) {
  const m = grid.length
  const n = grid[0].length
  const MOD = Math.pow(10, 9) + 7
  const memo = Array(m)
    .fill(0)
    .map(() => Array(n).fill(-1))

  const go = (i, j) => {
    if (memo[i][j] !== -1) return memo[i][j]
    let total = 1
    if (i + 1 < m && grid[i + 1][j] > grid[i][j]) {
      total += go(i + 1, j)
    }
    if (j + 1 < n && grid[i][j + 1] > grid[i][j]) {
      total += go(i, j + 1)
    }
    if (i - 1 >= 0 && grid[i - 1][j] > grid[i][j]) {
      total += go(i - 1, j)
    }
    if (j - 1 >= 0 && grid[i][j - 1] > grid[i][j]) {
      total += go(i, j - 1)
    }
    return (memo[i][j] = total % MOD)
  }

  let res = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      res = (res + go(i, j)) % MOD
    }
  }
  return res
}
