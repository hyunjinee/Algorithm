const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [n, q] = inputs.shift().split(" ").map(Number)

console.log(n, q)
