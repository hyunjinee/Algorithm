const longestSubsequence = (arr, diff) => {
  const map = new Map()
  let max = 0

  for (const num of arr) {
    const prev = map.has(num - diff) ? map.get(num - diff) : 0
    const val = prev + 1

    map.set(num, val)

    max = Math.max(max, val)
  }

  return max
}
