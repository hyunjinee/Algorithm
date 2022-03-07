const fs = require("fs")
let [nums, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

let [N, M] = nums.split(" ").map((el) => +el)
let answer = true
let visited = Array.from(Array(N), () => Array(M).fill(false))
let before = arr.splice(0, N).map((el) => el.split(" ").map((el2) => +el2))
let after = arr.splice(0, N).map((el) => el.split(" ").map((el2) => +el2))

let dy = [-1, 0, 1, 0]
let dx = [0, -1, 0, 1]

const bfs = (y, x, valueB, valueA) => {
  let q = []
  q.push([y, x])
  while (q.length) {
    let [nextY, nextX] = q.shift()
    visited[nextY][nextX] = true
    before[nextY][nextX] = valueA
    for (let k = 0; k < dy.length; k++) {
      let dyy = dy[k] + nextY
      let dxx = dx[k] + nextX
      if (dyy > -1 && dxx > -1 && dyy < N && dxx < M) {
        if (!visited[dyy][dxx] && before[dyy][dxx] === valueB) {
          q.push([dyy, dxx])
        }
      }
    }
  }
}

let flag = true
for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    if (before[y][x] !== after[y][x]) {
      bfs(y, x, before[y][x], after[y][x])
      flag = false
      if (!flag) break
    }
  }
  if (!flag) break
}

for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    if (before[y][x] !== after[y][x]) {
      answer = false
      if (!answer) break
    }
  }
  if (!answer) break
}

console.log(answer ? "YES" : "NO")

// const fs = require("fs")
// let [num, ...arr] = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// let [n, m] = num.split(" ").map((v) => Number(v))

// let before = arr.splice(0, n).map((e) => e.split(" ").map((e) => +e))
// let after = arr.splice(0, n).map((e) => e.split(" ").map((e) => +e))

// function solution() {
//   for (let y = 0; y < n; y++) {
//     for (let x = 0; x < m; x++) {
//       if (before[y][x] !== after[y][x]) {
//         bfs(y, x)
//         return check()
//       }
//     }
//   }
//   return "YES"
// }

// let dy = [-1, 0, 1, 0]
// let dx = [0, -1, 0, 1]

// function bfs(y, x) {
//   let q = [[y, x]]
//   let visited = Array.from(Array(n), () => Array(m).fill(false))
//   let temp = before[y][x]
//   let target = after[y][x]
//   while (q.length) {
//     let [nowY, nowX] = q.shift()
//     before[nowY][nowX] = target
//     visited[nowY][nowX] = true
//     for (let i = 0; i < 4; i++) {
//       let ny = nowY + dy[i]
//       let nx = nowX + dx[i]

//       if (
//         ny >= 0 &&
//         ny < n &&
//         nx >= 0 &&
//         nx < m &&
//         !visited[ny][nx] &&
//         before[ny][nx] == temp
//       ) {
//         q.push([ny, nx])
//         visited[ny][nx] = true
//       }
//     }
//   }
// }

// function check() {
//   for (let i = 0; i < n; i++) {
//     for (let j = 0; j < n; j++) {
//       if (before[i][j] !== after[i][j]) {
//         return "NO"
//       }
//     }
//   }
//   return "YES"
// }

// console.log(solution())
// // const bfs = (y, x, valueB, valueA) => {
// //     let q = [];
// //     q.push([y, x]);
// //     while (q.length) {
// //         let [nextY, nextX] = q.shift();
// //         visited[nextY][nextX] = true;
// //         before[nextY][nextX] = valueA;
// //         for (let k = 0 ; k < dy.length ; k++) {
// //             let dyy = dy[k] + nextY;
// //             let dxx = dx[k] + nextX;
// //             if (dyy > -1 && dxx > -1 && dyy < N && dxx < M) {
// //                 if (!visited[dyy][dxx] && before[dyy][dxx] === valueB) {
// //                     q.push([dyy, dxx]);
// //                 }
// //             }
// //         }
// //     }
// // }

// // let flag = true;
// // for (let y = 0; y < N; y++) {
// //     for (let x = 0; x < M; x++) {
// //         if (before[y][x] !== after[y][x]) {
// //             bfs(y, x, before[y][x], after[y][x]);
// //             flag = false;
// //             if (!flag) break;
// //         }
// //     }
// //     if (!flag) break;
// // }

// // for (let y = 0; y < N; y++) {
// //     for (let x = 0; x < M; x++) {
// //         if (before[y][x] !== after[y][x]) {
// //             answer = false;
// //             if (!answer) break;
// //         }
// //     }
// //     if (!answer) break;
// // }

// // console.log(answer ? "YES" : "NO");
