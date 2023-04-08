const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]
function rotate(arr) {
  const N = arr.length
  const result = Array.from(Array(N), () => Array(N).fill(0))

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      console.log(i, j)
      console.log(j, N - 1 - i)
      result[j][N - 1 - i] = arr[i][j]
    }
  }

  return result
}

console.log(rotate(arr))
