const fs = require("fs")
const num = fs.readFileSync("/dev/stdin").toString().trim()

let left = 0,
  right = 0

for (let i = 0; i < num.length / 2; i++) {
  left += +num[i]
  right += +num[num.length - i - 1]
}
console.log(left === right ? "LUCKY" : "READY")
