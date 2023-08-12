const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim()
let [NQ, ...A] = input.split("\n").map((e) => e.split(" ").map(Number))
const direction = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
]
const [N, Q] = NQ
const L = A.pop()

console.log(solution([N, Q], A, L))

function solution([N, Q], A, L) {
  const getLen = (n) => Math.pow(2, n)
  const check = (y, x) => 0 <= y && y < len && 0 <= x && x < len
  const len = getLen(N)

  const spin = (l) => {
    const temp = Array.from({ length: len }, () => Array(len).fill(0))
    for (let y = 0; y < len; y += l) {
      for (let x = 0; x < len; x += l) {
        for (let i = 0; i < l; i++) {
          for (let j = 0; j < l; j++) {
            temp[y + i][x + j] = A[y + l - j - 1][x + i]
          }
        }
      }
    }
    A = temp
  }

  const melt = () => {
    const newA = JSON.parse(JSON.stringify(A))
    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len; j++) {
        let cnt = 0
        for (const [dy, dx] of direction) {
          const ny = dy + i
          const nx = dx + j
          if (!check(ny, nx)) continue
          if (A[ny][nx] > 0) {
            cnt++
          }
        }
        if (cnt < 3 && newA[i][j] > 0) {
          newA[i][j]--
        }
      }
    }
    A = newA
  }

  for (let i = 0; i < Q; i++) {
    if (L[i] !== 0) spin(getLen(L[i]))
    melt()
  }

  let sum = 0
  let max = 0
  const visited = Array.from({ length: len }, () => Array(len).fill(false))

  const bfs = (pos) => {
    let queue = [[pos[0], pos[1]]]
    let cnt = 0
    visited[pos[0]][pos[1]] = true
    while (queue.length > 0) {
      const size = queue.length
      const nextQueue = []
      for (let i = 0; i < size; i++) {
        const [y, x] = queue[i]
        cnt++
        sum += A[y][x]
        for (const [dy, dx] of direction) {
          const ny = dy + y
          const nx = dx + x
          if (!check(ny, nx)) continue
          if (visited[ny][nx]) continue
          visited[ny][nx] = true
          if (A[ny][nx] === 0) continue
          nextQueue.push([ny, nx])
        }
      }
      queue = nextQueue
    }
    max = Math.max(max, cnt)
  }

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (visited[i][j]) continue
      if (A[i][j] === 0) continue
      bfs([i, j])
    }
  }

  return [sum, max].join("\n")
}
// console.log(solution([N, Q], A, L))

// function solution([N, Q], A, L) {
//   const getLen = (n) => Math.pow(2, n)
//   const len = getLen(N)

//   const check = (y, x) => 0 <= y && y < len && 0 <= x && x < len

//   const spin = (l) => {
//     const temp = Array.from({ length: len }, () => Array(len).fill(0))
//     for (let y = 0; y < len; y += l) {
//       for (let x = 0; x < len; x += l) {
//         for (let i = 0; i < l; i++) {
//           for (let j = 0; j < l; j++) {
//             temp[y + i][x + j] = A[y + l - j - 1][x + i]
//           }
//         }
//       }
//     }
//     A = temp
//   }

//   const melt = () => {
//     const newA = JSON.parse(JSON.stringify(A))
//     for (let i = 0; i < len; i++) {
//       for (let j = 0; j < len; j++) {
//         let cnt = 0
//         for (const [dy, dx] of direction) {
//           const ny = dy + i
//           const nx = dx + j
//           if (!check(ny, nx)) continue
//           if (A[ny][nx] > 0) {
//             cnt++
//           }
//         }
//         if (cnt < 3 && newA[i][j] > 0) {
//           newA[i][j]--
//         }
//       }
//     }
//     A = newA
//   }

//   for (let i = 0; i < Q; i++) {
//     if (L[i] !== 0) spin(getLen(L[i]))
//     melt()
//   }

//   let sum = 0
//   let max = 0
//   const visited = Array.from({ length: len }, () => Array(len).fill(false))

//   const bfs = (pos, visited) => {
//     let queue = [[pos[0], pos[1]]]
//     let cnt = 0
//     visited[pos[0]][pos[1]] = true
//     while (queue.length > 0) {
//       const size = queue.length
//       const nextQueue = []
//       for (let i = 0; i < size; i++) {
//         const [y, x] = queue[i]
//         cnt++
//         sum += A[y][x]
//         for (const [dy, dx] of direction) {
//           const ny = dy + y
//           const nx = dx + x
//           if (!check(ny, nx)) continue
//           if (visited[ny][nx]) continue
//           visited[ny][nx] = true
//           if (A[ny][nx] === 0) continue
//           nextQueue.push([ny, nx])
//         }
//       }
//       queue = nextQueue
//     }
//     max = Math.max(max, cnt)
//   }

//   for (let i = 0; i < len; i++) {
//     for (let j = 0; j < len; j++) {
//       if (visited[i][j]) continue
//       if (A[i][j] === 0) continue
//       bfs([i, j], visited)
//     }
//   }

//   return [sum, max].join("\n")
// }
