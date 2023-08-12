const inputs = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")

const n = Number(inputs.shift())
const [from, to] = inputs.shift().split(" ").map(Number)

function solution(inputs) {
  const connections = Number(inputs.shift())
  const tree = Array.from(Array(n + 1), () => new Array())
  const visit = Array.from(Array(n + 1), () => 0)

  inputs.map((input) => {
    const [x, y] = input.split(" ").map(Number)
    tree[x].push(y)
    tree[y].push(x)
  })

  const queue = []
  queue.push(from)
  visit[from] = 1

  while (queue.length) {
    const now = queue.shift()

    for (let next of tree[now]) {
      if (visit[next]) continue
      visit[next] = visit[now] + 1
      queue.push(next)
    }
  }

  console.log(visit[to] ? visit[to] - 1 : -1)
}

solution(inputs)

// let visited

// function solution(board, node, target, depth) {
//   let ret = -1
//   visited[node] = 1

//   if (node === target) {
//     return depth
//   }

//   for (let i = 1; i < board[node].length; i++) {
//     if (board[node][i] === 1 && visited[i] === 0) {
//       ret = solution(board, i, target, depth + 1)
//       if (ret !== -1) break
//     }
//   }

//   return ret
// }

// function init() {
//   const fs = require("fs")
//   const input = fs.readFileSync("/dev/stdin").toString().split("\n")

//   let N = Number(input[0])
//   let [start, target] = input[1].split(" ")
//   start = Number(start)
//   target = Number(target)
//   let cnt = Number(input[2])
//   let board = new Array(N + 1)
//   visited = new Array(N + 1).fill(0)

//   for (let i = 0; i < N + 1; i++) {
//     board[i] = new Array(N + 1).fill(0)
//   }

//   for (let i = 0; i < cnt; i++) {
//     let [from, to] = input[3 + i].split(" ")
//     board[from][to] = 1
//     board[to][from] = 1
//   }

//   let ans
//   ans = solution(board, start, target, 0)
//   console.log(ans)
// }

// init()

// // const fs = require("fs")

// // let [n, nums, m, ...arr] = fs
// //   .readFileSync("./dev/stdin")
// //   .toString()
// //   .trim()
// //   .split("\n")
// // let [s, e] = nums.split(" ").map((e) => +e)
// // const visited = Array(+n).fill(0)
// // arr = arr.map((e) => e.split(" ").map((e) => +e))

// // const graph = Array.from(Array(+n), () => [])
// // arr.map((e) => {
// //   graph[e[0] - 1].push(e[1] - 1)
// //   graph[e[1] - 1].push(e[0] - 1)
// // })
// // console.log(graph)

// // function bfs() {
// //   q = []
// //   let depth = 0
// //   q.push([s, depth])
// //   while (q.length) {
// //     let [node, depth] = q.shift()
// //     console.log(node, depth)
// //     console.log(node, e, "?")
// //     if (node == e) {
// //       console.log(depth, "?whw")
// //       return depth
// //     }
// //     if (!visited[node]) {
// //       visited[node] = 1
// //       graph[node].forEach((e) => {
// //         if (!visited[e]) q.push([e, depth + 1])
// //       })
// //     }
// //   }
// // }

// // console.log(bfs())

// // // let P = +people;
// // // let answer = -1;
// // // let visited = Array(P).fill(0);
// // // let [F, T] = nums.split(' ').map(el => el-1);
// // // let points = Array.from(Array(P), () => []);
// // // arr.forEach(el => {
// // //     let [from, to] = el.split(' ').map(el2 => +el2);
// // //     points[from-1].push(to-1);
// // //     points[to-1].push(from-1);
// // // });

// // // const bfs = () => {
// // //     let q = [];
// // //     q.push([F, 0]);
// // //     while (q.length) {
// // //         let [start, dist] = q.shift();
// // //         if (start === T) {
// // //             answer = dist;
// // //             break;
// // //         }
// // //         if (!visited[start]) {
// // //             visited[start] = dist;
// // //             for (const el of points[start]) {
// // //                 if (!visited[el]) {
// // //                     q.push([el, dist+1]);
// // //                 }
// // //             }
// // //         }
// // //     }
// // // }

// // // bfs();

// // // console.log(answer);
