function solution(n, wires) {
  const links = {}
  wires.forEach((w) => {
    const [a, b] = w
    if (!links[a]) links[a] = []
    if (!links[b]) links[b] = []
    links[a].push(b)
    links[b].push(a)
  })

  let answer = Number.MAX_SAFE_INTEGER

  wires.forEach((wire, i) => {
    const [a, b] = wire
    const diff = Math.abs(searchTree(a, b) - searchTree(b, a))
    answer = answer > diff ? diff : answer
  })

  return answer

  function searchTree(root, exception) {
    let count = 0
    const q = [root]
    const visited = []

    visited[root] = true

    while (q.length) {
      const cur = q.shift()
      links[cur].forEach((next) => {
        if (next !== exception && !visited[next]) {
          visited[next] = true
          q.push(next)
        }
      })

      count++
    }

    return count
  }
}

// function solution(n, wires) {
//   let result = Number.MAX_SAFE_INTEGER
//   for (let i = 0; i < wires.length; i++) {
//     const curExceptArr = wires.slice(0, i).concat(wires.slice(i + 1))
//     const curConnect = {}

//     curExceptArr.forEach((wire) => {
//       const [to, from] = wire
//       if (!curConnect[to]) curConnect[to] = []
//       if (!curConnect[from]) curConnect[from] = []

//       curConnect[to].push(from)
//       curConnect[from].push(to)
//     })

//     const [root, tree] = Object.entries(curConnect)[0]

//     let count = findTree(curConnect, root)
//     const other = n - count
//     count = Math.abs(count - other)
//     if (result > count) {
//       result = count
//     }
//   }

//   return count
// }

// function findTree(obj, root) {
//   let count = 1
//   const queue = [root]

//   const visited = []
//   visited[root] = true

//   while (queue.length) {
//     const cur = queue.pop()
//     obj[cur].forEach((now) => {
//       if (!visited[now]) {
//         queue.push(now)
//         visited[now] = true
//         count++
//       }
//     })
//   }

//   return count
// }
// // function solution(n, wires) {
// //   let answer = Number.MAX_SAFE_INTEGER
// //   const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0))

// //   for (const [a, b] of wires) {
// //     graph[a][b] = 1
// //     graph[b][a] = 1
// //   }

// //   for (const [a, b] of wires) {
// //     graph[a][b] = 0
// //     graph[b][a] = 0

// //     const visited = Array.from({ length: n + 1 }, () => 0)
// //     visited[1] = 1
// //     const count = bfs(1, visited)

// //     graph[a][b] = 1
// //     graph[b][a] = 1

// //     // break
// //     answer = Math.min(answer, Math.abs(n - count - count))
// //   }

// //   console.log(answer)

// //   return answer

// //   function bfs(x, visited) {
// //     let count = 1
// //     const queue = [x]
// //     while (queue.length) {
// //       const node = queue.shift()
// //       for (let i = 1; i <= n; i++) {
// //         // console.log(graph[node][i])
// //         if (visited[i] === 0 && graph[node][i] === 1) {
// //           queue.push(graph[node][i])
// //           visited[i] = 1
// //           count++
// //         }
// //       }
// //     }
// //     console.log(count)
// //     return count
// //   }
// // }

// // solution(9, [
// //   [1, 3],
// //   [2, 3],
// //   [3, 4],
// //   [4, 5],
// //   [4, 6],
// //   [4, 7],
// //   [7, 8],
// //   [7, 9],
// // ])

// // // 3
