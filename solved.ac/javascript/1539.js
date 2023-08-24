const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n").map(Number)
const n = inputs.shift()

let ans = 1

const root = {
  value: inputs[0],
}

for (let i = 1; i < inputs.length; i++) {
  const value = inputs[i]

  insert(value)
}

function insert(value) {
  let curr = root
  let temp = 1

  while (true) {
    temp++
    if (value < curr.value) {
      if (!curr.left) {
        curr.left = { value }
        break
      } else {
        curr = curr.left
      }
    } else {
      if (!curr.right) {
        curr.right = { value }
        break
      } else {
        curr = curr.right
      }
    }
  }

  ans += temp
}

console.log(ans)
