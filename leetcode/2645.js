const addMinimum = function (word) {
  let res = 0,
    str = "abc".repeat(word.length)
  let pointerInWord = 0,
    pointerInStr = 0

  while (pointerInWord < word.length) {
    if (word[pointerInWord] === str[pointerInStr]) {
      pointerInWord++
    } else {
      res++
    }
    pointerInStr++
  }
  word[pointerInWord - 1] === "a"
    ? (res += 2)
    : word[pointerInWord - 1] === "b"
    ? (res += 1)
    : null
  return res
}
