const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const k = +inputs.shift()
const str = inputs.shift()
let board = Array(str.length / k)
  .fill()
  .map(() => Array(k).fill())

for (let i = 0; i < str.length; i++) {
  let x = Math.floor(i / k)
  let y = i % k
  board[x][y] = str[i]
}

board = board.map((row, i) => {
  if (i % 2 === 1) {
    return row.reverse()
  } else {
    return row
  }
})

let ans = ""

for (let i = 0; i < board[0].length; i++) {
  for (let j = 0; j < board.length; j++) {
    if (board[j][i]) {
      ans += board[j][i]
    }
  }
}

console.log(ans)
