const [s, _, ...inputs] = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

const map = new Map()
const answer = []

for (const input of inputs) {
  let [alphabet, start, end] = input.split(" ")
  start = Number(start)
  end = Number(end)
  console.log(alphabet, start, end)
  if (!map.has(alphabet)) {
    let temp = Array(s.length + 1).fill(0)
    for (let i = 0; i < s.length; i++) {
      let sum = s[i] === alphabet ? 1 : 0
      temp[i + 1] = temp[i] + sum
    }
    map.set(alphabet, temp)
  }
  answer.push(map.get(alphabet)[end + 1] - map.get(alphabet)[start])
}

console.log(answer)
