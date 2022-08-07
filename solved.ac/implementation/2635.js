let N = parseInt(require("fs").readFileSync("/dev/stdin").toString().trim())
let res = [0]
for (let i = 1; i <= N; ++i) {
  let l = [N, i]
  while (l[l.length - 2] - l[l.length - 1] >= 0) {
    l.push(l[l.length - 2] - l[l.length - 1])
  }
  if (l.length > res.length) {
    res = l
  }
}
console.log(res.length)
