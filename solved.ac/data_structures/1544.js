const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")

const n = +input[0]
const arr = []
let ans = 0
for (let a of input.slice(1)) {
  if (!arr.includes(a)) {
    ans += 1
    for (let i = 0; i < a.length; i++) {
      a = a.slice(1) + a[0]
      if (!arr.includes(a)) arr.push(a)
    }
  }
}

console.log(ans)
