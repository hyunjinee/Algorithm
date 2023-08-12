const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

let index = 0
const frames = +inputs[index++]
const students = +inputs[index++]
const votes = inputs[index].split(" ").map(Number)
const results = {}

votes.forEach((v, t) => {
  if (results[v]) {
    results[v].count++
  } else {
    if (frames !== Object.keys(results).length) {
      if (results[v] === undefined) {
        results[v] = { count: 1, time: t }
      }
    } else {
      const mins = Object.keys(results).sort(
        (a, b) => results[a].count - results[b].count || results[a].time - results[b].time
      )
      delete results[mins[0]]
      results[v] = { count: 1, time: t }
    }
  }
})

console.log(
  Object.keys(results)
    .sort((a, b) => a - b)
    // .sort((a, b) => b.count - a.count)
    .join(" ")
)

// const fs = require("fs")
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

// const N = input[0]
// const arr = input[2].split(" ").map((v) => +v)
// const stack = []
// const num = []

// arr.forEach((v) => {
//   const index = stack.indexOf(v)
//   if (index > -1) {
//     num[index]++
//   } else if (stack.length < N) {
//     stack.push(v)
//     num.push(1)
//   } else {
//     const min = Math.min(...num)
//     const j = num.indexOf(min)
//     num.splice(j, 1)
//     stack.splice(j, 1)
//     num.push(1)
//     stack.push(v)
//   }
// })

// console.log(stack.sort((a, b) => a - b).join(" "))
