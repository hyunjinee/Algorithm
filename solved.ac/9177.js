const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const n = +inputs.shift()
inputs.forEach((input, i) => {
  inputs[i] = input.split(" ")
})

let i = 1

for (const [a, b, c] of inputs) {
  const result = Array.from(c)
  const A = Array.from(a)
  const B = Array.from(b)

  let flag = true
  while (result.length) {
    const next = result.shift()

    if (A[0] === next) {
      A.shift()
    } else if (B[0] === next) {
      B.shift()
    } else {
      flag = false
      break
    }
  }

  console.log("Data Set " + i + ": " + (flag ? "yes" : "no"))

  i++
}
