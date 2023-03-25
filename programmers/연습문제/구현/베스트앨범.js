function solution(genres, plays) {
  const answer = []
  const gMap = new Map()
  const gSet = new Set()

  genres.forEach((g, i) => {
    gSet.add(g)
    if (gMap.has(g)) {
      gMap.set(g, gMap.get(g) + plays[i])
      return
    }

    gMap.set(g, plays[i])
  })

  const gArr = Array.from(gMap)
  gArr.sort((a, b) => b[1] - a[1])
  let pointer = 0

  while (pointer !== gArr.length) {
    const genre = gArr[pointer][0]
    const play = []
    genres.forEach((g, i) => {
      if (genre === g) {
        play.push([plays[i], i])
      }
    })

    if (play.length === 0) {
      pointer++
      continue
    }

    if (play.length === 1) {
      answer.push(play[0][1])
      pointer++
      continue
    }

    play.sort((a, b) => {
      if (a[0] === b[0]) {
        return a[1] - b[1]
      }

      return b[0] - a[0]
    })

    const a = play.shift()
    answer.push(a[1])

    const b = play.shift()
    answer.push(b[1])

    pointer++
  }

  return answer
}

// 속한 노래가 많이 재생된 장르를 먼저 수록한다.
