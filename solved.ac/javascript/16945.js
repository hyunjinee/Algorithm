const fs = require("fs")
const realBoard = fs
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number))
const visited = Array(10).fill(false)

let ans = Infinity

dfs(
  0,
  Array(3)
    .fill()
    .map(() => Array(3).fill(0))
)

function dfs(depth, board) {
  if (depth === 9 && check(board)) {
    let temp = 0

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        temp += Math.abs(board[i][j] - realBoard[i][j])
      }
    }

    ans = Math.min(ans, temp)

    return
  }

  let x = Math.floor(depth / 3)
  let y = depth % 3

  for (let i = 1; i <= 9; i++) {
    if (visited[i]) {
      continue
    }
    visited[i] = true
    board[x][y] = i
    dfs(depth + 1, board)
    board[x][y] = 0
    visited[i] = false
  }
}

function check(board) {
  const sum = board[0].reduce((a, x) => a + x, 0)

  for (let i = 0; i < 3; i++) {
    let temp = 0

    for (let j = 0; j < 3; j++) {
      temp += board[i][j]
    }

    if (temp !== sum) {
      return false
    }
  }

  for (let i = 0; i < 3; i++) {
    let temp = 0

    for (let j = 0; j < 3; j++) {
      temp += board[j][i]
    }

    if (temp !== sum) {
      return false
    }
  }

  let temp = 0

  for (let i = 0; i < 3; i++) {
    temp += board[i][i]
  }

  if (temp !== sum) {
    return false
  }

  temp = 0

  for (let i = 0; i < 3; i++) {
    temp += board[i][2 - i]
  }

  if (temp !== sum) {
    return false
  }

  return true
}

console.log(ans)
