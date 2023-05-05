/**
 * @param {number} n
 * @return {number}
 */
const integerReplacement = function (n) {
  const q = [[n, 0]]

  while (q.length) {
    const [x, cnt] = q.shift()

    if (x === 1) {
      return cnt
    }

    if (x % 2 === 0) {
      q.push([x / 2, cnt + 1])
    } else {
      q.push([x + 1, cnt + 1])
      q.push([x - 1, cnt + 1])
    }
  }
}
