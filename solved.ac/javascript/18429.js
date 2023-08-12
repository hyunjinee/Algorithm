const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [[n, k], arr] = inputs.map((v) => v.split(" ").map(Number))

// 운동키트는 n일 동안 한번씩만 사용가능 -> 근력 증가
// 하루에 k 씩 근력 감소

const visited = Array(n).fill(false)
let ans = 0

backTracking([], 500)

function backTracking(curr, strength) {
  if (curr.length === n) {
    ans++

    return
  }

  if (strength < 500) {
    return
  }

  for (let i = 0; i < n; i++) {
    if (visited[i]) {
      continue
    }

    if (strength + arr[i] - k >= 500) {
      visited[i] = true
      backTracking(curr.concat(i), strength + arr[i] - k)
      visited[i] = false
    }
  }
}

console.log(ans)
