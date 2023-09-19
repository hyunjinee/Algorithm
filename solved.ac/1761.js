const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const n = +inputs.shift()

const edges = inputs.slice(0, n - 1).map((x) => x.split(" ").map(Number))
const aTob = inputs.slice(n).map((x) => x.split(" ").map(Number))
console.log(edges, aTob)

const graph = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () => []))

for (const [a, b, c] of edges) {
  graph[a].push([b, c])
  graph[b].push([a, c])
}

for (const [a, b] of aTob) {
}

function dfs(start, end, visited = Array(n + 1).fill(false), distance = Array(n + 1).fill(Infinity)) {
  for (const [next, cost] of graph[start]) {
    if (visited[next]) continue

    visited[start] = true
    dfs(next, end, visited)
    visited[start] = false
  }
}
