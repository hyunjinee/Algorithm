const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, m] = inputs[0].split(" ").map(Number)
const jewels = inputs.slice(1).map(Number)

let left = 1,
  right = Math.max(...jewels)
// 한명당 보석을 몇개 줄 것인가
let min = Infinity

while (left <= right) {
  // 일단 중간에서 시작하자
  const mid = Math.floor((left + right) / 2)
  //명당 0개
  let personPerJewel = 0

  for (const jewel of jewels) {
    // 몫 = 몇명에게 줄 수 있는가
    const quotient = Math.floor(jewel / mid)
    personPerJewel += quotient
    // 나머지가 있으면 한명 더 줘야함
    const remainer = jewel % mid

    if (remainer) {
      personPerJewel++
    }
  }
  // 줘야하는게 사람 개수보다 많으면 줄 수 없음 따라서 명당 보석 수를 늘려야한다.
  if (personPerJewel > n) {
    left = mid + 1
  } else {
    // 줄 수 있다면 일단 최솟값에 반영해놓는다.
    min = Math.min(min, mid)
    right = mid - 1
  }
}
// 답 출력
console.log(min)

// while (left <= right) {
//   const mid = Math.ceil((left + right) / 2)
//   const count = arr.reduce((acc, cur) => acc + Math.ceil(cur / mid), 0)
//   if (count > n) {
//     left = mid + 1
//   } else {
//     min = mid
//     right = mid - 1
//   }
// }
// console.log(min)
// while (left <= right) {
//   const mid = Math.ceil((left + right) / 2);
//   const count = arr.reduce((acc, cur) => acc + Math.ceil(cur / mid), 0);
//   if (count > n) {
//       left = mid + 1;
//   } else {
//       min = mid;
//       right = mid - 1;
//   }
// }
// console.log(min);
