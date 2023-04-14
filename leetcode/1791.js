/**
 * @param {number[][]} edges
 * @return {number}
 */
const findCenter = function (edges) {
  const nodeCount = new Set()
  const map = new Map()

  for (const [a, b] of edges) {
    nodeCount.add(a)
    nodeCount.add(b)
  }

  const count = nodeCount.size

  for (const node of nodeCount) {
    map.set(node, 0)
  }

  for (const [a, b] of edges) {
    map.set(a, map.get(a) + 1)
    map.set(b, map.get(b) + 1)
  }

  for (const [key, value] of map) {
    if (value === count - 1) {
      return key
    }
  }
}
