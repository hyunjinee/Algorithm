const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +input[0]
const board = input.slice(1).map((e) => e.split(" ").map((e) => +e))
const max = Math.max(...board.flat())
let dx = [0, 0, 1, -1],
  dy = [1, -1, 0, 0]
function bfs(x, y, h, visited) {
  const q = [[x, y]]
  while (q.length) {
    const [x, y] = q.shift()
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i],
        ny = y + dy[i]
      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue
      if (board[nx][ny] > h && !visited[nx][ny]) {
        visited[nx][ny] = true
        q.push([nx, ny])
      }
    }
  }
}
let i = 0,
  ans = 0
while (i <= max) {
  let cnt = 0
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => false)
  )
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      if (!visited[x][y] && board[x][y] > i) {
        bfs(x, y, i, visited)
        cnt += 1
      }
    }
  }
  i++
  ans = Math.max(cnt, ans)
}
console.log(ans)
