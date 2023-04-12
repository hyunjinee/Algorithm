function solution(n, info) {
  let result = Array(11).fill(0)
  let max = 0

  function shot(peachScore, ryanScore, count, idx, scoreBoard) {
    if (n < count) {
      return
    }

    if (idx > 10) {
      let scoreDiff = ryanScore - peachScore

      if (max < scoreDiff) {
        scoreBoard[10] = n - count
        max = scoreDiff
        result = scoreBoard
      }

      return
    }

    if (n > count) {
      let candidate = [...scoreBoard]
      candidate[10 - idx] = info[10 - idx] + 1
      shot(
        peachScore,
        ryanScore + idx,
        count + info[10 - idx] + 1,
        idx + 1,
        candidate
      )
    }

    if (info[10 - idx] > 0) {
      shot(peachScore + idx, ryanScore, count, idx + 1, scoreBoard)
    } else {
      shot(peachScore, ryanScore, count, idx + 1, scoreBoard)
    }
  }

  shot(0, 0, 0, 0, result)

  if (max === 0) return [-1]
  return result
}
