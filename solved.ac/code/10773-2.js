const query = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")

const stack = []

for (let i = 1; i < query.length; i++) {
  const v = +query[i]
  v === 0 ? stack.pop() : stack.push(v)
}

console.log(stack.reduce((a, x) => a + x, 0))
