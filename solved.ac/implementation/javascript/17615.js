//

const fs = require("fs")
const filePath = process.platform === "linux" ? "./dev/stdin" : "./dev/stdin"
const input = fs.readFileSync(filePath).toString()

const lines = input.split("\n")
const data = lines[1].split("")

let result = Number.MAX_SAFE_INTEGER

// 빨간 공
let count = 0
for (let i = 0; i < data.length; i++) {
  if (data[i] !== "R") {
    while (i < data.length) {
      if (data[i] === "R") count += 1
      i += 1
    }
  }
}
result = count
console.log(data)

count = 0
for (let i = data.length - 1; i >= 0; i--) {
  if (data[i] !== "R") {
    while (i >= 0) {
      if (data[i] === "R") count += 1
      i -= 1
    }
  }
}
result = Math.min(result, count)
console.log(data)

// 파란 공
count = 0
for (let i = 0; i < data.length; i++) {
  if (data[i] !== "B") {
    while (i < data.length) {
      if (data[i] === "B") count += 1
      i += 1
    }
  }
}
result = Math.min(result, count)

count = 0
for (let i = data.length - 1; i >= 0; i--) {
  if (data[i] !== "B") {
    while (i >= 0) {
      if (data[i] === "B") count += 1
      i -= 1
    }
  }
}
result = Math.min(result, count)

console.log(result)
// const { exit } = require("process")
// const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

// const n = +input[0],
//   balls = input[1]

// if (balls.replaceAll("R", "").length === 0 || balls.replaceAll("B", "").length === 0) {
//   console.log(0)

//   exit(0)
// }

// const check = (str, ball) => {
//   let check = false
//   let count = 0

//   for (let i = 0; i < str.length; i++) {
//     if (str[i] === ball) {
//       check = true
//     }

//     if (check && str[i] !== ball) {
//       count++
//     }
//   }
//   console.log(count, "count")
//   return count
// }

// let result = Math.min(
//   check(balls, "R"),
//   check(balls, "B"),
//   check(balls.split("").reverse().join(""), "R"),
//   check(balls.split("").reverse().join(""), "B")
// )

// console.log(result)
