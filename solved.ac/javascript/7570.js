const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const n = +inputs.shift()
const children = inputs[0].split(" ").map(Number)

const dy = Array(n + 1).fill(0)

let max = 0

for (let i = 1; i <= n; i++) {
  const curr = children[i - 1]
  dy[curr] = dy[curr - 1] + 1
  max = Math.max(max, dy[curr])
  console.log(dy)
}
console.log(children)
console.log(dy)
console.log(n - max)
