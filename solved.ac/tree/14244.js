const [N, M] = require("fs").readFileSync("./dev/stdin").toString().trim().split(" ").map(Number)

const answer = []

for (let i = 0; i < M - 1; i++) {
  answer.push(i + " " + (M - 1))
}

// console.log(answer)
for (let i = M - 1; i < N - 1; i++) {
  answer.push(i + " " + (i + 1))
}
console.log(answer.join("\n"))
