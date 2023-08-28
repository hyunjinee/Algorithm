function solution(expression) {
  let ans = -Infinity
  const numberString = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  const order = []
  const visited = Array(3).fill(false)
  const map = {
    0: "*",
    1: "+",
    2: "-",
  }

  backTracking([])

  for (const o of order) {
    calculate(expression, o)
  }

  function calculate(expression, order) {
    // 피연산자와 연산자를 나누자
    const groupA = []
    const groupB = []

    while (true) {
      let i = 0
      while (numberString.includes(expression[i])) {
        i++
      }

      const temp = expression.slice(0, i)
      const operator = expression[i]

      if (!operator) {
        groupA.push(temp)
        break
      }

      groupA.push(+temp)
      groupB.push(operator)

      expression = expression.slice(i + 1)
    }

    const first = map[order[0]]
    const second = map[order[1]]
    const third = map[order[2]]

    let i = 0

    while (groupB.length) {
      const operator = i === 0 ? first : i === 1 ? second : third

      while (groupB.includes(operator)) {
        const index = groupB.indexOf(operator)
        const left = groupA[index]
        const right = groupA[index + 1]

        const result = eval(left + operator + right)
        groupA.splice(index, 2, result)
        groupB.splice(index, 1)
      }

      i++
    }

    ans = Math.max(ans, Math.abs(groupA[0]))
  }

  function backTracking(curr) {
    if (curr.length === 3) {
      order.push(curr)
      return
    }

    for (let i = 0; i < 3; i++) {
      if (visited[i]) continue
      visited[i] = true
      backTracking([...curr, i])
      visited[i] = false
    }
  }

  return ans
}
