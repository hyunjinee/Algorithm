const fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

let n = Number(input[0])

const array = Array(n)
  .fill()
  .map((_, i) => i + 1)

let index = 0
let step = 1

while (n > 1) {
  index = (index + Math.pow(step, 3) - 1) % n
  array.splice(index, 1)

  n -= 1
  step += 1
}

console.log(array[0])

// const fs = require("fs")
// let n = fs.readFileSync("/dev/stdin").toString()

// n = +n

// solution(n)
// function solution(n) {
//   const q = Array(n)
//     .fill()
//     .map((_, i) => i + 1)
//   let level = 1

//   while (q.length > 1) {
//     let t = Math.pow(level, 3)

//     while (t > 0) {
//       t--
//       const temp = q.shift()
//       q.push(temp)
//     }

//     q.pop()
//     level++
//   }

//   console.log(q[0])
// }

// // console.log(solution(3)) // 3
// // console.log(solution(6)) // 6
// // console.log(solution(10)) // 8
