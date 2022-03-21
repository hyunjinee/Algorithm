const fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
let [n, m] = input
const graph = Array.from({ length: +n + 1 }, () =>
  Array.from({ length: +n + 1 }, () => 0)
)
const edges = input.slice(2).map((x) => x.split(" ").map((x) => +x))
for ([a, b] of edges) {
  graph[a][b] = 1
}
for (let k = 1; k <= n; k++) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (graph[i][k] && graph[k][j]) {
        graph[i][j] = 1
      }
    }
  }
}
for (let i = 1; i <= n; i++) {
  let cnt = 0
  for (let j = 1; j <= n; j++) {
    if (!graph[i][j] && !graph[j][i]) cnt++
  }
  console.log(cnt - 1)
}
