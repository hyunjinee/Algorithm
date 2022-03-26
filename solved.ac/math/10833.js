const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +input[0]
const arr = input.slice(1).map((e) => e.split(" ").map((e) => +e))
let _sum = 0
for (let [a, b] of arr) {
  _sum += b % a
}
console.log(_sum)
