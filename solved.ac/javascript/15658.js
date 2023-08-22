const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

const N = parseInt(input[0])
const nums = input[1].split(" ").map(Number)
const operator = input[2].split(" ").map(Number)

let max = -Infinity
let min = Infinity

function dfs(k, value) {
  if (k === N - 1) {
    max = Math.max(max, value)
    min = Math.min(min, value)

    return
  }

  for (let i = 0; i <= 3; i++) {
    if (operator[i] >= 1) {
      operator[i]--
      let newValue = value
      if (i === 0) newValue += nums[k + 1]
      if (i === 1) newValue -= nums[k + 1]
      if (i === 2) newValue *= nums[k + 1]
      if (i === 3) newValue = parseInt(newValue / nums[k + 1])
      dfs(k + 1, newValue)
      operator[i]++
    }
  }
}

dfs(0, nums[0])
console.log(`${max}\n${min}`)
