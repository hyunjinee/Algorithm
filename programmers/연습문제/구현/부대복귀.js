function solution(n, roads, sources, destination) {
  const graph = Array.from({ length: n + 1 }, () => [])

  roads.forEach(([a, b]) => {
    graph[a].push(b)
    graph[b].push(a)
  })

  const visited = Array(n + 1).fill(Infinity)

  function bfs(destination) {
    const q = [destination]
    visited[destination] = 0

    while (q.length > 0) {
      const idx = q.shift()
      for (let newIdx of graph[idx]) {
        if (visited[idx] + 1 < visited[newIdx]) {
          visited[newIdx] = visited[idx] + 1
          q.push(newIdx)
        }
      }
    }
  }

  bfs(destination)

  return sources.map((v) => {
    if (visited[v] === Infinity) return -1
    return visited[v]
  })
}
