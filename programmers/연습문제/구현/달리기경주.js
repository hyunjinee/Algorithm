function solution(players, callings) {
  const map = new Map()

  players.forEach((p, i) => {
    map.set(p, i)
  })

  callings.forEach((calling) => {
    const index = map.get(calling)
    const beforePlayer = players[index - 1]

    players[index - 1] = calling
    players[index] = beforePlayer

    map.set(calling, index - 1)
    map.set(beforePlayer, index)
  })

  return players
}
