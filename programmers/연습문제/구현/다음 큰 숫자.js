function solution(n) {
  const nBinary = n.toString(2)
  const nBinaryOneCount = nBinary.split("").filter((v) => v === "1").length

  let answer = n + 1

  while (true) {
    const answerBinary = answer.toString(2)
    const answerBinaryOneCount = answerBinary
      .split("")
      .filter((v) => v === "1").length

    if (nBinaryOneCount === answerBinaryOneCount) {
      return answer
    }
    answer += 1
  }

  return answer
}

// String to Binary

// (n).toString(2)
