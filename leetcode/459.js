/**
 * @param {string} s
 * @return {boolean}
 */
const repeatedSubstringPattern = function (s) {
  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j < s.length; j++) {
      const t = s.slice(i, j)

      const replaced = s.replaceAll(t, "")

      console.log(replaced)

      if (replaced === "") return true
    }
  }

  return false
  // given a string s , check if it can be c
}

repeatedSubstringPattern("abab")

// 시간 초과를 어떻게 해결할까?
