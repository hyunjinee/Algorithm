const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +input[0],
  arr = input[1].split(" ").map(Number),
  visited = Array(arr.reduce((a, c) => a + c, 0) + 2).fill(false)

function backTracking(curr, index) {
  if (index === n) {
    visited[curr] = true
    return
  }

  backTracking(curr + arr[index], index + 1)
  backTracking(curr, index + 1)
}

backTracking(0, 0)
console.log(visited.indexOf(false))

// const readFile = "/dev/stdin"
// let input = require("fs").readFileSync(readFile).toString().split("\n")

// const N = Number(input[0])
// const a = input[1].split(" ").map(Number)
// const c = new Array(N * 100000 + 10).fill(false) //부분합으로 만들 수 있는지 없는지 모두 체크

// function go(i, sum) {
//   //부분합 완성
//   if (i === N) {
//     c[sum] = true
//     return
//   }
//   go(i + 1, sum + a[i])
//   go(i + 1, sum)
// }
// go(0, 0)
// let j = 1
// while (true) {
//   if (!c[j]) break
//   j += 1
// }
// console.log(j)
