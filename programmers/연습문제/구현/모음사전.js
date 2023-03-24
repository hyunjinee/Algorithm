function solution(word) {
  const alphabets = ["A", "E", "I", "O", "U"]
  const words = []

  backTracking("")

  function backTracking(x) {
    if (x.length <= 5) {
      words.push(x)
    }

    if (x.length === 5) {
      return
    }
    for (let i = 0; i < 5; i++) {
      console.log(alphabets[i])
      const temp = x + alphabets[i]
      backTracking(temp)
    }
  }
  console.log(words)
  return words.indexOf(word)
  // console.log(words)
}

// 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는 길이 5이하의 모든 단어가 수록되어 있다.
// 사전에서 첫 번째 단어는 "A", 두 번째 단어는 "AA"이며, 마지막 단어는 "UUUUU"이다.

// 단어하나 word가 매개변수로 주어질때, 이 단어가 사전에서 몇 번째인지 return 하도록 solution 함수를 완성해주세요.

solution("AAAAE") // 6
solution("AAAE") // 10
solution("I") // 1563
solution("EIO") // 1189
