function solution(brown, yellow) {
  let sum = brown + yellow
  let height = 3

  while (true) {
    if (sum % height === 0) {
      let width = sum / height
      if ((width - 2) * (height - 2) === yellow) {
        return [width, height]
      }
    }

    height++
  }
}
