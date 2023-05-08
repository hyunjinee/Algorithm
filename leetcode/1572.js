/**
 * @param {number[][]} mat
 * @return {number}
 */
const diagonalSum = function (mat) {
  let result = 0
  const n = mat.length
  for (let i = 0; i < n; i++) {
    result += mat[i][i]
  }
  let j = 0
  for (let i = n - 1; i >= 0; i--) {
    result += mat[i][j++]
  }

  if (n % 2 == 1) {
    result -= mat[Math.floor(n / 2)][Math.floor(n / 2)]
  }

  return result
}
