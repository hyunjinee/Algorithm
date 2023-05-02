/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
const findTheDifference = function (s, t) {
  if (s === "") return t
  for (let i = 0; i < s.length; i++) {
    const temp = Array.from(t)
    const index = temp.findIndex((x) => x == s[i])

    temp.splice(index, 1)
    t = temp
  }

  if (t.length === 0) {
    return ""
  }

  return t.join("")
}
