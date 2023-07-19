const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const k = +inputs[0],
  arr = inputs[1].split(" ").map(Number),
  sum = arr.reduce((a, c) => a + c, 0),
  visited = Array(sum + 1).fill(false)

const backTracking = (index, weight) => {
  if (index === k) {
    if (weight >= 0) {
      visited[weight] = true
    }
    return
  }
  backTracking(index + 1, weight + arr[index])
  backTracking(index + 1, weight - arr[index])
  backTracking(index + 1, weight)
}
backTracking(0, 0)
console.log(visited.reduce((a, c) => (c === false ? a + 1 : a), 0))
