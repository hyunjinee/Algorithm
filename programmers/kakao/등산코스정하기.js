function solution(n, paths, gates, summits) {
  const graph = Array(n + 1)
    .fill()
    .map(() => [])

  for (const [i, j, w] of paths) {
    graph[i].push([j, w])
    graph[j].push([i, w])
  }

  console.log(graph)

  for (const gate of gates) {
    bfs(gate)
  }

  function bfs(start) {
    let result = -Infinity
    const queue = [[start, -Infinity]]
    let isSummitVisited = false

    let visited = Array(n + 1).fill(false)

    while (queue.length) {
      const [curr, weight] = queue.shift()
      visited[curr] = true

      if (isSummitVisited && curr === start) {
        result = Math.max(result, weight)
        continue
      }

      if (!isSummitVisited && gates.includes(curr) && weight !== -Infinity) {
        continue
      }

      for (const [next, w] of graph[curr]) {
        if (summits.includes(next)) {
          isSummitVisited = true
          visited = Array(n + 1).fill(false)
        }

        queue.push([next, Math.max(weight, w)])
      }
    }

    console.log(result)
    return result
  }
}

solution(
  6,
  [
    [1, 2, 3],
    [2, 3, 5],
    [2, 4, 2],
    [2, 5, 4],
    [3, 4, 4],
    [4, 5, 3],
    [4, 6, 1],
    [5, 6, 1],
  ],
  [1, 3],
  [5]
)
