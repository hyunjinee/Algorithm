const inputs = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

const [R, C, Q] = inputs[0].split(" ").map(Number)
const arr = inputs.slice(1, R + 1).map((v) => v.split(" ").map(Number))
const testcases = inputs.slice(R + 1).map((v) => v.split(" ").map(Number))
const dp = Array.from(Array(R + 1), () => Array(C + 1).fill(0))
console.log(arr)
for (let i = 1; i < R + 1; i++) {
  for (let j = 1; j < C + 1; j++) {
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i - 1][j - 1]
    console.log(dp)
  }
}

for (const [r1, c1, r2, c2] of testcases) {
  const ans = dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1]
  console.log(Math.floor(ans / ((r2 - r1 + 1) * (c2 - c1 + 1))))
}
