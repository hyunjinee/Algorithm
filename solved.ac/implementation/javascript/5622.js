const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString().trim()
const arr = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
let cnt = 0

for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < input.length; j++) {
    if (arr[i].includes(input[j])) cnt += i + 3
  }
}

console.log(cnt)
