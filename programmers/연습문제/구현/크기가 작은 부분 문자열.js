function solution(t, p) {
  let answer = 0
  const pLen = p.length
  const tLen = t.length
  let i = 0
  while (i + pLen <= tLen) {
    const sliced = t.slice(i, i + pLen)
    const slicedToNumber = Number(sliced)
    if (slicedToNumber <= Number(p)) {
      answer += 1
    }
    i++
  }

  return answer
}
