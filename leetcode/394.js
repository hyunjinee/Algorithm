/**
 * @param {string} s
 * @return {string}
 */
const decodeString = function (s) {
  const stack = []
  let num = 0
  let str = ""

  for (const char of s) {
    if (char === "[") {
      stack.push(str)
      stack.push(num)
      num = 0
      str = ""
    } else if (Number.isInteger(Number(char))) {
      num = num * 10 + Number(char)
    } else if (char === "]") {
      let prevNum = stack.pop()
      let prevStr = stack.pop()
      str = prevStr + str.repeat(prevNum)
    } else {
      str += char
    }
  }

  return str
}

decodeString("3[a]2[bc]") // 'aaabcbc'
decodeString("3[a2[c]]") // 'accaccacc'
decodeString("2[abc]3[cd]ef") // 'abcabccdcdcdef'
