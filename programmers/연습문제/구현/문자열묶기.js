function solution(strArr) {
  const obj = {}

  strArr.forEach((str) => {
    const length = str.length

    if (obj[length]) {
      obj[length] = obj[length] + 1
    } else {
      obj[length] = 1
    }
  })

  return Math.max(...Object.values(obj))
}
