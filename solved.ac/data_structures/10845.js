const [_, ...a] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const q = []
const r = []
for (const s of a) {
  const l = q.length
  s[1] == "u" && q.push(s.split(" ")[1])
  s[1] == "o" && r.push(l ? q.shift() : -1)
  s[1] == "i" && r.push(l)
  s[1] == "m" && r.push(l ? 0 : 1)
  s[1] == "r" && r.push(l ? q[0] : -1)
  s[1] == "a" && r.push(l ? q[l - 1] : -1)
}
console.log(r.join("\n"))

// const input = require("fs")
//   .readFileSync("./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
// const q = []
// for (let i = 1; i < input.length; i++) {
//   if (input[i].slice(0, 4) == "push") {
//     q.push(+input[i].split(" ")[1])
//   } else if (input[i][0] == "f") {
//     if (q.length == 0) {
//       console.log(-1)
//     } else {
//       console.log(q[0])
//     }
//   } else if (input[i].slice(0, 3) == "pop") {
//     if (q.length == 0) {
//       console.log(-1)
//     } else {
//       console.log(q.shift())
//     }
//   } else if (input[i].slice(0, 4) == "size") {
//     console.log(q.length)
//   } else if (input[i].slice(0, 5) == "empty") {
//     if (q.length == 0) {
//       console.log(1)
//     } else {
//       console.log(0)
//     }
//   } else {
//     if (q.length == 0) {
//       console.log(-1)
//     } else {
//       console.log(q[q.length - 1])
//     }
//   }
// }
