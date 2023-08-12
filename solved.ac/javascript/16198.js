const inputs = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, arr] = [+inputs[0], inputs.slice(1)[0].split(" ").map(Number)]
let result = -Infinity

function backTracking(cur, sum) {
  result = Math.max(sum, result)
  for (let i = 1; i < cur.length - 1; i++) {
    backTracking(
      cur.filter((x, index) => i !== index),
      cur[i - 1] * cur[i + 1] + sum
    )
  }
}

backTracking(arr, 0)
console.log(result)
