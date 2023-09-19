const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [N, K] = inputs[0].split(" ").map(Number)
