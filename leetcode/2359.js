const closestMeetingNode = function (edges, node1, node2) {
  const n = edges.length
  const distanceOne = new Array(n).fill(Infinity)
  const visitedOne = new Array(n).fill(false)
  const distanceTwo = new Array(n).fill(Infinity)
  const visitedTwo = new Array(n).fill(false)

  dfs(edges, node1, distanceOne, visitedOne, 0)
  dfs(edges, node2, distanceTwo, visitedTwo, 0)

  let ans = -1
  let minDistance = Infinity
  for (let i = 0; i < n; i++) {
    const maxDistance = Math.max(distanceOne[i], distanceTwo[i])
    if (maxDistance < minDistance) {
      ans = i
      minDistance = maxDistance
    }
  }

  return ans
}

function dfs(edges, node, distance, visited, curr) {
  visited[node] = true
  distance[node] = curr

  const next = edges[node]
  if (next !== -1 && !visited[next]) {
    dfs(edges, next, distance, visited, curr + 1)
  }
}
