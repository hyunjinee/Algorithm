function solution(picks, minerals) {
  let answer = 0
  const picksSum = picks.reduce((a, x) => a + x)
  const slicedMinerals = minerals.slice(0, picksSum * 5)
  const countedMinerals = slicedMinerals.reduce((acc, cur, idx) => {
    const index = Math.floor(idx / 5)
    if (!acc[index]) acc[index] = [0, 0, 0]
    if (cur === "diamond") acc[index][0]++
    else if (cur === "iron") acc[index][1]++
    else if (cur === "stone") acc[index][2]++
    return acc
  }, [])

  const sortedMinerals = countedMinerals.sort(
    (a, b) => b[0] - a[0] || b[1] - a[1] || b[2] - a[2]
  )

  for (const [dia, iron, stone] of sortedMinerals) {
    if (picks[0]) {
      answer += dia + iron + stone
      picks[0]--
    } else if (picks[1]) {
      answer += dia * 5 + iron + stone
      picks[1]--
    } else if (picks[2]) {
      answer += dia * 25 + iron * 5 + stone
      picks[2]--
    }
  }
  return answer
}
