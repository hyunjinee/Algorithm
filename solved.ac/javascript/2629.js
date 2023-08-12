const [wLen, w, mLen, m] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
const weights = w.split(" ").map(Number)
const marvels = m.split(" ").map(Number)
const dp = Array.from(Array(Number(wLen + 1)), () =>
  Array(Number(15001)).fill(false)
)
const res = new Array(15001)
function check(i, w) {
  if (i > wLen) return
  if (dp[i][w]) return
  dp[i][w] = true
  res[w] = true
  check(i + 1, w)
  check(i + 1, w + weights[i])
  check(i + 1, Math.abs(w - weights[i]))
}
check(0, 0)
let ans = ""
marvels.forEach((mv) => {
  ans += res[mv] ? "Y " : "N "
})

console.log(ans)
