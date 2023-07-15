const areSentencesSimilar = function (sentence1, sentence2) {
  if (sentence1 === sentence2) return true
  if (sentence2.length > sentence1.length) [sentence1, sentence2] = [sentence2, sentence1]
  let long = sentence1.split(" ")
  let short = sentence2.split(" ")
  while (long[0] === short[0]) long.shift(), short.shift()
  while (long[long.length - 1] === short[short.length - 1]) long.pop(), short.pop()
  return short.length === 0
}
