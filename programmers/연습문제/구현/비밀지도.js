function solution(n, arr1, arr2) {
  arr1 = arr1
    .map((x) => x.toString(2))
    .map((x) => {
      while (x.length !== n) {
        x = "0" + x
      }
      return x
    })

  arr2 = arr2
    .map((x) => x.toString(2))
    .map((x) => {
      while (x.length !== n) {
        x = "0" + x
      }
      return x
    })

  const board = Array(n)
    .fill("")
    .map((x) => Array(n).fill(" "))

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr1[i][j] == "1" || arr2[i][j] == "1") {
        board[i][j] = "#"
        continue
      }
    }
  }

  return board.map((x) => x.join(""))
}

// "" , "#"
