function solution(maps) {
  const ans = []

  const [n, m] = [maps.length, maps[0].length]
  const visited = Array.from(Array(n), () => Array(m).fill(false))

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maps[i][j] === "X") continue

      if (!visited[i][j]) {
        ans.push(bfs(i, j, maps, visited))
      }
    }
  }
  return ans.length ? ans.sort() : [-1]
}

function bfs(startX, startY, maps, visited) {
  const queue = [[startX, startY]]
  let days = 0

  const directions = [
    [-1, 0], // up
    [1, 0], // down
    [0, -1], // left
    [0, 1], // right
  ]

  while (queue.length) {
    let [x, y] = queue.shift()
    visited[x][y] = true
    days += +maps[x][y]

    for (const [dx, dy] of directions) {
      const nx = x + dx
      const ny = y + dy

      if (
        nx < 0 ||
        ny < 0 ||
        maps.length <= nx ||
        maps[0].length <= ny ||
        visited[nx][ny] ||
        maps[nx][ny] == "X"
      ) {
        continue
      }

      queue.push([nx, ny])
      visited[nx][ny] = true
    }
  }
  return days
}

solution(["X591X", "X1X5X", "X231X", "1XXX1"])
