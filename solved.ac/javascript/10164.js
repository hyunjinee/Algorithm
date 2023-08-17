const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, m, k] = inputs[0].split(" ").map(Number)
let count = 1
const board = Array(n)
  .fill()
  .map(() =>
    Array(m)
      .fill()
      .map((_) => count++)
  )

let ans = 0

const dy = [0, 1]
const dx = [1, 0]
const visited = Array(n)
  .fill()
  .map(() => Array(m).fill(false))
visited[0][0] = true

// console.log(board)

dfs([0, 0], [1])

function dfs(curr, arr) {
  if (curr[0] === n - 1 && curr[1] === m - 1) {
    if (k === 0) ans++
    if (arr.includes(k)) ans++

    return
  }

  for (let i = 0; i < 2; i++) {
    const [ny, nx] = [curr[0] + dy[i], curr[1] + dx[i]]
    if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue
    if (visited[ny][nx]) continue

    visited[ny][nx] = true
    arr.push(board[ny][nx])
    dfs([ny, nx], arr)
    arr.pop()
    visited[ny][nx] = false
  }
}

console.log(ans)
