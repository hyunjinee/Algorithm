const findJudge = (n, trust) => {
  const people = new Map()

  for (let i = 1; i <= n; i++) {
    people.set(i, 0)
  }

  trust.forEach((t) => {
    people.delete(t[0]) // 믿는 사람은 judge가 될 수 없음
  })

  if (people.size === 0) {
    return -1
  }

  trust.forEach((t) => {
    if (people.has(t[1])) {
      people.set(t[1], people.get(t[1]) + 1)
    }
  })

  const judges = [...people]
  if (judges[0][1] != n - 1) {
    return -1
  }

  return judges[0][0]
}

findJudge(3, [
  [1, 2],
  [2, 3],
])
