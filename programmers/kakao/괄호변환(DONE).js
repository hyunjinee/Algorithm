function solution(p) {
  if (checkIsRightString(p)) {
    return p
  }
  return algo(p)
}

function algo(s) {
  // 1. 입력이 빈 문자열인 경우 빈 문자열을 반환한다.
  if (s === "") return s

  // 2. 문자열 w를 두 균형잡힌 괄호 문자열 u와 v로 분리한다.
  return divide(s)

  function divide(s) {
    // s는 일단 이미 균형잡힌 문자열임 근데 이걸 나눌꺼임
    // u, v인데 u는 균형잡힌 문자열로 더이상 분리될 수가 없음, v는 빈문자열이 될 수 있음

    for (let i = 0; i <= s.length; i++) {
      const u = s.slice(0, i)
      const v = s.slice(i)

      // 2. 문자열 w를 두 균형잡힌 괄호 문자열 u와 v로 분리한다.
      if (checkIsBalancedStringWhichCanNotDivide(u) && (checkIsBalancedString(v) || v === "")) {
        // 단 u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야하며 v는 빈 문자열이 될 수도 있다.
        // 3. u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행한다.
        if (checkIsRightString(u)) {
          // 3.1 수행 결과를 u에 이어 붙인 후 반환한다.
          return u + algo(v)
        } else {
          // 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행한다.
          return (
            "" +
            "(" +
            algo(v) +
            ")" +
            Array.from(u.slice(1, -1))
              .map((x) => {
                if (x === "(") return ")"
                else if (x === ")") return "("
              })
              .join("")
          )
        }
      }
    }
  }
}

function checkIsBalancedStringWhichCanNotDivide(s) {
  if (!checkIsBalancedString(s)) {
    return false
  }

  let flag = true

  for (let i = 0; i < s.length; i++) {
    const left = s.slice(0, i)
    const right = s.slice(i)

    if (checkIsBalancedString(left) && checkIsBalancedString(right)) {
      flag = false
      break
    }
  }

  return flag
}

function checkIsBalancedString(s) {
  if (s === "") return false // 빈 문자열은 균형잡힌 문자열이 아니다.

  let left = 0 // 왼쪽 괄호의 개수
  let right = 0 // 오른쪽 괄호의 개수

  for (const char of s) {
    if (char === "(") left++
    else if (char === ")") right++
    else {
      return false // 다른 문자가 포함되어 있다면 균형잡힌 문자열이 아니다.
    }
  }

  return left === right
}

function checkIsRightString(s) {
  if (!checkIsBalancedString(s)) {
    return false
  }

  const stack = []

  for (const char of s) {
    if (stack.length === 0) {
      stack.push(char)
      continue
    }

    if (stack.at(-1) === "(" && char === ")") {
      stack.pop()
    } else {
      stack.push(char)
    }
  }

  return stack.length === 0 ? true : false
}
