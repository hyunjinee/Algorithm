function solution(pin) {
  // 4자리 핀번호 체크
  if (pin[0] === pin[1] && pin[1] === pin[2] && pin[2] === pin[3]) {
    return false
  }

  // 오름 차순 체크
  for (let i = 0; i < 2; i++) {
    const sliced = pin.slice(i, i + 3)

    console.log(sliced)

    if (
      Number(sliced[0]) + 1 === Number(sliced[1]) &&
      Number(sliced[1]) + 1 === Number(sliced[2])
    ) {
      return false
    }
  }
  // 내림 차순 체크
  for (let i = 0; i < 2; i++) {
    const sliced = pin.slice(i, i + 3)

    if (
      Number(sliced[0]) - 1 === Number(sliced[1]) &&
      Number(sliced[1]) - 1 === Number(sliced[2])
    ) {
      return false
    }
  }

  return true
}

console.log(solution("1234")) // false
console.log(solution("1111")) // false
console.log(solution("1434")) // true
console.log(solution("4321")) // false
