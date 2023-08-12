let s = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")[1]
let x = s.match(/[\d]{1,}/g)
if (x === null) {
  console.log(0)
} else {
  console.log(
    x.reduce(function (prev, curr) {
      return prev + parseInt(curr)
    }, 0)
  )
}
