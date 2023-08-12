const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const t = +inputs.shift()

for (let i = 0; i < t; i++) {
  const n = +inputs.shift()
  const days = inputs.shift().split(" ").map(Number)

  let max = 0
  let ans = 0

  for (let i = days.length - 1; i >= 0; i--) {
    if (days[i] > max) {
      max = days[i]
    } else {
      ans += max - days[i]
    }
  }

  console.log(ans)
}
