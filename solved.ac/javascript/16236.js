function solution() {
  const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")

  const n = +input[0]
  const space = []
  for (let i = 1; i <= n; i++) {
    space.push(input[i].split(" ").map((e) => +e))
  }

  let pos = null
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (space[r][c] === 9) {
        space[r][c] = 0
        pos = [r, c]
        break
      }
    }
  }

  let size = 2
  let ate = 0
  let ans = 0
  const dr = [1, -1, 0, 0]
  const dc = [0, 0, 1, -1]

  while (true) {
    let visited = new Set([`${pos[0]}${pos[1]}`])
    let fish = [] // "물고기의 r좌표", "c좌표", "거리" 순으로 저장
    let queue = [[pos[0], pos[1], 0]]

    // 잡아먹을 물고기 탐색
    while (queue.length > 0) {
      const [r, c, dist] = queue.shift()
      // 만약 현재까지 찾은 잡아먹을 수 있는 물고기 까지의 거리보다
      // 더 멀리 가면 조기 종료
      if (fish.length > 0 && fish[0][2] < dist + 1) break

      for (let i = 0; i < 4; i++) {
        const [nr, nc] = [r + dr[i], c + dc[i]]

        if (
          nr >= 0 &&
          nr < n &&
          nc >= 0 &&
          nc < n &&
          !visited.has(`${nr}${nc}`) &&
          space[nr][nc] <= size
        ) {
          visited.add(`${nr}${nc}`)
          queue.push([nr, nc, dist + 1])

          if (space[nr][nc] !== 0 && space[nr][nc] < size) {
            if (
              fish.length === 0 ||
              nr < fish[0][0] ||
              (nr === fish[0][0] && nc < fish[0][1])
            ) {
              fish[0] = [nr, nc, dist + 1]
            }
          }
        }
      }
    }

    // 더 이상 잡아먹을 물고기가 없으면 종료
    if (fish.length === 0) return ans

    // 물고기를 잡아 먹음
    const [fishR, fishC, dist] = fish[0]
    pos = [fishR, fishC]
    space[fishR][fishC] = 0
    ans += dist
    ate += 1
    if (size === ate) [size, ate] = [size + 1, 0]
  }
}

console.log(solution())

// const d = require("fs")
//   .readFileSync("./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((x) => x.split(" ").map((x) => +x))
// const n = +d.shift()
// const visited = new Array(n).fill(0).map((_) => new Array(n).fill(false))
// let size = 2,
//   cnt = 0,
//   time = 0,
//   ans = 0,
//   stack = [],
//   nextStack = []

// for (let i = 0; i < n; i++) {
//   for (let j = 0; j < n; j++) {
//     if (d[i][j] == 9) {
//       nextStack.push([i, j])
//       visited[i][j] = true
//       d[i][j] = 0
//       break
//     }
//   }
// }

// function search(i, j) {
//   if (!(0 <= i && i < n && 0 <= j && j < n)) return
//   if (visited[i][j]) return
//   visited[i][j] = true
//   if (d[i][j] <= size) nextStack.push([i, j])
// }

// while (nextStack.length) {
//   stack = nextStack.sort((a, b) => (a[0] !== b[0] ? b[0] - a[0] : b[1] - a[1]))
//   nextStack = []

//   while (stack.length) {
//     const [i, j] = stack.pop()

//     if (d[i][j] !== 0 && d[i][j] < size) {
//       d[i][j] = 0
//       nextStack = [[i, j]]
//       stack = []
//       ans = time--
//       visited.map((x) => x.fill(false))
//       visited[i][j] = true

//       cnt++
//       if (size <= cnt) {
//         cnt = 0
//         size++
//       }
//       break
//     }

//     search(i - 1, j)
//     search(i, j - 1)
//     search(i + 1, j)
//     search(i, j + 1)
//   }
//   time++
// }
// console.log(ans)

// while (nextStack.length) {
//   stack = nextStack.sort((a, b) => (a[0] !== b[0] ? b[0] - a[0] : b[1] - a[1]))
//   nextStack = []

//   while (stack.length) {
//     const [i, j] = stack.pop()

//     if (d[i][j] !== 0 && d[i][j] < size) {
//       d[i][j] = 0
//       nextStack = [[i, j]]
//       stack = []
//       ans = time--
//       visited.map((x) => x.fill(false))
//       visited[i][j] = true

//       cnt++
//       if (size <= cnt) {
//         cnt = 0
//         size++
//       }
//       break
//     }

//     search(i - 1, j)
//     search(i, j - 1)
//     search(i + 1, j)
//     search(i, j + 1)
//   }
//   time++
// }
// console.log(ans)
