const fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().trim()

console.log(
  input.indexOf("d2") != -1 || input.indexOf("D2") != -1 ? "D2" : "unrated"
)

// if (input.includes("d2")) {
//   console.log("D2")
// } else if (input.includes("D2")) {
//   console.log("d2")
// } else {
//   console.log("unrated")
// }
