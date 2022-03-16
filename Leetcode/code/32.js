var longestValidParentheses = function (s) {
  let stack = [-1]
  let max = 0

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i)
      continue
    }

    stack.pop()

    if (!stack.length) {
      stack.push(i)
    } else {
      max = Math.max(max, i - stack[stack.length - 1])
    }
  }

  return max
}
