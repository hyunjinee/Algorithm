const fs = require("fs")
const input = fs.readFileSync("./dev/stdin", "utf8").trim().split("\n")

// console.log(input)

const [k, ...a] = input

const ans = []

for (let i = 0; i < a.length; i++) {
  if (+a[i] == 0) {
    ans.pop()
  } else {
    ans.push(a[i])
  }
}

let sum = ans.map((v) => +v).reduce((a, x) => a + x, 0)
console.log(sum)
