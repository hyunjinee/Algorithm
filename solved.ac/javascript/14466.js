const [nkr, ...input] = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const [N, K, R] = nkr.split(" ").map(Number)
const roads = input.slice(0, R).map((line) => line.split(" ").map((v) => v - 1))
const cows = input.slice(R).map((line) => line.split(" ").map((v) => v - 1))

const DR = [0, 1, 0, -1]
const DC = [1, 0, -1, 0]

function solution(N, K, R, roads, cows) {
  const map = Array.from(Array(N), () =>
    Array(N)
      .fill()
      .map(() => Array(4).fill(0))
  )
  const visited = Array.from(Array(N), () => Array(N).fill(0))
  let count = 0

  makeRoad(map, roads)

  cows.forEach(([sr, sc], cur) => {
    visited.map((visit) => visit.fill(0))
    dfs(map, visited, sr, sc)

    for (let i = cur + 1; i < K; i++) {
      if (!visited[cows[i][0]][cows[i][1]]) count++
    }
  })

  return count
}

const makeRoad = (map, roads) => {
  roads.forEach((road) => {
    const [r, c, r2, c2] = road

    for (let dir = 0; dir < 4; dir++) {
      let nr = r + DR[dir]
      let nc = c + DC[dir]

      if (nr === r2 && nc === c2) {
        map[r][c][dir] = 1
        map[r2][c2][(dir + 2) % 4] = 1
      }
    }
  })
}

const dfs = (map, visited, r, c) => {
  visited[r][c] = 1

  for (let dir = 0; dir < 4; dir++) {
    if (map[r][c][dir]) continue

    let nr = r + DR[dir]
    let nc = c + DC[dir]

    if (!isInRange(nr, nc) || visited[nr][nc]) continue

    dfs(map, visited, nr, nc)
  }
}

const isInRange = (r, c) => {
  if (0 <= r && r < N && 0 <= c && c < N) return true
  return false
}

console.log(solution(N, K, R, roads, cows))

// const fs = require("fs")
// const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

// // 인접한 목초지 사이는 일반적으로 자유롭게 건널수 있다.
// const [n, k, r] = inputs.shift().split(" ").map(Number)
// const roads = inputs.slice(0, r).map((x) => x.split(" ").map((x) => Number(x - 1)))
// const cows = inputs.slice(r).map((x) => x.split(" ").map((x) => Number(x - 1)))

// const dy = [0, 0, -1, 1]
// const dx = [-1, 1, 0, 0]

// const map = Array.from(Array(n), () =>
//   Array(n)
//     .fill()
//     .map(() => Array(4).fill(0))
// )

// let count = 0
// const visited = Array.from(Array(n), () => Array(n).fill(0))
// const isSafe = (y, x) => y >= 0 && x >= 0 && y < n && x < n
// roads.forEach((road) => {
//   const [r, c, rr, cc] = road

//   for (let dir = 0; dir < 4; dir++) {
//     let nr = r + dy[dir]
//     let nc = c + dx[dir]

//     if (nr === rr && nc === cc) {
//       map[r][c][dir] = 1
//       map[rr][cc][(dir + 2) % 4] = 1
//     }
//   }
// })

// cows.forEach(([sr, sc], cur) => {
//   visited.map((visit) => visit.fill(0))
//   dfs(sr, sc)

//   for (let i = cur + 1; i < k; i++) {
//     if (!visited[cows[i][0]][cows[i][1]]) count++
//   }
// })

// function dfs(r, c) {
//   visited[r][c] = true

//   for (let dir = 0; dir < 4; dir++) {
//     if (map[r][c][dir] === 1) {
//       continue
//     }

//     let nr = r + dy[dir]
//     let nc = c + dx[dir]

//     if (isSafe(nr, nc) && !visited[nr][nc]) {
//       dfs(nr, nc)
//     }
//   }
// }

// console.log(count)
// // const dfs = (map, visited, r,c) = {

// //   // visited[r][c] = true

// //   // for (let dir = 0 ; dir  < 4; dir++) {

// //   // }
// // }
// // console.log(map)

// // while (cows.length) {
// //   const [y, x] = cows.shift()
// //   const visited = Array.from(Array(n), () => Array(n).fill(false))

// //   const q = [[y - 1, x - 1]]
// //   visited[y - 1][x - 1] = true

// //   while (q.length) {
// //     const [cy, cx] = q.shift()

// //     for (let i = 0; i < 4; i++) {
// //       const ny = cy + dy[i]
// //       const nx = cx + dx[i]

// //       if (isSafe(ny, nx) && !visited[ny][nx]) {
// //         visited[ny][nx] = true
// //       }

// //       // if (isSafe(ny, nx) && !visited[ny][nx]) {

// //       //   if (roads.some((road) => road[0] === cy && road[1] === cx && road[2] === ny && road[3] === nx)) {
// //       //     continue
// //       //   }

// //       //   if (roads.some((road) => road[0] === ny && road[1] === nx && road[2] === cy && road[3] === cx)) {
// //       //     continue
// //       //   }

// //       //   q.push([ny, nx])
// //       // }
// //     }
// //   }

// //   console.log(cow)
// // }
