const input = require("fs")
  .readFileSync("./dev/stdin", "utf8")
  .toString()
  .trim()

const [n, m] = input.split(" ")
console.log(n, m)
