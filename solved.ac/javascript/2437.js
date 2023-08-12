const fs = require("fs")
let [_, ...arr] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")
arr = arr[0].split(" ").map((e) => Number(e))

const solution = () => {
  arr = arr.sort((a, b) => a - b)

  let target = 1
  for (let num of arr) {
    if (target < num) {
      return target
    }
    target += num
  }
  return target
}

console.log(solution())
