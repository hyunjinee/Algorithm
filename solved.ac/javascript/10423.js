const fs = require("fs")
const input = fs
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number))

const [[N, M, K], balzunso, ...inputs] = input
let ans = 0
const parent = Array.from({ length: N + 1 }, (v, i) => i)
inputs.sort((a, b) => a[2] - b[2])

for (let i = 0; i < K; i++) {
  parent[balzunso[i]] = -1
}

function find(a) {
  if (parent[a] === a) return a
  return (parent[a] = find(parent[a]))
}

function union(a, b) {
  const parentA = find(a)
  const parentB = find(b)

  parentA > parentB ? (parent[parentA] = parentB) : (parent[parentB] = parentA)
}

function checkCycle(a, b) {
  const parentA = find(a)
  const parentB = find(b)
  if (parentA === parentB) return true
  return false
}

for (const [vertices1, vertices2, cost] of inputs) {
  if (!checkCycle(vertices1, vertices2)) {
    ans += cost
    union(vertices1, vertices2)
  }
}
console.log(ans)
