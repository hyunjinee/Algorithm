const fs = require("fs")
let inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
inputs = inputs.map((v) => v.split(" ").map(Number))
let max = 0

const graph = Array(n + 1)
  .fill()
  .map(() => Array(n + 1).fill(0))

for (const [a, b, c] of inputs) {
  graph[a][b] = c
  graph[b][a] = c
}

function bfs(n) {
  const visited = Array(n + 1).fill(false)
  const dist = Array(n + 1).fill(0)

  const queue = [1]

  while (queue.length) {
    const curr = queue.shift()

    visited[curr] = true

    for (let i = 1; i <= n; i++) {
      if (visited[i] || graph[curr][i] === 0) {
        continue
      }

      queue.push(i)
      dist[i] = dist[curr] + graph[curr][i]
    }
  }

  console.log(Math.max(...dist))
}
bfs(n)
// dfs(1, 0)
// function dfs(root, curr) {
//   if (max < curr) {
//     max = curr
//   }

//   if (graph[root].length === 0) {
//     return
//   }

//   for (const { weight, node } of graph[root]) {
//     if (visited[node]) {
//       continue
//     }

//     visited[node] = true
//     dfs(node, curr + weight)
//     visited[node] = false
//   }
// }

// console.log(max)
