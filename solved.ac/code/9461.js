const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = input.shift()
const a = []
a[0] = 0
a[1] = 1
a[2] = 1
a[3] = 1
// console.log(a)
for (let i = 4; i <= 100; i++) {
  a[i] = a[i - 2] + a[i - 3]
}
for (let i = 0; i < n; i++) {
  console.log(a[input[i]])
}
