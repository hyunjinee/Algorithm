/**
 * @param {number} num
 * @return {boolean}
 */
const checkPerfectNumber = function (num) {
  const temp = []

  for (let i = 1; i < num; i++) {
    if (num % i == 0) {
      temp.push(i)
    }
  }

  const result = temp.reduce((a, x) => a + x, 0)

  if (result === num) {
    return true
  }

  return false
}
