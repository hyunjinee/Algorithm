const dir = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
]
function solution(maps) {
  const [n, m] = [maps.length, maps[0].length]

  let sx, sy, lx, ly, ex, ey
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (maps[i][j] == "S") {
        sy = i
        sx = j
      }
      if (maps[i][j] == "L") {
        ly = i
        lx = j
      }
      if (maps[i][j] == "E") {
        ey = i
        ex = j
      }
    }
  }

  const one = bfs(sy, sx, ly, lx, maps)s
  const two = bfs(ly, lx, ey, ex, maps)

  if (one === 0 || two === 0) return -1
  return one + two
}

function bfs(startY, startX, endY, endX, maps) {
  const [n, m] = [maps.length, maps[0].length]
  const visited = Array.from({ length: n }, () => new Array(m).fill(false))

  const isValid = (y, x) =>
    0 <= y && y < n && 0 <= x && x < m && !visited[y][x] && maps[y][x] !== "X"

  const q = [[startY, startX, 0]]
  visited[startY][startX] = true

  while (q.length) {
    const [y, x, time] = q.shift()

    if (y === endY && x === endX) {
      return time
      break
    }

    for (let i = 0; i < 4; i += 1) {
      const [dy, dx] = dir[i]
      const [dirY, dirX] = [dy + y, dx + x]

      if (isValid(dirY, dirX)) {
        visited[dirY][dirX] = true
        q.push([dirY, dirX, time + 1])
      }
    }
  }
  return 0
}
