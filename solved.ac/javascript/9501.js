const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// 각 우주선마다 최고 속도와 연료 소비율이 조금씩 다르다.
// 연료 소비율은 단위 시간당 소비하는 연료의 양이다.
const t = +inputs.shift()
for (let i = 0; i < t; i++) {
  const [n, d] = inputs.shift().split(" ").map(Number)
  const rockets = inputs.slice(0, n).map((v) => v.split(" ").map(Number))

  for (let jj = 0; jj < n; jj++) {
    inputs.shift()
  }
  let result = 0
  rockets.forEach((rocket) => {
    const [v, f, c] = rocket
    // v 최고 속도
    // f는 연료의 양
    // c는 연료 소비율

    // 목적지까지 갈 수 있는지 확인

    const time = d / v
    const fuel = time * c

    if (fuel <= f) result++
    // 목적지까지 갈 수 있다면 result++
  })
  console.log(result)
}
