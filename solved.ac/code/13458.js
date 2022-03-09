const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
function solution(input) {
  const n = input.shift()
  console.log(input)
  const [main, sub] = input[1].split(" ").map((e) => Number(e))
  const exam = input[0].split(" ").map((e) => Number(e) - main)
  let answer = Number(n)
  exam.forEach((e) => {
    if (e > 0) {
      answer += Math.ceil(e / sub)
    }
  })
  console.log(answer)
}
solution(input)

//   exam.forEach((e) => {
//     if (e > 0) {
//       answer += Math.ceil(e / sub)
//     }
//   })
//   console.log(answer)
// }

// solution(input)
