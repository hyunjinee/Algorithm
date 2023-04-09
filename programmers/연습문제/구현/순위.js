function solution(n, results) {
  let ans = 0
  const winGraph = []
  const loseGraph = []

  results.forEach((result) => {
    if (winGraph[result[0]]) {
      winGraph[result[0]].push(result[1])
    } else {
      winGraph[result[0]] = [result[1]]
    }

    if (loseGraph[result[1]]) {
      loseGraph[result[1]].push(result[0])
    } else {
      loseGraph[result[1]] = [result[0]]
    }
  })

  for (let i = 1; i <= n; i++) {
    if (bfs(winGraph, i) + bfs(loseGraph, i) === n - 1) ans++
  }

  return ans

  function bfs(graph, start) {
    const q = [start]
    const visited = []
    let result = 0

    while (q.length > 0) {
      const node = q.shift()
      for (const nextNode of graph[node] || []) {
        if (visited[nextNode] !== true) {
          visited[nextNode] = true
          q.push(nextNode)
          result++
        }
      }
    }
    return result
  }
}

// function solution(n, results) {
//   let answer = 0

//   const list = Array(n)
//     .fill()
//     .map((v) => ({ rank: {}, win: [], loose: [] }))

//   results.forEach(([win, loose]) => {
//     list[win - 1].win.push(loose - 1)
//     list[loose - 1].loose.push(win - 1)
//   })
//   console.log(list)

//   function findRank(node, type, visited) {
//     visited[node] = true
//     if (list[node].rank[type]) {
//       return list[node].rank[type]
//     }

//     for (let i = 0; i < n; i++) {
//       const winner = findRank(i, "loose", )
//     }
//   }
// }

console.log(
  solution(5, [
    [4, 3],
    [4, 2],
    [3, 2],
    [1, 2],
    [2, 5],
  ])
) // 2
