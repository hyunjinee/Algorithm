const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
const temp = inputs.slice(0, n - 1).map((v) => v.split(" ").map(Number))
const k = inputs[n - 1]
const arr = inputs.slice(n).map((v) => v.split(" ").map(Number))
const graph = Array(n + 1)
  .fill()
  .map(() => [])

for (const [a, b, c] of temp) {
  graph[a].push([b, c])
  graph[b].push([a, c])
}

for (const [a, b] of arr) {
  solution(a, b)
}

function solution(a, b) {
  const visited = Array(n + 1).fill(false)

  let max = -Infinity
  let min = Infinity

  dfs(a, [])

  console.log(min, max)

  function dfs(x, curr) {
    if (x === b) {
      max = Math.max(max, Math.max(...curr))
      min = Math.min(min, Math.min(...curr))

      return
    }

    for (const [y, cost] of graph[x]) {
      if (visited[y]) continue

      visited[x] = true
      dfs(y, [...curr, cost])
      visited[x] = false
    }
  }
}
