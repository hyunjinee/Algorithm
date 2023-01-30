var isValid = function (s) {
  const temp = []

  Array.from(s).forEach((char) => {
    if (temp.length === 0) {
      temp.push(char)
    } else if (char === "{" || char === "(" || char === "[") {
      temp.push(char)
    } else if (char === "}" || char === ")" || char === "]") {
      if (temp[temp.length - 1] === "{" && char === "}") {
        temp.pop()
      } else if (temp[temp.length - 1] === "(" && char === ")") {
        temp.pop()
      } else if (temp[temp.length - 1] === "[" && char === "]") {
        temp.pop()
      } else {
        temp.push(char)
      }
    }
  })

  console.log(temp)

  if (temp.length > 0) {
    return false
  } else {
    return true
  }
}
