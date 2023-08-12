const fs = require("fs")
let inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
inputs = inputs.map(Number).sort((a, b) => a - b)

let result = 0

for (let i = 0; i < inputs.length; i++) {
  result += Math.abs(i + 1 - inputs[i])
}

console.log(result)
