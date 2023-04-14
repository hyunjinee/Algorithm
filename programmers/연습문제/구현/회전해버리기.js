const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

function rotate(arr) {
  const result = Array(arr.length)
    .fill()
    .map(() => Array(arr.length).fill(0))
  // console.log(result)

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      result[j][arr.length - i - 1] = arr[i][j]
      // result[i][j] = arr[j][arr.length - i - 1]
    }
  }

  console.log(result)

  return result
}

rotate(arr)
