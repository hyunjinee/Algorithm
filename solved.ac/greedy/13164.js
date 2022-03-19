//https://hyunjinee.tistory.com/32
const inputs = require("fs").readFileSync("./dev/stdin").toString().split("\n")
let [n, k] = inputs[0].split(" ").map(Number)
let heights = inputs[1].split(" ").map(Number)
let diff = []
for (let i = 1; i < n; i++) {
  diff.push(heights[i] - heights[i - 1])
}
diff.sort((a, b) => b - a)
diff = diff.slice(k - 1)
const ans = diff.reduce((acc, cur) => acc + cur, 0)
console.log(ans)
