const stdin = require("fs").readFileSync("./dev/stdin").toString().trim()
let [N, ops] = stdin.split("\n")
N = Number(N)
ops = Array.from(ops).map((v, i) => (i & 1 ? v : Number(v)))

console.log(ops)
const operate = ([amax, amin], op, [bmax, bmin]) => {
  switch (op) {
    case "+":
      return [amax + bmax, amin + bmin]
    case "-":
      return [amax - bmin, amin - bmax]
    case "*":
      const cases = [amax * bmax, amax * bmin, amin * bmax, amin * bmin]
      return [Math.max(...cases), Math.min(...cases)]
  }
}
const nums = (N + 1) / 2
let memo = []
memo[0] = [...Array(nums)].map((v, i) => [...Array(2)].fill(ops[i * 2]))

console.log(memo)
const get = (s, f) => memo[f - s][s]
for (let gap = 1; gap < nums; gap++) {
  memo[gap] = []
  for (let i = 0; i < nums - gap; i++) {
    let [max, min] = operate(get(i, i), ops[2 * i + 1], get(i + 1, i + gap))
    for (let j = i + 1; j < i + gap; j++) {
      const [tempMax, tempMin] = operate(get(i, j), ops[2 * j + 1], get(j + 1, i + gap))
      tempMax > max && (max = tempMax)
      tempMin < min && (min = tempMin)
    }
    memo[gap].push([max, min])
  }
}
console.log(memo)
console.log(memo[nums - 1][0][0])
