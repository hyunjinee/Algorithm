const input = require("fs").readFileSync("./dev/stdin").toString().trim()
let a = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for (let i = 1; i < +input; i++) {
  const b = [a[1]]
  for (let j = 1; j < 9; j++) {
    b.push((a[j - 1] + a[j + 1]) % 1000000000)
  }
  b.push(a[8])
  console.log(b)
  a = b
}

console.log(a.reduce((e, c) => e + c, 0) % 1000000000)
