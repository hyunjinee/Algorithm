const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [N, d, k, c] = inputs[0].split(" ").map(Number)
const sushis = inputs.slice(1).map(Number)

const newSushi = [...sushis, ...sushis]

let max = -Infinity

for (let i = 0; i < N; i++) {
  const sushi = newSushi.slice(i, i + k)
  const set = new Set(sushi)

  if (!set.has(c)) {
    set.add(c)
  }

  max = Math.max(max, set.size)
}

console.log(max)
