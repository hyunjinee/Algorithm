const readFile = "./dev/stdin"
let input = require("fs").readFileSync(readFile).toString().split("\n")

const k = parseInt(input[0])
const buildings = input[1].split(" ").map(Number)

console.log(k, buildings)

const levels = new Array(k)
for (let i = 0; i < k; i++) levels[i] = []

function solve(start, end, i) {
  const root = parseInt((end + start) / 2)
  console.log(root, "root")
  levels[i].push(buildings[root])
  if (start >= end) {
    return
  }
  solve(start, root - 1, i + 1)
  solve(root + 1, end, i + 1)
}
solve(0, buildings.length - 1, 0)

for (let i = 0; i < k; i++) console.log(levels[i].join(" "))
// const levels = new Array(k)

// function solve(start, end, i) {
//   const root = parseInt((end + start) / 2)
//   levels[i].push(buildings[root])
//   if (start >= end) return
//   solve(start, root - 1, i + 1)
//   solve(root + 1, end, i + 1)
// }

// solve(0, buildings.length - 1, 0)
// for (let i = 0; i < k; i++) console.log(levels[i].join(" "))
