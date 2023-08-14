const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

let ans = -Infinity
let value = 0

function main() {
  const [N, M] = inputs
    .shift()
    .split(" ")
    .map((v) => +v)
  const map = inputs.map((v) => v.split(" ").map((v) => +v))
  const visited = Array.from(Array(N), () => Array(M).fill(false))
  const dr = [-1, 0, 1, 0] // 상 우 하 좌
  const dc = [0, 1, 0, -1]

  function check(r1, c1, r2, c2) {
    const isReachable1 = r1 >= 0 && r1 < N && c1 >= 0 && c1 < M
    const isReachable2 = r2 >= 0 && r2 < N && c2 >= 0 && c2 < M
    const isNotVisited1 = isReachable1 && !visited[r1][c1]
    const isNotVisited2 = isReachable2 && !visited[r2][c2]

    return isReachable1 && isReachable2 && isNotVisited1 && isNotVisited2
  }

  let [value, ans] = [0, -Infinity]
  function dfs(r, c) {
    if (r === N) {
      ans = Math.max(value, ans)
      return
    }

    if (visited[r][c]) {
      c === M - 1 ? dfs(r + 1, 0) : dfs(r, c + 1)
    } else {
      for (let i = 0; i < 4; i++) {
        const [nr1, nc1] = [r + dr[i], c + dc[i]]
        const [nr2, nc2] = [r + dr[(i + 1) % 4], c + dc[(i + 1) % 4]]
        if (check(nr1, nc1, nr2, nc2)) {
          visited[r][c] = true
          visited[nr1][nc1] = true
          visited[nr2][nc2] = true
          value += map[r][c] * 2 + map[nr1][nc1] + map[nr2][nc2]

          c === M - 1 ? dfs(r + 1, 0) : dfs(r, c + 1)

          visited[r][c] = false
          visited[nr1][nc1] = false
          visited[nr2][nc2] = false
          value -= map[r][c] * 2 + map[nr1][nc1] + map[nr2][nc2]
        }
      }
      c === M - 1 ? dfs(r + 1, 0) : dfs(r, c + 1)
    }
  }
  dfs(0, 0)
  console.log(ans)
}

main()
