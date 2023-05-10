/**
 * @param {number} n
 * @return {number[][]}
 */
const generateMatrix = function (n) {
  const matrix = Array(n)
    .fill(0)
    .map((_) => Array(n).fill(0))
  let current = 1
  let [left, right, bottom, top] = [0, n - 1, n - 1, 0]

  while (left <= right && top <= bottom) {
    for (let i = left; i <= right; i++) {
      matrix[top][i] = current++
    }

    top++

    for (let i = top; i <= bottom; i++) {
      matrix[i][right] = current++
    }

    right--

    if (left <= right) {
      for (let i = right; i >= left; i--) {
        matrix[bottom][i] = current++
      }
      bottom--
    }

    if (top <= bottom) {
      for (let i = bottom; i >= top; i--) {
        matrix[i][left] = current++
      }

      left++
    }
  }

  return matrix
}
