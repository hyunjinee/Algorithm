const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [a, b] = inputs[0].split(" ")
let result = -1

const temp = []
const visited = Array(a.length).fill(false)

function dfs(curr) {
  if (curr.length === a.length) {
    temp.push(curr)
    return
  }

  for (let i = 0; i < a.length; i++) {
    if (visited[i]) continue
    visited[i] = true
    dfs(curr + a[i])
    visited[i] = false
  }
}

dfs("")

temp
  .filter((x) => {
    let temp = Number(x)
    if (String(temp).length === a.length) {
      return true
    }
  })
  .forEach((t) => {
    t = Number(t)

    if (t < +b && t > result) result = t
  })

console.log(result)
