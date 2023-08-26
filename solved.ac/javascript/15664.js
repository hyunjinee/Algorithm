const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [n, m] = inputs[0].split(" ").map(Number)
const nums = inputs[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b)

const set = new Set()

const visited = Array(n).fill(false)

backTracking([])

function backTracking(curr, index = 0) {
  console.log(curr)
  if (curr.length === m) {
    const str = curr.sort((a, b) => a - b).join(" ")
    if (!set.has(str)) {
      set.add(str)
      console.log(str)
    }
    return
  }

  for (let i = 0; i < n; i++) {
    if (visited[i]) continue

    visited[i] = true
    backTracking([...curr, nums[i]])
    visited[i] = false
  }
}
