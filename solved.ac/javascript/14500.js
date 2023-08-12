const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, m] = input[0].split(" ").map(Number)
const visited = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => false)
)
const dx = [0, 0, 1, -1],
  dy = [1, -1, 0, 0]
let [_, ...board] = input
let ans = 0,
  maxValue = 0
board = board.map((e) => e.split(" ").map((e) => +e))
board.map((e) =>
  e.map((ee) => {
    if (ee > maxValue) {
      maxValue = ee
    }
  })
)
function dfs(x, y, dep, sum) {
  if (dep == 4) {
    ans = Math.max(ans, sum)
    return
  }
  if (maxValue * (4 - dep) + sum <= ans) return
  for (let i = 0; i < 4; i++) {
    let nx = x + dx[i],
      ny = y + dy[i]
    if (0 <= nx && n > nx && 0 <= ny && ny < m && !visited[nx][ny]) {
      visited[nx][ny] = true
      if (dep === 2) dfs(x, y, dep + 1, sum + board[nx][ny])
      dfs(nx, ny, dep + 1, sum + board[nx][ny])
      visited[nx][ny] = false
    }
  }
}
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    visited[i][j] = 1
    dfs(i, j, 1, board[i][j])
    visited[i][j] = 0
  }
}
console.log(ans)
