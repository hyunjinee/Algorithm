function solution(s) {
  let answer = 0
  let fixedChar = ""
  let cnt1 = 0
  let cnt2 = 0

  for (let c of s) {
    if (!fixedChar) fixedChar = c

    if (fixedChar === c) {
      cnt1++
    } else {
      cnt2++
    }

    if (cnt1 === cnt2) {
      answer++
      cnt1 = 0
      cnt2 = 0
      fixedChar = ""
    }
  }

  if (fixedChar) answer++

  return answer
}

const aa = "bab".slice(1)
console.log(aa)
