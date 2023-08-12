const fs = require("fs")
let inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
inputs = inputs.map((v) => v.split(" ").map(Number))

function solution() {
  let res = -1

  const rightChild = Array(n + 1).fill(0)
  for (const [node, a, b] of inputs) {
    res += 1
    if (a > 0) res += 1
    if (b > 0) {
      res += 1
      rightChild[node] = b
    }
  }

  let u = 1
  while (rightChild[u] > 0) {
    u = rightChild[u]
    res -= 1
  }
  console.log(res)
}
solution()
// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// function solution() {
//     const N = Number(input[0]);
//     let res = -1;
//     let rightChild = Array(N+1).fill(0);
//     for (let i=1; i<=N; i++) {
//         const [a, b, c] = input[i].split(' ').map(Number);
//         res += 1;
//         if (b > 0) res += 1;
//         if (c > 0) {
//             res += 1;
//             rightChild[a] = c;
//         }
//     }
//     let u = 1;
//     while (rightChild[u] > 0) {
//         u = rightChild[u];
//         res -= 1;
//     }
//     console.log(res);
// }

// solution();
// const graph = Array(n + 1)
//   .fill(0)
//   .map(() => ({}))

// for (const [node, a, b] of inputs) {
//   if (a !== -1) {
//     graph[node].left = a
//   }

//   if (b !== -1) {
//     graph[node].right = b
//   }
// }

// const visited = Array(n + 1).fill(false)
// let count = 0

// function inOrder(root) {
//   // console.log(root, visited)
//   if (visited.reduce((a, c) => a + c, 0) == n) {
//     console.log(count)
//     process.exit(0)
//   }

//   const connections = graph[root]

//   if (!connections.left && !connections.right) {
//     visited[root] = true

//     if (visited.reduce((a, c) => a + c, 0) == n) {
//       console.log(count)
//       process.exit(0)
//     }
//     return
//   }

//   if (connections.left) {
//     count++
//     inOrder(connections.left)
//     count++
//   }

//   visited[root] = true

//   if (connections.right) {
//     count++
//     inOrder(connections.right)
//     count++
//   }
// }

// inOrder(1)

// // 전위 순회 (Preorder Traversal)
// // 중위 순회 (Inorder Traversal)
// // 후위 순회 (Postorder Traversal)
