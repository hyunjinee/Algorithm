function solution(data, col, rowBegin, rowEnd) {
  data.sort((a, b) => compare(a, b))
  const s = []
  for (let i = rowBegin - 1; i <= rowEnd - 1; i++) {
    const temp = data[i]
    let c = 0

    for (const t of temp) {
      c += t % (i + 1)
    }
    s.push(c)
  }
  return s.reduce((a, x) => a ^ x, 0)

  function compare(a, b) {
    if (a[col - 1] > b[col - 1]) return 1
    if (a[col - 1] < b[col - 1]) return -1
    if (a[0] > b[0]) return -1
    if (a[0] < b[0]) return 1
  }
}
