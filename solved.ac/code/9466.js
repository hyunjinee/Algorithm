let input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n")
  .slice(1)

let print = ""
while (input.length) {
  const n = +input.shift()
  const list = input
    .shift()
    .split(" ")
    .map((v) => +v)
  const visit = Array(n + 1).fill(0),
    f_visit = Array(n + 1).fill(0)

  const dfs = (start, cur, cnt) => {
    if (visit[cur]) return f_visit[cur] === start ? cnt - visit[cur] : 0

    f_visit[cur] = start
    visit[cur] = cnt
    return dfs(start, list[cur - 1], cnt + 1)
  }

  let cnt = 0
  for (let x = 1; x <= n; x++) if (!visit[x]) cnt += dfs(x, x, 1)
  print += n - cnt + "\n"
}
