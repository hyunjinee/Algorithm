function solution(n, start, end, roads, traps) {
  let ans = Infinity
  const graph = makeGraph()

  for (let i = 0; i < roads.length; i++) {
    const [from, to, cost] = roads[i]
    graph[from][to] = cost
  }

  let q = [[start, 0, graph]]
  // let counter = 0
  while (q.length) {
    const temp = []
    // console.log(q, "/")
    for (const [curr, cost, graph] of q) {
      if (cost >= ans) {
        continue
      }

      if (curr === end) {
        ans = Math.min(ans, cost)
        continue
      }

      // const nextNodes = graph[curr].filter((x) => x !== 0)

      // for (const nextNode of nextNodes) {
      //   const newGraph = JSON.parse(JSON.stringify(graph))
      //   const newCost = cost + nextNode
      //   temp.push([nextNode, newCost, newGraph])
      //   if (traps.includes(nextNode)) {
      //     // 만약에 i가 함정이라면? i랑 연결된 것들을 바꿈
      //     changeRoad(newGraph, nextNode)
      //   }
      // }

      for (let i = 1; i <= n; i++) {
        if (curr === i) continue
        if (graph[curr][i] !== 0) {
          const newGraph = JSON.parse(JSON.stringify(graph))

          temp.push([i, cost + graph[curr][i], newGraph])
          if (traps.includes(i)) {
            // 만약에 i가 함정이라면? i랑 연결된 것들을 바꿈
            changeRoad(newGraph, i)
          }
        }
      }
    }

    q = temp
  }

  function changeRoad(graph, number) {
    // number와 연관된 모든 것의 방향을 바꾼다.
    for (let i = 1; i <= n; i++) {
      for (let j = i + 1; j <= n; j++) {
        if (i !== number && j !== number) {
          continue
        }

        if (graph[i][j]) {
          graph[j][i] = graph[i][j]
          graph[i][j] = 0
        } else if (graph[j][i]) {
          graph[i][j] = graph[j][i]
          graph[j][i] = 0
        }
      }
    }
  }

  console.log(ans)
  return ans

  function makeGraph() {
    return Array(n + 1)
      .fill()
      .map(() => Array(n + 1).fill(0))
  }
}

console.log(
  solution(
    4,
    1,
    4,
    [
      [1, 2, 1],
      [3, 2, 1],
      [2, 4, 1],
    ],
    [2, 3]
  )
)
