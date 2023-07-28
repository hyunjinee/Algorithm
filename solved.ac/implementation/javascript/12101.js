const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim()

const [n, k] = input.split(" ").map(Number)
const ans = []

function dfs(curr) {
  if (curr.reduce((a, c) => a + c, 0) > n) {
    return
  }
  if (curr.reduce((a, c) => a + c, 0) === n) {
    ans.push(curr)

    return
  }

  for (let i = 1; i < 4; i++) {
    dfs([...curr, i])
  }
}

dfs([])
if (ans[k - 1]) {
  console.log(ans[k - 1].join("+"))
} else {
  console.log(-1)
}
