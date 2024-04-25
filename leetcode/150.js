/**
 * @param {string[]} tokens
 * @return {number}
 */
const evalRPN = function (tokens) {
  const stack = []

  for (const token of tokens) {
    if (!isNaN(parseInt(token))) {
      stack.push(parseInt(token))
    } else {
      let num2 = stack.pop()
      let num1 = stack.pop()

      switch (token) {
        case "+":
          stack.push(num1 + num2)
          break
        case "-":
          stack.push(num1 - num2)
          break
        case "*":
          stack.push(num1 * num2)
          break
        case "/":
          stack.push(parseInt(num1 / num2))
          break
      }
    }
  }

  return stack.pop()
}
