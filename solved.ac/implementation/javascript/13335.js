// w 대의 트럭만 동시에 올라갈 수 있다.
// 다리의 길이는 w 단위 길이 이며, 각 트럭들은 하나의 단위 시간에 하나의 단위 길이 만큼이동
// 다리의 최대 하중 L

// ddd
const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, w, L] = input[0].split(" ").map(Number)
const trucks = input[1].split(" ").map(Number)

let curWeight = 0
let t = 0

const arr = []

while (trucks.length !== 0) {
  if (arr.length >= w) {
    curWeight -= arr.shift()
  }
  if (curWeight + trucks[0] <= L) {
    const truck = trucks.shift()
    arr.push(truck)
    curWeight += truck
  } else {
    arr.push(0)
  }
  t++
}

t += w

console.log(t)
// const bridgeCrossTime = w
// const bridgeHoldTruckCount = w

// let time = 0
// const currentBridgeTrucks = []

// while (trucks.length) {
//   currentBridgeTrucks.forEach((truck) => (truck[1] += 1))

//   if (currentBridgeTrucks.length < bridgeHoldTruckCount) {
//     currentBridgeTrucks.push([trucks.shift(), 0])
//   }

//   // const truck = trucks.shift()
// }
