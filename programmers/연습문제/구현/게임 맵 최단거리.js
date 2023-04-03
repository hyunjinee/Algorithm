function solution(maps) {
  const visited = Array(maps.length)
    .fill(0)
    .map((x) => Array(maps[0].length).fill(false))

  const q = [[0, 0, 1]],
    dy = [1, -1, 0, 0],
    dx = [0, 0, 1, -1]
  visited[0][0] = true

  while (q.length) {
    const [cy, cx, cnt] = q.shift()

    if (cy === maps.length - 1 && cx === maps[0].length - 1) {
      return cnt
    }

    for (let i = 0; i < 4; i++) {
      const ny = cy + dy[i]
      const nx = cx + dx[i]

      if (
        0 <= ny &&
        ny < maps.length &&
        nx >= 0 &&
        nx < maps[0].length &&
        !visited[ny][nx] &&
        maps[ny][nx] === 1
      ) {
        visited[ny][nx] = true
        q.push([ny, nx, cnt + 1])
      }
    }
  }

  return -1
}
