const [a, b, n, m] = require("fs").readFileSync("./dev/stdin").toString().trim().split(" ").map(Number)
const queue = [[n, 0]]
const visited = Array(100001).fill(false)

visited[n] = true

while (queue.length) {
  const [current, count] = queue.shift()

  if (current === m) {
    console.log(count)
    break
  }

  for (const next of [
    current - 1,
    current + 1,
    current - a,
    current + a,
    current - b,
    current + b,
    a * current,
    b * current,
  ]) {
    if (next < 0 || next > 100000 || visited[next]) continue
    visited[next] = true
    queue.push([next, count + 1])
  }
}
