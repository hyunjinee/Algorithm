function solution(storey) {
  let answer = Infinity
  backTracking(storey, 0)

  function backTracking(num, counter) {
    if (counter >= answer) {
      return
    }
    if (num === 0) {
      answer = counter
      return
    }
    let res = num % 10
    backTracking((num - res) / 10, counter + res)
    backTracking((num - res) / 10 + 1, counter + 10 - res)
  }

  return answer
}
