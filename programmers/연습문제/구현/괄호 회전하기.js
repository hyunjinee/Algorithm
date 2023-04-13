function solution(s) {
  let answer = 0
  let count = 0

  s = Array.from(s)

  while (count < s.length) {
    const temp = [...s]

    for (let i = 0; i < count; i++) {
      temp.push(temp.shift())
    }

    if (isOK(temp)) {
      answer++
    }

    count++
  }

  function isOK(arr) {
    if (arr.length % 2 !== 0) {
      return false
    }

    const temp = []

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] == "[" || arr[i] == "{" || arr[i] == "(") {
        temp.push(arr[i])
      } else if (arr[i] == "]") {
        if (temp.length === 0) return false
        if (temp.pop() !== "[") {
          return false
        }
      } else if (arr[i] == "}") {
        if (temp.length == 0) return false
        if (temp.pop() !== "{") {
          return false
        }
      } else if (arr[i] == ")") {
        if (temp.length == 0) return false
        if (temp.pop() !== "(") {
          return false
        }
      }
    }

    if (temp.length === 0) return true

    return false
  }

  return answer
}
