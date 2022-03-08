const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
const arr = input[1].split(" ")
const stack = []
for (let i = 0; i < +arr.length; i++) {
  while (+arr[i] > +arr[stack[stack.length - 1]] && stack.length !== 0) {
    arr[stack.pop()] = arr[i]
  }
  stack.push(i)
}
while (stack.length !== 0) {
  arr[stack.pop()] = -1
}
console.log(arr.join(" "))
