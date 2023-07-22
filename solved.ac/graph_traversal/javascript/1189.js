const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
const [r, c, k] = input[0].split(" ")
const dy = [-1, 0, 1, 0],
  dx = [0, 1, 0, -1]
const visited = Array.from({ length: r }, () =>
  Array.from({ length: c }, () => false)
)
const board = input.slice(1)
let ans = 0

function dfs(y, x, cnt) {
  if (cnt == k && y == 0 && x == c - 1) {
    ans += 1
    return
  }

  for (let i = 0; i < 4; i++) {
    let ny = y + dy[i],
      nx = x + dx[i]
    if (
      0 <= ny &&
      ny < r &&
      0 <= nx &&
      nx < c &&
      !visited[ny][nx] &&
      board[ny][nx] != "T"
    ) {
      visited[ny][nx] = true
      dfs(ny, nx, cnt + 1)
      visited[ny][nx] = false
    }
  }
}
visited[r - 1][0] = true
dfs(r - 1, 0, 1)
console.log(ans)
