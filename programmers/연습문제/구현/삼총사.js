function solution(number) {
  let result = 0

  backTracking([], 0)
  function backTracking(current, start) {
    if (current.length === 3) {
      result += current.reduce((a, x) => a + x) === 0 ? 1 : 0
    }

    for (let i = start; i < number.length; i++) {
      backTracking([...current, number[i]], i + 1)
    }
  }

  return result
}
