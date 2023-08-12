const fs = require("fs")
let inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, s, d] = inputs.shift().split(" ").map(Number)
inputs = inputs.map((v) => v.split(" ").map(Number))
const graph = Array(n + 1)
  .fill()
  .map(() => [])
for (const [x, y] of inputs) {
  graph[x].push(y)
  graph[y].push(x)
}

let ans = 0

function dfs(cur, prev) {
  let max = 0

  for (const next of graph[cur]) {
    if (next !== prev) {
      max = Math.max(max, dfs(next, cur))
    }
  }

  if (max >= d) {
    ans += 1
  }

  return max + 1
}

dfs(s, 0)

console.log(ans > 0 ? (ans - 1) * 2 : 0)
// 리프 노드까지 쭉 내려갔다가
// 올라오면서 자신에게 자식 노드가 몇 개 있는지 카운트해서 저장해주어야한다.
// 그렇게 카운트가 구해지면
// 힘보다 크거나 같은 자식 노드를 갖는 노드만 방문해주면 된다.
// 힘이 3일 때, 자식 노드를 3개 가진 노드를 방문했고 하자.
// 그러면 해당 노드만 방문하고도 그 노드의 자식 노드까지 모두 전단지를 돌릴 수 있다.
// function dfs(cur, prev) {
//   console.log(cur, "cur")
//   let max = 0

//   for (const next of graph[cur]) {
//     if (next !== prev) {
//       max = Math.max(max, dfs(next, cur))
//     }
//   }

//   if (max >= d) {
//     ans += 1
//   }

//   return max + 1
// }

// dfs(s, 0)

// console.log(ans > 0 ? (ans - 1) * 2 : 0)

// import sys
// input = sys.stdin.readline
// sys.setrecursionlimit(10**5)

// def dfs(cur_node, pre_node):
//     global ans
//     max_d = 0
//     for next_node in graph[cur_node]:
//         if next_node != pre_node:
//             max_d = max(max_d,dfs(next_node, cur_node))
//     if max_d >= D:
//         ans += 1
//     return max_d + 1

// N, S, D = map(int, input().split())
// graph = {i: [] for i in range(1,N+1)}
// visited = [0] * (N+1)
// ans = 0
// for _ in range(N-1):
//     x, y = map(int, input().split())
//     graph[x] += [y]
//     graph[y] += [x]
// dfs(S, 0)
// print(2*(ans-1) if ans else 0)
