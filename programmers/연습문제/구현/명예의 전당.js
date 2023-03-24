function solution(k, score) {
  const legend = []
  const result = []

  for (let i = 0; i < score.length; i++) {
    if (legend.length < k) {
      legend.push(score[i])
      result.push(Math.min(...legend))
      continue
    }
    const minValue = Math.min(...legend)

    if (score[i] <= minValue) {
      result.push(minValue)
      continue
    }

    if (score[i] > minValue) {
      legend.sort((a, b) => a - b)
      legend.shift()
      legend.push(score[i])
      legend.sort((a, b) => a - b)

      result.push(legend[0])
    }
  }

  return result
}
