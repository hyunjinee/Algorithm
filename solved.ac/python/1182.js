const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, s] = input[0].split(" ").map((e) => +e)
lst = input[1].split(" ").map((e) => +e)
let ans = 0
function dfs(idx, sum) {
  if (idx >= n) {
    return
  }
  sum += lst[idx]
  if (sum === s) {
    ans += 1
  }
  dfs(idx + 1, sum)
  dfs(idx + 1, sum - lst[idx])
}

dfs(0, 0)

console.log(ans)
