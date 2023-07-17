const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const infos = input.slice(1).map((str) => str.split(" ").map(Number))

console.log(infos)
function solution() {
  let t = 0
  while (1) {
    let N = +input.shift()
    if (N == 0) break
    let g = input.splice(0, N).map((str) => str.split(" ").map(Number))
    let dp = Array.from({ length: N }, () => Array(3).fill(Infinity))
    dp[0] = [Infinity, g[0][1], g[0][2] + g[0][1]]
    for (let i = 1; i < N; i++) {
      dp[i][0] = Math.min(dp[i - 1][0], dp[i - 1][1]) + g[i][0]
      dp[i][1] = Math.min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + g[i][1]
      dp[i][2] = Math.min(dp[i][1], dp[i - 1][1], dp[i - 1][2]) + g[i][2]
    }
    console.log(++t + ". " + dp[N - 1][1])
  }
}

solution()
