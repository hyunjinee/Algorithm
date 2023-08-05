const fs = require("fs")
const inputs = fs
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number))
const [[n, k], arr] = inputs
const counter = Array(Math.max(...arr) + 1).fill(0)

let left = 0,
  right = 0

let ans = -Infinity

while (right < n) {
  if (counter[arr[right]] < k) {
    counter[arr[right]]++
    right++
  } else {
    counter[arr[left]]--
    left++
  }

  ans = Math.max(ans, right - left)
}

console.log(ans)
