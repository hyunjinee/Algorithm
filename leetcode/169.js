/**
 * @param {number[]} nums
 * @return {number}
 */
const majorityElement = function (nums) {
  const map = new Map()

  nums.forEach((num) => {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1)
    } else {
      map.set(num, 1)
    }
  })

  let temp = -Infinity

  let result

  for (const [key, value] of map) {
    if (temp < value) {
      temp = value
      result = key
    }
  }

  return result
}

majorityElement([3, 2, 3])
