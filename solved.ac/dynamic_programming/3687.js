const fs = require("fs")
const input = fs
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number)

const N = input.shift()
const answer = []

const Max = (num) => {
  let min = ""
  if (num % 2 == 1) {
    min += "7"
    num -= 3
  }
  const L = num / 2
  for (let i = 0; i < L; i++) {
    min += "1"
  }
  return min
}

const MAX = Math.max(...input)
let minDP = new Array(MAX + 1).fill(Infinity)
minDP[2] = 1
minDP[3] = 7
minDP[4] = 4
minDP[5] = 2
minDP[6] = 6
minDP[7] = 8

const matches = [, , "1", "7", "4", "2", "0", "8"]
for (let i = 8; i <= MAX; i++) {
  for (let j = 2; j < 8; j++) {
    if (i - j < 2) continue
    minDP[i] = Math.min(minDP[i], Number(`${minDP[i - j]}` + matches[j]))
  }
}

for (let i = 0; i < N; i++) {
  const num = input[i]
  answer.push(`${minDP[num]} ${Max(num)}`)
}

console.log(answer.join("\n"))
