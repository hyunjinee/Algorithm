function solution(n, wires) {
  let answer = Number.MAX_SAFE_INTEGER
  let count = 1

  const visited = Array.from({ length: n + 1 }, () => 0)
  const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0))

  for (const [a, b] of wires) {
    graph[a][b] = 1
    graph[b][a] = 1
  }

  for (const [a, b] of wires) {
    graph[a][b] = 0
    graph[b][a] = 0

    count = 1
    dfs(1)

    graph[a][b] = 1
    graph[b][a] = 1

    answer = Math.min(answer, Math.abs(n - count - count))
  }

  return answer

  function dfs(x) {
    for (let i = 1; i <= n; i++) {
      if (visited[i] === 0 && graph[x][i] === 1) {
        visited[x] = 1
        count++
        dfs(i)
        visited[x] = 0
      }
    }
  }
}
