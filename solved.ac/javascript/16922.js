const line = require("fs").readFileSync("/dev/stdin", "utf8")
const input = line.trim().split("\n")
const N = Number(input[0])
const A = [1, 5, 10, 50]
const visit = new Array(50 * N + 1).fill(false)
let ans = 0
const dfs = (num, idx, cnt) => {
  if (cnt === N) {
    if (!visit[num]) {
      ans += 1
      visit[num] = true
    }
    return
  }

  for (let i = idx; i < A.length; i++) {
    dfs(num + A[i], i, cnt + 1)
  }
}

dfs(0, 0, 0)

console.log(ans)

// const fs = require("fs")
// const input = fs.readFileSync("/dev/stdin").toString().trim()
// const N = parseInt(input)

// const data = []

// for (let i = 0; i <= N; i++) {
//   for (let j = 0; j <= N; j++) {
//     if (i + j > N) break
//     for (let k = 0; k <= N; k++) {
//       if (i + j + k > N) break
//       const arr = [i, j, k, N - i - j - k]
//       data.push(arr)
//     }
//   }
// }

// const res = []

// for (let i = 0; i < data.length; i++) {
//   const sum = data[i][0] + data[i][1] * 5 + data[i][2] * 10 + data[i][3] * 50
//   res.push(sum)
// }
// console.log(res.filter((elem, idx) => res.indexOf(elem) === idx).length)
