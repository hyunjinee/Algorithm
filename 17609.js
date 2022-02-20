function palindrom(word, remain) {
  let left = 0
  let right = word.length - 1

  while (left < right) {
    if (word[left] === word[right]) {
      left++
      right--
    } else if (remain-- > 0) {
      if (palindrom(word.substring(left + 1, right + 1), 0) === 0) return 1
      else if (palindrom(word.substring(left, right), 0) === 0) return 1
      else return 2
    } else {
      return 2
    }
  }

  return 0
}

function solution(lines) {
  const [n, ...words] = lines

  for (let i = 0; i < n; i++) {
    console.log(palindrom(words[i], 1))
  }
}

const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const lines = []
rl.on("line", function (line) {
  lines.push(line)
}).on("close", function () {
  solution(lines)
})
