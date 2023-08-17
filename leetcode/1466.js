const minReorder = (n, connections) => {
  const graph = []
  const set = new Set()

  for (let i = 0; i < n; i++) {
    graph[i] = []
  }

  for (const [u, v] of connections) {
    graph[u].push(v)
    graph[v].push(u)
    set.add(`${u}#${v}`)
  }

  let count = 0

  dfs(0, -1)

  return count

  function dfs(node, parent) {
    if (set.has(`${parent}#${node}`)) count++
    // 부모에서 자식으로 가는게 있으면 역방향으로 바꿔야함 한개 증가

    for (const nei of graph[node]) {
      if (nei === parent) continue

      dfs(nei, node)
    }
  }
}
