function solution(n, edges) {
  const adjList = edges.reduce((G, [from, to]) => {
    G[from] = (G[from] || []).concat(to)
    G[to] = (G[to] || []).concat(from)
    return G
  }, {})
  const queue = [1]
  const visited = { 1: true }
  const dist = { 1: 0 }
  while (queue.length > 0) {
    const node = queue.shift()
    if (adjList[node]) {
      adjList[node].forEach((n) => {
        if (!visited[n]) {
          queue.push(n)
          visited[n] = true
          const d = dist[node] + 1
          if (dist[n] == undefined || d < dist[n]) {
            dist[n] = d
          }
        }
      })
    }
  }
  const dists = Object.values(dist)
  const maxDist = Math.max(...dists)
  return dists.filter((d) => d == maxDist).length
}
solution(6, [
  [3, 6],
  [4, 3],
  [3, 2],
  [1, 3],
  [1, 2],
  [2, 4],
  [5, 2],
])
