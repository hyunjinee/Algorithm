/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function (arr, k) {
  const result = []
  let i = 1
  while (result.length < k) {
    if (!arr.includes(i)) result.push(i)
    i++
  }
  return result[result.length - 1]
}
