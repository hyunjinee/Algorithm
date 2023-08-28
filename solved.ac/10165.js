const inputs = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs.shift()
const m = +inputs.shift()

let road = inputs.map((x) => x.split(" ").map(Number)).map((x, i) => [x[0], x[1], i + 1])

const ascending = road.filter((x) => x[0] < x[1])
const descending = road.filter((x) => x[0] > x[1]).map((x) => [x[1], x[0], x[2]])

// 재밌는 사실. 역으로 가는 친구는 스위칭을 해줬을 때 거기에 포함되지 않는 나머지가 존재한다면  그 친구는 삭제할 수 있는
// 친구로 취급할 수 있다.

ascending.sort((a, b) => {
  if (a[0] > b[0]) {
    return 1
  } else if (a[0] < b[0]) {
    return -1
  } else {
    return a[1] - b[1]
  }
})

const removeIndexSet = new Set()

for (let i = 0; i < ascending.length; i++) {
  for (let j = i + 1; j < ascending.length; j++) {
    if (ascending[i][0] <= ascending[j][0] && ascending[i][1] >= ascending[j][1]) {
      removeIndexSet.add(ascending[j][2])
    }
  }
}

descending.forEach((x) => {
  const [start, end, index] = x
  for (let i = 0; i < ascending.length; i++) {
    const [ss, ee, ii] = ascending[i]

    if (start <= ss && end >= ee) {
      removeIndexSet.add(ii)
    } else {
    }
  }
})

console.log(
  Array(m + 1)
    .fill()
    .map((_, i) => i)
    .filter((x) => {
      if (!removeIndexSet.has(x) && x > 0) {
        return true
      }
    })
    .join(" ")
)
