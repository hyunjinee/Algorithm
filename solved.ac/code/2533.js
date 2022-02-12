const fs = require("fs")
const input = fs.readFileSync("./dev/stdin", "utf8").trim().split("\n")

console.log(input)
const n = +input[0]
const root = 1
const arrFrom = { length: n + 1 }
const con = Array.from(arrFrom, () => [])
const dp = Array.from(arrFrom, () => [0, 1])
console.log(dp)
const visit = Array(n + 1).fill(false)
console.log(visit)
for (let i = 1; i < n; i += 1) {
  const [node1, node2] = input[i].split(" ")
  con[node1].push(node2)
  con[node2].push(node1)
}

const dfs = (node) => {
  visit[node] = true
  for (let i = 0, l = con[node].length; i < l; i += 1) {
    const child = con[node][i]

    if (visit[child]) continue
    dfs(child)

    dp[node][0] += dp[child][1]
    dp[node][1] += Math.min(dp[child][0], dp[child][1])
  }
}

dfs(root)

const ans = Math.min(dp[root][0], dp[root][1])
console.log(ans)
// dfs(root)
// const ans = Math.min(dp[root][0], dp[root][1])

// console.log(ans)
