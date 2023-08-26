const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [x, y, w, s] = inputs[0].split(" ").map(Number)

const curr = [0, 0]

let move1 = (x + y) * w
let move2
if ((x + y) % 2 === 0) {
  move2 = Math.max(x, y) * s
} else {
  move2 = (Math.max(x, y) - 1) * s + w
}
const move3 = Math.min(x, y) * s + (Math.max(x, y) - Math.min(x, y)) * w
const res = Math.min(move1, move2, move3)

console.log(res)
