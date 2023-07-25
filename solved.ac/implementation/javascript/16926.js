const inputs = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number))
const [[n, m, r], ...board] = inputs

for (let i = 0; i < r; i++) cycle()
console.log(
  board
    .map((e) => {
      return e.join(" ")
    })
    .join("\n")
)

function cycle() {
  let tmp
  for (let t = 0; t < Math.min(m, n) / 2; t++) {
    tmp = board[t][t]
    for (let i = t; i < m - t - 1; i++) {
      board[t][i] = board[t][i + 1]
    }
    for (let i = t; i < n - t - 1; i++) {
      board[i][m - 1 - t] = board[i + 1][m - 1 - t]
    }
    for (let i = m - 1 - t; i > t; i--) {
      board[n - 1 - t][i] = board[n - 1 - t][i - 1]
    }
    for (let i = n - t - 1; i > t + 1; i--) {
      board[i][t] = board[i - 1][t]
    }
    board[t + 1][t] = tmp
  }
}
