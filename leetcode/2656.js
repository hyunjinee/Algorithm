function maximizeSum(nums, k) {
  let result = 0
  let max = Math.max(...nums)

  for (let i = 0; i < k; i++) {
    result += max
    max += 1
  }

  return result
}
