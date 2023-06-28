const maxProbability = function (n, edges, succProb, start, end) {
  const nei = Array(n)
    .fill()
    .map(() => [])

  for (let i = 0; i < edges.length; i++) {
    const [a, b] = edges[i]
    nei[a].push([b, succProb[i]])
    nei[b].push([a, succProb[i]])
  }

  const probs = new Array(n).fill(0)
  const queue = [start]
  probs[start] = 1

  while (queue.length) {
    const next = []
    for (const i of queue) {
      for (const [j, p] of nei[i]) {
        if (probs[i] * p > probs[j]) {
          next.push(j)
          probs[j] = probs[i] * p
        }
      }
    }
    queue = next
  }

  return probs[end]
}
