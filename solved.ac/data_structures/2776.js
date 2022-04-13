let [T, ...I] = (require("fs").readFileSync(0, "utf-8") + "").trim().split("\n")
I = I.map((item) => item.split(" ").map(Number))
const R = []
for (let k = 0; k < I.length; k += 4) {
  const H = new Map()
  for (let i = 0; i < I[k]; i++) H.set(I[k + 1][i], 1)
  for (let i = 0; i < I[k + 2]; i++) R.push(H.get(I[k + 3][i]) ? 1 : 0)
}
console.log(R.join("\n"))
