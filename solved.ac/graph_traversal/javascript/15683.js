const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [[n, m], ...board] = inputs.map((v) => v.split(" ").map(Number)),
  cctvs = [],
  dr = [-1, 1, 0, 0],
  dc = [0, 0, -1, 1],
  moves = [
    [],
    [[0], [1], [2], [3]],
    [
      [0, 1],
      [2, 3],
    ],
    [
      [0, 3],
      [3, 1],
      [1, 2],
      [2, 0],
    ],
    [
      [2, 0, 3],
      [0, 3, 1],
      [3, 1, 2],
      [1, 2, 0],
    ],
    [[0, 1, 2, 3]],
  ],
  isOutOfRange = (r, c) => r < 0 || r >= n || c < 0 || c >= m

let ans = 0

for (let r = 0; r < n; r++) {
  for (let c = 0; c < m; c++) {
    if (board[r][c] === 6) continue
    if (board[r][c] === 0) ans++
    else cctvs.push([r, c, board[r][c]])
  }
}

dfs(board, 0)

function dfs(board, currCCTV) {
  if (currCCTV >= cctvs.length) {
    let cnt = 0
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (board[r][c] === 0) cnt++
      }
    }

    ans = Math.min(ans, cnt)
    return
  }

  const [r, c, type] = cctvs[currCCTV]

  for (const dirs of moves[type]) {
    const temp = [...board.map((row) => [...row])]
    for (const dir of dirs) {
      let [nr, nc] = [r + dr[dir], c + dc[dir]]
      while (!isOutOfRange(nr, nc) && temp[nr][nc] !== 6) {
        temp[nr][nc] = -1
        nr += dr[dir]
        nc += dc[dir]
      }
    }
    dfs(temp, currCCTV + 1)
  }
}

console.log(ans)
// function dfs(board, curCCTV) {
//   if (curCCTV >= cctvs.length) {
//     let cnt = 0
//     for (let r = 0; r < n; r++) {
//       for (let c = 0; c < m; c++) {
//         if (board[r][c] === 0) cnt++
//       }
//     }

//     ans = Math.min(ans, cnt)
//     return
//   }

//   const [r, c, cctvType] = cctvs[curCCTV]
//   for (const dirs of moves[cctvType]) {
//     const tmp = [...board.map((row) => [...row])]

//     for (const dir of dirs) {
//       let [nr, nc] = [r + dr[dir], c + dc[dir]]
//       while (!isOutOfRange(nr, nc) && board[nr][nc] !== 6) {
//         tmp[nr][nc] = -1
//         nr += dr[dir]
//         nc += dc[dir]
//       }
//     }

//     dfs(tmp, curCCTV + 1)
//   }
// }

// const [n, m] = stdin[0].split(" ").map(Number)
// const office = stdin.slice(1).map((el) => el.split(" ").map(Number))
// const dr = [-1, 1, 0, 0]
// const dc = [0, 0, -1, 1]

//

// dfs(office, 0)
// console.log(ans)
