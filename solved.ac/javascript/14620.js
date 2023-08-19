const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = Number(inputs.shift())
const board = inputs.map((line) => line.split(" ").map(Number))
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]
const isSafe = (x, y) => x >= 0 && x < n && y >= 0 && y < n

let ans = Infinity

const coords = []
const visited = Array(coords.length).fill(false)
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    coords.push([i, j])
  }
}

function bfs(arr) {
  if (arr.length === 3) {
    let flowers = []
    let canPlant = true

    for (let i = 0; i < arr.length; i++) {
      let temp = []
      const [x, y] = arr[i]

      temp.push([x, y])

      for (let j = 0; j < 4; j++) {
        const nx = x + dx[j]
        const ny = y + dy[j]

        if (!isSafe(nx, ny) || flowers.some(([fx, fy]) => fx === nx && fy === ny)) {
          canPlant = false
          break
        }

        temp.push([nx, ny])
      }

      if (temp.length === 5) {
        flowers = [...flowers, ...temp]
      }
    }

    if (canPlant) {
      let sum = 0

      for (let i = 0; i < flowers.length; i++) {
        const [x, y] = flowers[i]
        sum += board[x][y]
      }

      ans = Math.min(ans, sum)
    }

    return
  }

  for (let i = 0; i < coords.length; i++) {
    if (visited[i]) {
      continue
    }

    arr.push(coords[i])
    visited[i] = true
    bfs(arr)
    arr.pop()
    visited[i] = false
  }
}

bfs([])

console.log(ans)
