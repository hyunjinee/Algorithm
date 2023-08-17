/**
 * @param {number[][]} bombs
 * @return {number}
 */
const maximumDetonation = function (bombs) {
  const num = bombs.length
  const graph = {}
  for (let i = 0; i < num; i++) {
    graph[i] = []
    const [x1, y1, r1] = bombs[i]
    for (let j = 0; j < num; j++) {
      const [x2, y2] = bombs[j]
      if (distance(x1, x2, y1, y2) <= r1) {
        graph[i].push(j)
      }
    }
  }
  let max = 1
  for (let i in graph) {
    const set = new Set()
    graph[i].forEach((val) => set.add(val))
    console.log(set)
    set.forEach((val) => {
      graph[val].forEach((val2) => set.add(val2))
    })
    console.log(set)
    if (set.size > max) max = set.size
  }
  return max
}

function distance(x1, x2, y1, y2) {
  return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
}
