const integerReplacement = function (n) {
  let result = Infinity

  backTracking(n, 0)

  function backTracking(x, cnt) {
    if (x === 1) {
      result = Math.min(result, cnt)
      return
    }

    if (x % 2 === 0) {
      backTracking(x / 2, cnt + 1)
    } else {
      backTracking(x + 1, cnt + 1)
      backTracking(x - 1, cnt + 1)
    }
  }

  return result
}
