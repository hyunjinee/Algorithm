const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n"),
  testcase = inputs.slice(1).map(Number),
  result = []

const bfs = (target, arr) => {
  const visited = Array(10000000).fill(false)
  const q = [[0, arr]]
  while (q.length) {
    let [curr, arr] = q.shift()
    if (visited[curr]) {
      continue
    }
    visited[curr] = true

    if (curr === target) {
      result.push(arr.join(" "))
      break
    }
    if (curr < 0) {
      curr = 0
    }
    q.push([curr + 60, [arr[0] + 1, arr[1], arr[2], arr[3], arr[4]]])
    q.push([curr + 10, [arr[0], arr[1] + 1, arr[2], arr[3], arr[4]]])
    q.push([curr - 10, [arr[0], arr[1], arr[2] + 1, arr[3], arr[4]]])
    q.push([curr + 1, [arr[0], arr[1], arr[2], arr[3] + 1, arr[4]]])
    q.push([curr - 1, [arr[0], arr[1], arr[2], arr[3], arr[4] + 1]])
  }
}

for (const tc of testcase) {
  bfs(tc, [0, 0, 0, 0, 0])
}
console.log(result.join("/n"))

// const backTracking = (curr, arr, target) => {
//   if (curr === target) {
//     answer.push(arr.join(" "))
//     return
//   }

//   if (curr < 0) {
//     curr = 0
//   }

//   // const temp = [...arr]
//   backTracking(
//     curr + 60,
//     arr.map((x, i) => {
//       if (i == 0) {
//         return x + 1
//       } else {
//         return
//       }
//     }),
//     target
//   )
//   backTracking(
//     curr + 10,
//     arr.map((x, i) => {
//       if (i == 1) {
//         return x + 1
//       } else {
//         return
//       }
//     }),
//     target
//   )
//   backTracking(
//     curr - 10,
//     arr.map((x, i) => {
//       if (i == 2) {
//         return x + 1
//       } else {
//         return
//       }
//     }),
//     target
//   )
//   backTracking(
//     curr + 1,
//     arr.map((x, i) => {
//       if (i == 3) {
//         return x + 1
//       } else {
//         return
//       }
//     }),
//     target
//   )
//   backTracking(
//     curr - 1,
//     arr.map((x, i) => {
//       if (i == 4) {
//         return x + 1
//       } else {
//         return
//       }
//     })
//   ),
//     target
// }

// for (const tc of testcase) {
//   // console.log(tc)
//   backTracking(0, [0, 0, 0, 0, 0], tc)
// }

// console.log(answer.join("/n"))

// const [t, ...n] = (require("fs").readFileSync("/dev/stdin") + "").trim().split("\n").map((v) => +v);
// const visited = Array(401).fill(false);
// const from = Array(401).fill(0);
// const queue = [0];
// visited[0] = true;
// const push = (v, f) => {
//   if (!visited[v] && v >= 0 && v < 401) {
//     visited[v] = true;
//     from[v] = f;
//     queue.push(v);
//   }
// };
// while (queue.length > 0) {
//   const cur = queue.shift();
//   push(cur - 1, cur);
//   push(cur + 1, cur);
//   push(cur - 10, cur);
//   push(cur + 10, cur);
//   push(cur + 60, cur);
// }
// const solve = (d) => {
//   const ans = [0, 0, 0, 0, 0];
//   if (d >= 200) {
//     ans[0] += Math.floor(d / 60) - 2;
//     d -= 60 * (Math.floor(d / 60) - 2);
//   }
//   while (d > 0) {
//     ans[[60, 10, -10, 1, -1].indexOf(d - from[d])] += 1;
//     d = from[d];
//   }
//   console.log(ans.join(" "));
// };
// n.map(solve);
