let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
console.log(solution(input))

function solution(trees) {
  let answer = ""
  let treeMap = new Map()
  let count = trees.length
  for (const tree of trees) {
    if (!treeMap.has(tree)) {
      treeMap.set(tree, 1)
      continue
    }
    treeMap.set(tree, treeMap.get(tree) + 1)
  }
  for (const [key, value] of treeMap) {
    treeMap.set(key, ((value / count) * 100).toFixed(4))
  }

  let treeArr = [...treeMap.entries()].sort((a, b) => {
    if (a[0] < b[0]) return -1
  })

  return treeArr.map((tree) => tree.join(" ")).join("\n")
}
