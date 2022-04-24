const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
const n = +input[0]
const m = input[1].split(" ").map(Number)
const visited = Array.from({ length: n }, () => false)
const explore = []
let max = 0
function dfs(depth) {
  if (depth == n) {
    let temp = 0
    for (let i = 0; i < n - 1; i++) {
      temp += Math.abs(explore[i] - explore[i + 1])
    }

    if (temp > max) max = temp
  }
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      visited[i] = true
      explore.push(m[i])
      dfs(depth + 1)
      visited[i] = false
      explore.pop()
    }
  }
}
dfs(0)
console.log(max)
