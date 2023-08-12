const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")

const [n, r, q] = input[0].split(" ").map(Number)
const edges = input
  .slice(1, input.length - q)
  .map((x) => x.split(" ").map(Number))
const queries = input.slice(input.length - q).map(Number)
const tree = Array.from({ length: n + 1 }, () => [])
const cnt = Array.from({ length: n + 1 }, () => 0)
for (let [a, b] of edges) {
  tree[a].push(b)
  tree[b].push(a)
}
function dfs(x) {
  cnt[x] = 1
  for (let y of tree[x]) {
    dfs(y)
    cnt[x] += cnt[y]
  }
}
dfs(r)
queries.map((q) => console.log(cnt[q]))
