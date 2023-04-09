function solution(s) {
  s = s.toLowerCase()

  let pCount = 0
  let yCount = 0

  Array.from(s).forEach((char) => {
    if (char === "p") pCount++
    if (char === "y") yCount++
  })

  if (pCount === 0 && yCount === 0) {
    return true
  }

  if (pCount === yCount) {
    return true
  }

  return false
}
