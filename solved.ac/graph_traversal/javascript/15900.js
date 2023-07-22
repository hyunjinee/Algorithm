const fs = require("fs")
const filePath = "./dev/stdin"
const input = fs.readFileSync(filePath).toString().trim().split("\n")
console.log(input)

const N = +input.shift()
const arr = input.map((l) => l.split(" ").map(Number))

const graph = Array.from({ length: N + 1 }, () => new Array())
const visited = Array(N + 1).fill(0)

for (const [x, y] of arr) {
  graph[x].push(y)
  graph[y].push(x)
}

let count = 0
visited[1] = true
dfs(0, 1)

function dfs(L, cur) {
  if (cur !== 1 && graph[cur].length === 1) {
    if (L % 2 === 1) count++
    return
  }

  visited[cur] = 1

  const nextNodes = graph[cur]
  for (const nextNode of nextNodes) {
    if (!visited[nextNode]) {
      dfs(L + 1, nextNode)
    }
  }
}
console.log(count % 2 === 1 ? "Yes" : "No")
