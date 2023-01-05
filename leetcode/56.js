var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0])
  const res = [intervals[0]]
  for (let curr of intervals) {
    const prev = res[res.length - 1]
    if (prev[1] >= curr[0]) {
      prev[1] = Math.max(curr[1], prev[1])
    } else {
      res.push(curr)
    }
  }
  return res
}
