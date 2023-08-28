const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const board = Array.from({ length: 8 }, () => Array.from({ length: 8 }, () => 0))
const alpha = "ABCDEFGH"
let [ky, kx, n] = inputs.shift().split(" ")

const currKing = [7 - (+ky[1] - 1), alpha.indexOf(ky[0])]
const currStone = [7 - (+kx[1] - 1), alpha.indexOf(kx[0])]

const move = {
  R: [0, 1],
  L: [0, -1],
  B: [1, 0],
  T: [-1, 0],
  RT: [-1, 1],
  LT: [-1, -1],
  RB: [1, 1],
  LB: [1, -1],
}

const isSafe = (y, x) => y >= 0 && y <= 7 && x >= 0 && x <= 7

for (const input of inputs) {
  const [dy, dx] = move[input]
  const [ny, nx] = [currKing[0] + dy, currKing[1] + dx]

  if (!isSafe(ny, nx)) continue

  if (ny === currStone[0] && nx === currStone[1]) {
    const [sy, sx] = [currStone[0] + dy, currStone[1] + dx]

    if (!isSafe(sy, sx)) continue

    currStone[0] = sy
    currStone[1] = sx
  }

  currKing[0] = ny
  currKing[1] = nx
}

console.log(String(alpha[currKing[1]]) + String(8 - currKing[0]))
console.log(String(alpha[currStone[1]]) + String(8 - currStone[0]))
