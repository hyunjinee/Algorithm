let inputs = require("fs").readFileSync("/dev/stdin").toString().trim()
inputs = inputs.split("\n")
const [m, n] = inputs[0].split(" ").map(Number)
const box = inputs.slice(1).map((input) => input.split(" ").map(Number))
let retval = 0
let days = 0
let tomatos = []
box.map((b, y) => b.map((t, x) => t === 1 && tomatos.push([y, x])))

function checkTomato(y, x, arr) {
  if (x >= 0 && x < m && y >= 0 && y < n && !box[y][x]) {
    box[y][x] = 1
    arr.push([y, x])
  }
}

while (tomatos.length) {
  const nextTomato = []
  tomatos.map((tomato) => {
    const [y, x] = tomato
    checkTomato(y - 1, x, nextTomato)
    checkTomato(y + 1, x, nextTomato)
    checkTomato(y, x - 1, nextTomato)
    checkTomato(y, x + 1, nextTomato)
  })
  tomatos = nextTomato
  ++days
}

box.map((b) => {
  if (b.includes(0)) {
    retval = -1
    return
  }
})
console.log(retval || days - 1)

// const input = require("fs")
//   .readFileSync("./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
// const [n, m] = input[0].split(" ").map(Number)
// const dx = [0, 0, 1, -1],
//   dy = [1, -1, 0, 0]
// const q = []
// const tomato = input.slice(1).map((x) => x.split(" ").map(Number))
// let count = 0
// for (let i = 0; i < m; i++) {
//   for (let j = 0; j < n; j++) {
//     if (tomato[i][j] == 1) {
//       q.push([i, j])
//     }
//     if (tomato[i][j] == -1) {
//       count++
//     }
//   }
// }

// function bfs() {
//   while (q.length) {
//     let [cx, cy] = q.shift()
//     for (let i = 0; i < 4; i++) {
//       let nx = cx + dx[i],
//         ny = cy + dy[i]
//       if (0 <= nx && nx < m && 0 <= ny && ny < n) {
//         if (tomato[nx][ny] === 0) {
//           tomato[nx][ny] = tomato[cx][cy] + 1
//           q.push([nx, ny])
//         }
//       }
//     }
//   }
//   if (count != m * n) {
//     console.log(-1)
//     process.exit()
//     return
//   }
// }

// bfs()

// let ans = 0
// for (let i = 0; i < m; i++) {
//   for (let j = 0; j < n; j++) {
//     if (tomato[i][j] == 0) {
//       console.log(-1)
//       process.exit()
//     }
//     ans = Math.max(ans, tomato[i][j] - 1)
//   }
// }
// console.log(ans)
// tomato.flat().forEach((x) => {
//   if (x == 0) {
//     console.log(-1)
//     process.exit()
//   }
// })
// console.log(Math.max(...tomato.map((x) => Math.max(...x))) - 1)
