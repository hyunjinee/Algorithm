const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [n, m, t] = input[0].split(" ").map(Number)
const arr = input.slice(1).map((data) => data.split(" ").map(Number))
const visited = Array.from(Array(n), () => Array(m).fill(false))

function bfs() {
  const queue = [[0, 0, 0]]
  let min = Infinity
  while (queue.length !== 0) {
    const [i, j, time] = queue.shift()
    if (time > t) continue

    if (i === n - 1 && j === m - 1 && time <= t) min = Math.min(min, time)
    if (arr[i][j] === 2 && time + (n - i - 1) + (m - j - 1) <= t) {
      min = Math.min(min, time + (n - i - 1) + (m - j - 1))
      continue
    }

    ;[
      [i - 1, j],
      [i, j - 1],
      [i + 1, j],
      [i, j + 1],
    ].forEach(([x, y]) => {
      if (x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1 && arr[x][y] !== 1 && !visited[x][y]) {
        visited[x][y] = true
        queue.push([x, y, time + 1])
      }
    })
  }

  console.log(min === Infinity ? "Fail" : min)
}

bfs()

// const fs = require("fs")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

// const [N, M, T] = input[0].split(" ").map(Number)
// const board = input.slice(1).map((data) => data.split(" ").map(Number))
// const visited = Array.from(Array(N), () => Array(M).fill(false))

// const bfs = () => {
//   const q = [[0, 0, 0]]
//   let min = Infinity

//   while (q.length) {
//     const [i, j, time] = q.shift()

//     if (time > T) {
//       continue
//     }

//     if (i === N - 1 && j === M - 1 && time <= T) {
//       min = Math.min(min, time)
//     }

//     if (board[i][j] === 2 && time + (N - i - 1) + (M - j - 1) <= T) {
//       min = Math.min(min, time + (N - i - 1) + (M - j - 1))
//       continue
//     }

//     ;[
//       [i - 1, j],
//       [i, j - 1],
//       [i + 1, j],
//       [i, j + 1],
//     ].forEach(([x, y]) => {
//       if (x >= 0 && x <= N - 1 && y >= 0 && y <= M - 1 && board[x][y] !== 1) {
//         visited[x][y] = true
//         q.push([x, y, time + 1])
//       }
//     })
//   }
//   console.log(min === Infinity ? "Fail" : min)
// }

// bfs()
// //   let min = Infinity
// //   while (queue.length !== 0) {
// //     const [i, j, time] = queue.shift()
// //     if (time > t) continue

// //     if (i === n - 1 && j === m - 1 && time <= t) min = Math.min(min, time)
// //     if (arr[i][j] === 2 && time + (n - i - 1) + (m - j - 1) <= t) {
// //       min = Math.min(min, time + (n - i - 1) + (m - j - 1))
// //       continue
// //     }

// //     ;[
// //       [i - 1, j],
// //       [i, j - 1],
// //       [i + 1, j],
// //       [i, j + 1],
// //     ].forEach(([x, y]) => {
// //       if (x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1 && arr[x][y] !== 1 && !visited[x][y]) {
// //         visited[x][y] = true
// //         queue.push([x, y, time + 1])
// //       }
// //     })
// //   }

// //   console.log(min === Infinity ? "Fail" : min)
// // }

// // bfs()
