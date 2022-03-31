const ladderLength = function (beginWord, endWord, wordList) {
  // 인접한거는 한 단어만 다르다.
  if (!wordList.includes(endWord)) return 0

  const wordSet = new Set(wordList)
  let queue = [beginWord]
  let steps = 1

  while (queue.length) {
    const next = []
    for (let word of queue) {
      if (word === endWord) return steps

      for (let i = 0; i < word.length; i++) {
        for (let j = 0; j < 26; j++) {
          const newWord =
            word.slice(0, i) + String.fromCharCode(j + 97) + word.slice(i + 1)
          if (wordSet.has(newWord)) {
            next.push(newWord)
            wordSet.delete(newWord)
          }
        }
      }
    }
    queue = next
    steps++
  }
  return 0
}
