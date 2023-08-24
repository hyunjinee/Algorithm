const fs = require("fs")
let inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
inputs = inputs.map((v) => v.split(" ").map(Number))
const visited = Array(n).fill(false)
const dp = Array(n)
  .fill()
  .map(() => Array(17).fill(0))
const tree = Array(n)
  .fill()
  .map(() => [])

for (let i = 0; i < inputs.length; i++) {
  const [a, b] = inputs[i]
  tree[a - 1].push(b - 1)
  tree[b - 1].push(a - 1)
}

dfs(0)

function dfs(here) {
  visited[here] = true

  for (const there of tree[here]) {
    if (visited[there]) continue

    dfs(there)

    for (let i = 0; i < 17; i++) {
      let min = 10000000
      for (let j = 0; j < 17; j++) {
        if (i === j) continue

        min = Math.min(min, dp[there][j])
      }
      dp[here][i] += min
    }
  }
  for (let i = 0; i < 17; i++) {
    dp[here][i] += i + 1
  }

  return
}

console.log(Math.min(...dp[0]))
