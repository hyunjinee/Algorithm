const input = require("fs").readFileSync("./dev/stdin").toString().trim()

let answer = 0
for (let i = 0; i < input.length; i++) {
  if (i == 0) {
    answer += 10
  } else if (input[i] == input[i - 1]) {
    answer += 5
  } else {
    answer += 10
  }
}

console.log(answer)
