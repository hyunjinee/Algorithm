function solution(price, money, count) {
  // 놀이기구를 count 번 타면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록
  // 금액이 부족하지 않으면 0을 리턴하세요
  let counter = 0

  for (let i = 1; i <= count; i++) {
    counter += i
  }

  console.log(counter)

  const total = price * counter

  return money - total >= 0 ? 0 : total - money
}

// 제한 1 <= price <= 2500
// money 1 <= money <= 1000,000,000
// count 1 <= count <= 2,500

console.log(solution(3, 20, 4)) // 10
console.log(solution(3, 20, 5)) // 25

// function solution(price, money, count) {
//   let answer = 0

//   for (let i = 1; i <= count; i++) {
//     answer += price * i
//   }

//   return answer - money > 0 ? answer - money : 0
// }
