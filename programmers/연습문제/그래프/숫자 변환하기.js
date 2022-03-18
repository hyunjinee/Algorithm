function solution(x, y, n) {
  let answer = 0

  const start = [[x, 0]]

  while (start.length) {
    const [current, point] = start.shift()

    if (current === y) {
      answer = point

      console.log(answer)
      return answer
    }

    if (current > y) {
      continue
    }

    start.push([current * 2, point + 1])
    start.push([current + n, point + 1])
    start.push([current * 3, point + 1])
  }
  return -1
}

solution(10, 40, 5)
