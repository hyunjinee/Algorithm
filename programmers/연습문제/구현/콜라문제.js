const solution = (a, b, n) => {
  let answer = 0
  let remain = n

  while (true) {
    if (a > remain) {
      break
    }
    answer += parseInt(remain / a) * b
    remain = parseInt(remain / a) * b + (remain % a)
  }

  return answer
}
