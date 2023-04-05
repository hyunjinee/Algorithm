function solution(price, money, count) {
  let temp = 0

  for (let i = 1; i <= count; i++) {
    temp += i * price
  }

  if (money > temp) {
    return 0
  }

  return temp - money
}
