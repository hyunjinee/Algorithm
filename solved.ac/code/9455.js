const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) =>
    x
      .trim()
      .split(" ")
      .map((x) => +x)
  )

const T = +input.shift()
for (let t = 0; t < T; t++) {
  const [m, n] = input.shift()
  let distance = 0
  for (let j = 0; j < n; j++) {
    let check = 0
    for (let i = 0; i < m; i++) {
      if (input[i][j]) {
        check++
      } else {
        distance += check
      }
    }
  }
  console.log(distance)
  input.splice(0, m)
  // console.log(input)
}
