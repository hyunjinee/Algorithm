const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()

const dp = Array(33334)
  .fill()
  .map((_) => Array(3).fill(0))

dp[1][0] = 0
dp[1][1] = 0
dp[1][2] = 0

dp[2][0] = 2
dp[2][1] = 2
dp[2][2] = 2

const MOD = 1000000009

for (let i = 3; i <= n; i++) {
  dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
  dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
  dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
}

console.log(dp[n][0] % MOD)
