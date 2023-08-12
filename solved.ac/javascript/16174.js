const [[n], ...board] = require("fs")
    .readFileSync("./dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map((V) => V.split(" ").map(Number)),
  q = [[0, 0]]

while (q.length) {
  const [y, x] = q.shift()

  if (x === n - 1 && y === n - 1) {
    console.log("HaruHaru")
    process.exit()
  }

  const jump = board[y][x]
  board[y][x] = 0

  if (x + jump < n && board[y][x + jump] !== 0) {
    q.push([y, x + jump])
  }

  if (y + jump < n && board[y + jump][x] !== 0) {
    q.push([y + jump, x])
  }
}

console.log("Hing")
