const [info, ...data] = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const [V, E, begin] = info.split(" ").map(Number)

const graph = Array.from(Array(V + 1), () => [])

for (let edge of data) {
  const [from, to] = edge.split(" ").map(Number)
  graph[from].push(to)
  graph[to].push(from)
}
graph.forEach((nodes) => nodes.sort((a, b) => b - a))
const visited = Array(V + 1).fill(0)
let depth = 1

const DFS = (begin) => {
  visited[begin] = depth
  for (let dest of graph[begin]) {
    if (visited[dest]) continue
    depth += 1
    DFS(dest)
  }
}
DFS(begin)

console.log(visited.slice(1).join("\n"))

// // const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

// // const [n, m, r] = input[0].split(" ").map(Number)
// // const edges = input.slice(1).map((v) => v.split(" ").map(Number))

// // const graph = {}

// // for (const [s, e] of edges) {
// //   if (!graph[s]) {
// //     graph[s] = []
// //   }
// //   if (!graph[e]) {
// //     graph[e] = []
// //   }
// //   graph[s].push(e)
// //   graph[e].push(s)
// // }

// // Object.values(graph).forEach((v) => v.sort((a, b) => b - a))
// // const visited = Array(n + 1).fill(0)

// // let count = 0
// // function dfs(curr) {
// //   visited[curr] = ++count

// //   for (const next of graph[curr]) {
// //     if (!visited[next]) {
// //       dfs(next)
// //     }
// //   }
// // }

// // dfs(r)
// // console.log(visited.slice(1).join("\n"))

// const fs = require("fs")
// const [nums, ...arr] = fs
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((el) => el.split(" ").map(Number))

// const [N, M, R] = nums
// let count = 0
// const visited = Array(N + 1).fill(0)
// const points = Array(N + 1)
//   .fill(null)
//   .map((_) => [])
// arr.forEach((el) => {
//   const [from, to] = el
//   points[from].push(to)
//   points[to].push(from)
// })

// const sortedPoints = points.map((el) => el.sort((a, b) => b - a))

// const dfs = (x) => {
//   if (!visited[x]) {
//     visited[x] = ++count
//     for (const next of points[x]) {
//       dfs(next)
//     }
//   }
// }

// dfs(R)

// console.log(visited.slice(1).join("\n"))
