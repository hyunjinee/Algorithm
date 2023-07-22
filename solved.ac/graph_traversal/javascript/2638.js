const fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
let [a, ...board] = input
let [n, m] = a.split(" ").map((e) => +e)
board = board.map((e) => e.split(" ").map((e) => +e))

let dx = [0, 0, 1, -1],
  dy = [1, -1, 0, 0],
  ans = 0
while (true) {
  let q = []
  q.push([0, 0])
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => 0)
  )
  visited[0][0] = 1
  while (q.length) {
    let [x, y] = q.shift()
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i],
        ny = y + dy[i]
      if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] === 0) {
        if (board[nx][ny]) {
          board[nx][ny] += 1
        } else {
          visited[nx][ny] = 1
          q.push([nx, ny])
        }
      }
    }
  }
  let flag = 0
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] >= 3) {
        board[i][j] = 0
      } else if (board[i][j] > 0) {
        flag = 1
        board[i][j] = 1
      }
    }
  }
  ans += 1
  if (!flag) {
    console.log(ans)
    break
  }
}
