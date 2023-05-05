/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const maxVowels = function (s, k) {
  let result = 0,
    count = 0

  if (s.length == 1) {
    return 1
  }

  for (let i = 0; i < s.length; i++) {
    if (["a", "e", "i", "o", "u"].includes(s[i])) {
      count++
    }
    if (i >= k && ["a", "e", "i", "o", "u"].includes(s[i - k])) {
      count--
    }

    if (count === k) {
      return k
    }

    result = Math.max(result, count)
  }
  return result
}
