const input = require("fs")
  .readFileSync("./dev/stdin", "utf8")
  .trim()
  .split("\n")
const [n, s, m] = input[0].split(" ").map(Number)
const arr = input[1].split(" ").map(Number)
arr.unshift("temp")
const dp = Array.from(Array(n + 1), () => new Array(m + 1).fill(0))
dp[0][s] = 1
for (let i = 1; i <= n; i++) {
  for (let j = 0; j <= m; j++) {
    if (dp[i - 1][j] == 1) {
      if (j + arr[i] <= m) dp[i][j + arr[i]] = 1
      if (j - arr[i] >= 0) dp[i][j - arr[i]] = 1
    }
  }
}
const idx = dp[n].reverse().indexOf(1)
console.log(idx >= 0 ? m - idx : -1)

// for (let i = 1; i <= N; i++) {
//     for (let j = 0; j <= M; j++) {
//         if (dp[i - 1][j] === 1) {
//             if (j + arr[i] <= M) dp[i][j + arr[i]] = 1;
//             if (j - arr[i] >= 0) dp[i][j - arr[i]] = 1;
//         }
//     }
// }

// const idx = dp[N].reverse().indexOf(1);
// console.log(idx >= 0 ? M - idx : -1);
