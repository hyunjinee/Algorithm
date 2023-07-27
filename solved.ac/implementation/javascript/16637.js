const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.trim())
const log = console.log

function solution(N, test) {
  const calculate = (num1, num2, order) => {
    switch (order) {
      case "+":
        return num1 + num2
      case "-":
        return num1 - num2
      case "*":
        return num1 * num2
    }
  }

  let MAX = -Infinity
  const deque = [[0, +test[0]]]
  console.log(deque, "?")

  while (deque.length) {
    const [idx, total] = deque.shift()
    if (idx === N - 1) {
      MAX = Math.max(MAX, total)
      continue
    }
    if (idx + 2 < N) {
      deque.push([idx + 2, calculate(total, +test[idx + 2], test[idx + 1])])
    }
    if (idx + 4 < N) {
      const tmp = calculate(+test[idx + 2], +test[idx + 4], test[idx + 3])
      deque.push([idx + 4, calculate(total, tmp, test[idx + 1])])
    }
  }

  return MAX
}

log(solution(+input[0], input[1]))
