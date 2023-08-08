const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, m, k] = input.slice(0, 1)[0].split(" ").map(Number)
const board = input.slice(1)
const visited = Array.from({ length: n }, () => Array.from({ length: m }, () => false))
const startDistance = 1
const isValid = (y, x) => 0 <= y && y < n && 0 <= x && x < m
const dy = [-1, 0, 1, 0],
  dx = [0, 1, 0, -1]
let q = [[0, 0, k, startDistance]]

let minDistance = Infinity

const [y, x, kk, distance] = q
while (q.length) {
  let temp = []

  for (const [y, x, kk, distance] of q) {
    if (y == n - 1 && x == m - 1) {
      minDistance = Math.min(minDistance, distance)
      continue
    }

    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i],
        nx = x + dx[i]

      if (isValid(ny, nx) && !visited[ny][nx] && board[ny][nx] == "0") {
        visited[ny][nx] = true
        temp.push([ny, nx, kk, distance + 1])
      } else if (isValid(ny, nx) && !visited[ny][nx] && board[ny][nx] == "1" && kk > 0) {
        visited[ny][nx] = true
        temp.push([ny, nx, kk - 1, distance + 1])
      }
    }
  }
  q = temp
}

console.log(minDistance === Infinity ? -1 : minDistance)
